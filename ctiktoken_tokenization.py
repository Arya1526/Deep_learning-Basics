{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "676046b8-7524-48b9-b05f-eb4e527994f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting tiktoken\n",
      "  Downloading tiktoken-0.13.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (6.7 kB)\n",
      "Requirement already satisfied: regex in /opt/anaconda3/lib/python3.12/site-packages (from tiktoken) (2024.9.11)\n",
      "Requirement already satisfied: requests in /opt/anaconda3/lib/python3.12/site-packages (from tiktoken) (2.32.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/anaconda3/lib/python3.12/site-packages (from requests->tiktoken) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/lib/python3.12/site-packages (from requests->tiktoken) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/anaconda3/lib/python3.12/site-packages (from requests->tiktoken) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.12/site-packages (from requests->tiktoken) (2026.4.22)\n",
      "Downloading tiktoken-0.13.0-cp312-cp312-macosx_11_0_arm64.whl (982 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m983.0/983.0 kB\u001b[0m \u001b[31m2.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m-:--:--\u001b[0m\n",
      "\u001b[?25hInstalling collected packages: tiktoken\n",
      "Successfully installed tiktoken-0.13.0\n",
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
   "id": "49f8a47d-878d-4668-8d80-79b15e36ca41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============================================================\n",
      "English Sentence\n",
      "------------------------------------------------------------\n",
      "Original Text:\n",
      "Artificial Intelligence is transforming the world.\n",
      "\n",
      "Tokens:\n",
      "['Art', 'ificial', ' Intelligence', ' is', ' transforming', ' the', ' world', '.']\n",
      "\n",
      "Token Count: 8\n",
      "\n",
      "============================================================\n",
      "Python Function\n",
      "------------------------------------------------------------\n",
      "Original Text:\n",
      "\n",
      "def add(a, b):\n",
      "    return a + b\n",
      "\n",
      "\n",
      "Tokens:\n",
      "['\\n', 'def', ' add', '(a', ',', ' b', '):\\n', '   ', ' return', ' a', ' +', ' b', '\\n']\n",
      "\n",
      "Token Count: 13\n",
      "\n",
      "============================================================\n",
      "Native Language Sentence\n",
      "------------------------------------------------------------\n",
      "Original Text:\n",
      "എനിക്ക് പൈത്തൺ പഠിക്കാൻ ഇഷ്ടമാണ്\n",
      "\n",
      "Tokens:\n",
      "['�', '�', '�', '�', '�', '�', '�', '�', '്�', '�', '്', ' �', '�', '�', '�', '�', '�', '�', '്�', '�', '�', '�', ' �', '�', '�', '�', '�', '�', '�', '�', '�', '്�', '�', '�', '�', '�', '�', ' �', '�', '�', '�', '�', '്�', '�', '�', '�', '�', '�', '�', '�', '്']\n",
      "\n",
      "Token Count: 51\n",
      "\n",
      "============================================================\n",
      "Number\n",
      "------------------------------------------------------------\n",
      "Original Text:\n",
      "1234567\n",
      "\n",
      "Tokens:\n",
      "['123', '456', '7']\n",
      "\n",
      "Token Count: 3\n",
      "\n",
      "============================================================\n",
      "Email Address\n",
      "------------------------------------------------------------\n",
      "Original Text:\n",
      "student123@gmail.com\n",
      "\n",
      "Tokens:\n",
      "['student', '123', '@gmail', '.com']\n",
      "\n",
      "Token Count: 4\n",
      "\n",
      "============================================================\n",
      "Mathematical Notation\n",
      "------------------------------------------------------------\n",
      "Original Text:\n",
      "f(x) = x^2 + 3x + 5\n",
      "\n",
      "Tokens:\n",
      "['f', '(x', ')', ' =', ' x', '^', '2', ' +', ' ', '3', 'x', ' +', ' ', '5']\n",
      "\n",
      "Token Count: 14\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import tiktoken\n",
    "\n",
    "encoding = tiktoken.get_encoding(\"cl100k_base\")\n",
    "\n",
    "inputs = {\n",
    "    \"English Sentence\": \"Artificial Intelligence is transforming the world.\",\n",
    "\n",
    "    \"Python Function\": \"\"\"\n",
    "def add(a, b):\n",
    "    return a + b\n",
    "\"\"\",\n",
    "\n",
    "    \"Native Language Sentence\": \"എനിക്ക് പൈത്തൺ പഠിക്കാൻ ഇഷ്ടമാണ്\",\n",
    "\n",
    "    \"Number\": \"1234567\",\n",
    "\n",
    "    \"Email Address\": \"student123@gmail.com\",\n",
    "\n",
    "    \"Mathematical Notation\": \"f(x) = x^2 + 3x + 5\"\n",
    "}\n",
    "\n",
    "for title, text in inputs.items():\n",
    "    print(\"=\" * 60)\n",
    "    print(title)\n",
    "    print(\"-\" * 60)\n",
    "\n",
    "    token_ids = encoding.encode(text)\n",
    "\n",
    "    token_strings = [encoding.decode([token]) for token in token_ids]\n",
    "\n",
    "    print(\"Original Text:\")\n",
    "    print(text)\n",
    "\n",
    "    print(\"\\nTokens:\")\n",
    "    print(token_strings)\n",
    "\n",
    "    print(\"\\nToken Count:\", len(token_ids))\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2d3fb3f2-bcde-409a-91a1-5615c79e1005",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Observations:\n",
      "\n",
      "1. The English sentence was split into meaningful word parts instead of individual characters.\n",
      "   Common words and spaces were grouped into fewer tokens.\n",
      "\n",
      "2. The Malayalam sentence used more tokens because many native-language characters\n",
      "   were divided into smaller pieces.\n",
      "\n",
      "3. The email address and mathematical notation were separated into symbols,\n",
      "   numbers, and text parts individually.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"\"\"\n",
    "Observations:\n",
    "\n",
    "1. The English sentence was split into meaningful word parts instead of individual characters.\n",
    "   Common words and spaces were grouped into fewer tokens.\n",
    "\n",
    "2. The Malayalam sentence used more tokens because many native-language characters\n",
    "   were divided into smaller pieces.\n",
    "\n",
    "3. The email address and mathematical notation were separated into symbols,\n",
    "   numbers, and text parts individually.\n",
    "\"\"\")"
   ]
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
