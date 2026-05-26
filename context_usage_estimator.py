{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "470c515f-6b3e-47ce-8622-d1a4acc456d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tiktoken in /opt/anaconda3/lib/python3.12/site-packages (0.13.0)\n",
      "Requirement already satisfied: regex in /opt/anaconda3/lib/python3.12/site-packages (from tiktoken) (2024.9.11)\n",
      "Requirement already satisfied: requests in /opt/anaconda3/lib/python3.12/site-packages (from tiktoken) (2.32.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/anaconda3/lib/python3.12/site-packages (from requests->tiktoken) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/lib/python3.12/site-packages (from requests->tiktoken) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/anaconda3/lib/python3.12/site-packages (from requests->tiktoken) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.12/site-packages (from requests->tiktoken) (2026.4.22)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install tiktoken"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "034ad42e-1500-4712-99d0-e5b32b7db4fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tiktoken\n",
    "\n",
    "encoding = tiktoken.get_encoding(\"cl100k_base\")\n",
    "\n",
    "MODEL_LIMIT = 8192\n",
    "\n",
    "def estimate_context_usage(messages_list):\n",
    "\n",
    "    total_tokens = 0\n",
    "\n",
    "    for message in messages_list:\n",
    "\n",
    "        text = message[\"content\"]\n",
    "\n",
    "        tokens = encoding.encode(text)\n",
    "\n",
    "        total_tokens += len(tokens)\n",
    "\n",
    "    usage_percent = (total_tokens / MODEL_LIMIT) * 100\n",
    "\n",
    "    print(\"=\" * 60)\n",
    "    print(\"Total Tokens:\", total_tokens)\n",
    "    print(\"Model Limit:\", MODEL_LIMIT)\n",
    "    print(f\"Usage: {usage_percent:.2f}%\")\n",
    "    print(\"=\" * 60)\n",
    "\n",
    "    if usage_percent > 80:\n",
    "        print(\"WARNING: Context usage exceeded 80% of model limit.\")\n",
    "    else:\n",
    "        print(\"Context usage is within safe range.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9152aa26-e7f4-4ae6-a1e2-3d006e4fa457",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============================================================\n",
      "Total Tokens: 150157\n",
      "Model Limit: 8192\n",
      "Usage: 1832.97%\n",
      "============================================================\n",
      "WARNING: Context usage exceeded 80% of model limit.\n"
     ]
    }
   ],
   "source": [
    "messages = [\n",
    "    {\n",
    "        \"role\": \"system\",\n",
    "        \"content\": \"You are a Python programming assistant.\"\n",
    "    }\n",
    "]\n",
    "\n",
    "large_text = \"\"\"\n",
    "Python is a high-level programming language used for web development,\n",
    "data science, machine learning, automation, and many other applications.\n",
    "\"\"\" * 200\n",
    "\n",
    "for i in range(15):\n",
    "\n",
    "    messages.append(\n",
    "        {\n",
    "            \"role\": \"user\",\n",
    "            \"content\": f\"Question {i+1}: {large_text}\"\n",
    "        }\n",
    "    )\n",
    "\n",
    "    messages.append(\n",
    "        {\n",
    "            \"role\": \"assistant\",\n",
    "            \"content\": f\"Answer {i+1}: {large_text}\"\n",
    "        }\n",
    "    )\n",
    "\n",
    "estimate_context_usage(messages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f10d604-f6fd-4b43-beb9-de25fa6b103a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
