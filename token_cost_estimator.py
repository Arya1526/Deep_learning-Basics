{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "185f3c15-9fee-4488-aa93-403cb24bf5d6",
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
   "execution_count": 3,
   "id": "a020c27e-3551-43ce-9be7-ccc4a86800c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tiktoken\n",
    "import pandas as pd\n",
    "\n",
    "encoding = tiktoken.get_encoding(\"cl100k_base\")\n",
    "\n",
    "def token_cost(text, price_per_million=0.10):\n",
    "    tokens = encoding.encode(text)\n",
    "    token_count = len(tokens)\n",
    "\n",
    "    cost = (token_count / 1_000_000) * price_per_million\n",
    "\n",
    "    return token_count, cost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4faa6252-207b-4075-aa3f-e54d88859672",
   "metadata": {},
   "outputs": [],
   "source": [
    "paragraph = \"\"\"\n",
    "Artificial intelligence is rapidly changing the way people work, communicate,\n",
    "and solve problems across industries. From healthcare and education to finance\n",
    "and entertainment, AI systems are being integrated into everyday tools and\n",
    "services. Machine learning models can analyze large datasets quickly, helping\n",
    "organizations make data-driven decisions. Natural language processing allows\n",
    "computers to understand and generate human language, enabling chatbots,\n",
    "translation systems, and virtual assistants. As AI technologies continue to\n",
    "advance, ethical considerations such as privacy, fairness, and transparency\n",
    "become increasingly important. Governments, researchers, and companies are\n",
    "working together to establish guidelines for responsible AI development and\n",
    "deployment. The future of AI promises both exciting opportunities and\n",
    "significant challenges that society must carefully navigate.\n",
    "\"\"\" * 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6cbfec09-117f-4326-a426-8125888f8297",
   "metadata": {},
   "outputs": [],
   "source": [
    "python_script = \"\"\"\n",
    "def add(a, b):\n",
    "    return a + b\n",
    "\n",
    "def subtract(a, b):\n",
    "    return a - b\n",
    "\n",
    "for i in range(50):\n",
    "    print(add(i, i))\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "89f50879-4e03-477e-860f-26c998030c3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "conversation = \"\"\"\n",
    "User: Hi, how are you?\n",
    "Assistant: I am doing well. How can I help you today?\n",
    "\n",
    "User: Explain machine learning in simple terms.\n",
    "Assistant: Machine learning is a method where computers learn patterns from data.\n",
    "\n",
    "User: Give me one real-life example.\n",
    "Assistant: Recommendation systems used by streaming platforms are a common example.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a17c1ab1-3124-4a06-a168-a488d1a38adb",
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
