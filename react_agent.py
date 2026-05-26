{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c9c60ff8-0c23-4f84-a586-37093484e40d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Problem: Find 10% of the population of India.\n",
      "\n",
      "Thought: I need to look up the population of India.\n",
      "Action: lookup('population of india')\n",
      "Observation: 1.44 billion\n",
      "\n",
      "Thought: Convert 1.44 billion into number form.\n",
      "Thought: Now calculate 10% of the population.\n",
      "Action: calculate(1440000000.0 * 0.10)\n",
      "Observation: 144000000.0\n",
      "\n",
      "Final Answer:\n",
      "10% of India's population is 144000000\n"
     ]
    }
   ],
   "source": [
    "facts = {\n",
    "    \"population of india\": \"1.44 billion\",\n",
    "    \"speed of light\": \"3x10^8 m/s\"\n",
    "}\n",
    "\n",
    "def lookup(fact):\n",
    "    return facts.get(fact.lower(), \"Fact not found\")\n",
    "\n",
    "def calculate(expression):\n",
    "    return eval(expression)\n",
    "\n",
    "def react_agent(problem):\n",
    "    print(\"Problem:\", problem)\n",
    "    print()\n",
    "\n",
    "    print(\"Thought: I need to look up the population of India.\")\n",
    "    population = lookup(\"population of india\")\n",
    "\n",
    "    print(\"Action: lookup('population of india')\")\n",
    "    print(\"Observation:\", population)\n",
    "    print()\n",
    "\n",
    "    print(\"Thought: Convert 1.44 billion into number form.\")\n",
    "    population_number = 1.44 * 1000000000\n",
    "\n",
    "    print(\"Thought: Now calculate 10% of the population.\")\n",
    "    result = calculate(f\"{population_number} * 0.10\")\n",
    "\n",
    "    print(f\"Action: calculate({population_number} * 0.10)\")\n",
    "    print(\"Observation:\", result)\n",
    "    print()\n",
    "\n",
    "    print(\"Final Answer:\")\n",
    "    print(\"10% of India's population is\", int(result))\n",
    "\n",
    "problem = \"Find 10% of the population of India.\"\n",
    "\n",
    "react_agent(problem)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "424ed32a-a07c-4722-ab34-223c2db87167",
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
