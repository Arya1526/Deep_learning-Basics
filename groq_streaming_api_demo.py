{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d493a5b2-da4e-4414-91b9-489d9dad2b9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: groq in /opt/anaconda3/lib/python3.12/site-packages (1.2.0)\n",
      "Requirement already satisfied: anyio<5,>=3.5.0 in /opt/anaconda3/lib/python3.12/site-packages (from groq) (4.2.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in /opt/anaconda3/lib/python3.12/site-packages (from groq) (1.9.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in /opt/anaconda3/lib/python3.12/site-packages (from groq) (0.27.0)\n",
      "Requirement already satisfied: pydantic<3,>=1.9.0 in /opt/anaconda3/lib/python3.12/site-packages (from groq) (2.8.2)\n",
      "Requirement already satisfied: sniffio in /opt/anaconda3/lib/python3.12/site-packages (from groq) (1.3.0)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.14 in /opt/anaconda3/lib/python3.12/site-packages (from groq) (4.14.0)\n",
      "Requirement already satisfied: idna>=2.8 in /opt/anaconda3/lib/python3.12/site-packages (from anyio<5,>=3.5.0->groq) (3.7)\n",
      "Requirement already satisfied: certifi in /opt/anaconda3/lib/python3.12/site-packages (from httpx<1,>=0.23.0->groq) (2026.4.22)\n",
      "Requirement already satisfied: httpcore==1.* in /opt/anaconda3/lib/python3.12/site-packages (from httpx<1,>=0.23.0->groq) (1.0.2)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in /opt/anaconda3/lib/python3.12/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->groq) (0.14.0)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in /opt/anaconda3/lib/python3.12/site-packages (from pydantic<3,>=1.9.0->groq) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.20.1 in /opt/anaconda3/lib/python3.12/site-packages (from pydantic<3,>=1.9.0->groq) (2.20.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install groq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "978a0419-2c51-4561-97f2-950267824344",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Streaming Poem:\n",
      "\n",
      "Silver crescent in the night,\n",
      "A glowing orb, a gentle light.\n",
      "The moon's soft beams upon us shine,\n",
      " Illuminating all that's divine.\n",
      "\n",
      "With phases marked, it waxes and wanes,\n",
      "A constant change, yet steady remains.\n",
      "A beacon in the darkened sky,\n",
      "The moon's serene beauty catches the eye.\n",
      "\n",
      "In ancient myths, it's a mystic spell,\n",
      "A symbol of magic, and stories to tell.\n",
      "The moon's enchantment is a wondrous sight,\n",
      "A celestial wonder, in all its light."
     ]
    }
   ],
   "source": [
    "from groq import Groq\n",
    "import time\n",
    "\n",
    "client = Groq(\n",
    "    api_key=\"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\"\n",
    ")\n",
    "\n",
    "print(\"Streaming Poem:\\n\")\n",
    "\n",
    "stream = client.chat.completions.create(\n",
    "    model=\"llama-3.1-8b-instant\",\n",
    "    messages=[\n",
    "        {\n",
    "            \"role\": \"user\",\n",
    "            \"content\": \"Write a short poem about the moon.\"\n",
    "        }\n",
    "    ],\n",
    "    temperature=0.7,\n",
    "    stream=True\n",
    ")\n",
    "\n",
    "for chunk in stream:\n",
    "\n",
    "    token = chunk.choices[0].delta.content\n",
    "\n",
    "    if token:\n",
    "        print(token, end=\"\", flush=True)\n",
    "        time.sleep(0.02)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "aa72fc2a-cbc2-4b47-b6d4-7704b2a3340b",
   "metadata": {},
   "outputs": [
    {
     "ename": "AuthenticationError",
     "evalue": "Error code: 401 - {'error': {'message': 'Invalid API Key', 'type': 'invalid_request_error', 'code': 'invalid_api_key'}}",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAuthenticationError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[6], line 12\u001b[0m\n\u001b[1;32m      8\u001b[0m tokens \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m     10\u001b[0m start_time \u001b[38;5;241m=\u001b[39m time\u001b[38;5;241m.\u001b[39mtime()\n\u001b[0;32m---> 12\u001b[0m stream \u001b[38;5;241m=\u001b[39m client\u001b[38;5;241m.\u001b[39mchat\u001b[38;5;241m.\u001b[39mcompletions\u001b[38;5;241m.\u001b[39mcreate(\n\u001b[1;32m     13\u001b[0m     model\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mllama-3.1-8b-instant\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     14\u001b[0m     messages\u001b[38;5;241m=\u001b[39m[\n\u001b[1;32m     15\u001b[0m         {\n\u001b[1;32m     16\u001b[0m             \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrole\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124muser\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     17\u001b[0m             \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcontent\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWrite a short poem about the moon.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     18\u001b[0m         }\n\u001b[1;32m     19\u001b[0m     ],\n\u001b[1;32m     20\u001b[0m     temperature\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0.7\u001b[39m,\n\u001b[1;32m     21\u001b[0m     stream\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m     22\u001b[0m )\n\u001b[1;32m     24\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGenerated Poem:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     26\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m chunk \u001b[38;5;129;01min\u001b[39;00m stream:\n",
      "File \u001b[0;32m/opt/anaconda3/lib/python3.12/site-packages/groq/resources/chat/completions.py:461\u001b[0m, in \u001b[0;36mCompletions.create\u001b[0;34m(self, messages, model, citation_options, compound_custom, disable_tool_validation, documents, exclude_domains, frequency_penalty, function_call, functions, include_domains, include_reasoning, logit_bias, logprobs, max_completion_tokens, max_tokens, metadata, n, parallel_tool_calls, presence_penalty, reasoning_effort, reasoning_format, response_format, search_settings, seed, service_tier, stop, store, stream, temperature, tool_choice, tools, top_logprobs, top_p, user, extra_headers, extra_query, extra_body, timeout)\u001b[0m\n\u001b[1;32m    241\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mcreate\u001b[39m(\n\u001b[1;32m    242\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m    243\u001b[0m     \u001b[38;5;241m*\u001b[39m,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    300\u001b[0m     timeout: \u001b[38;5;28mfloat\u001b[39m \u001b[38;5;241m|\u001b[39m httpx\u001b[38;5;241m.\u001b[39mTimeout \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m|\u001b[39m NotGiven \u001b[38;5;241m=\u001b[39m not_given,\n\u001b[1;32m    301\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m ChatCompletion \u001b[38;5;241m|\u001b[39m Stream[ChatCompletionChunk]:\n\u001b[1;32m    302\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    303\u001b[0m \u001b[38;5;124;03m    Creates a model response for the given chat conversation.\u001b[39;00m\n\u001b[1;32m    304\u001b[0m \n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    459\u001b[0m \u001b[38;5;124;03m      timeout: Override the client-level default timeout for this request, in seconds\u001b[39;00m\n\u001b[1;32m    460\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 461\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_post(\n\u001b[1;32m    462\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m/openai/v1/chat/completions\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m    463\u001b[0m         body\u001b[38;5;241m=\u001b[39mmaybe_transform(\n\u001b[1;32m    464\u001b[0m             {\n\u001b[1;32m    465\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmessages\u001b[39m\u001b[38;5;124m\"\u001b[39m: messages,\n\u001b[1;32m    466\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmodel\u001b[39m\u001b[38;5;124m\"\u001b[39m: model,\n\u001b[1;32m    467\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcitation_options\u001b[39m\u001b[38;5;124m\"\u001b[39m: citation_options,\n\u001b[1;32m    468\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcompound_custom\u001b[39m\u001b[38;5;124m\"\u001b[39m: compound_custom,\n\u001b[1;32m    469\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisable_tool_validation\u001b[39m\u001b[38;5;124m\"\u001b[39m: disable_tool_validation,\n\u001b[1;32m    470\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdocuments\u001b[39m\u001b[38;5;124m\"\u001b[39m: documents,\n\u001b[1;32m    471\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexclude_domains\u001b[39m\u001b[38;5;124m\"\u001b[39m: exclude_domains,\n\u001b[1;32m    472\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfrequency_penalty\u001b[39m\u001b[38;5;124m\"\u001b[39m: frequency_penalty,\n\u001b[1;32m    473\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfunction_call\u001b[39m\u001b[38;5;124m\"\u001b[39m: function_call,\n\u001b[1;32m    474\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfunctions\u001b[39m\u001b[38;5;124m\"\u001b[39m: functions,\n\u001b[1;32m    475\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124minclude_domains\u001b[39m\u001b[38;5;124m\"\u001b[39m: include_domains,\n\u001b[1;32m    476\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124minclude_reasoning\u001b[39m\u001b[38;5;124m\"\u001b[39m: include_reasoning,\n\u001b[1;32m    477\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlogit_bias\u001b[39m\u001b[38;5;124m\"\u001b[39m: logit_bias,\n\u001b[1;32m    478\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlogprobs\u001b[39m\u001b[38;5;124m\"\u001b[39m: logprobs,\n\u001b[1;32m    479\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmax_completion_tokens\u001b[39m\u001b[38;5;124m\"\u001b[39m: max_completion_tokens,\n\u001b[1;32m    480\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmax_tokens\u001b[39m\u001b[38;5;124m\"\u001b[39m: max_tokens,\n\u001b[1;32m    481\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: metadata,\n\u001b[1;32m    482\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mn\u001b[39m\u001b[38;5;124m\"\u001b[39m: n,\n\u001b[1;32m    483\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mparallel_tool_calls\u001b[39m\u001b[38;5;124m\"\u001b[39m: parallel_tool_calls,\n\u001b[1;32m    484\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpresence_penalty\u001b[39m\u001b[38;5;124m\"\u001b[39m: presence_penalty,\n\u001b[1;32m    485\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mreasoning_effort\u001b[39m\u001b[38;5;124m\"\u001b[39m: reasoning_effort,\n\u001b[1;32m    486\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mreasoning_format\u001b[39m\u001b[38;5;124m\"\u001b[39m: reasoning_format,\n\u001b[1;32m    487\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mresponse_format\u001b[39m\u001b[38;5;124m\"\u001b[39m: response_format,\n\u001b[1;32m    488\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msearch_settings\u001b[39m\u001b[38;5;124m\"\u001b[39m: search_settings,\n\u001b[1;32m    489\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mseed\u001b[39m\u001b[38;5;124m\"\u001b[39m: seed,\n\u001b[1;32m    490\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mservice_tier\u001b[39m\u001b[38;5;124m\"\u001b[39m: service_tier,\n\u001b[1;32m    491\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstop\u001b[39m\u001b[38;5;124m\"\u001b[39m: stop,\n\u001b[1;32m    492\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstore\u001b[39m\u001b[38;5;124m\"\u001b[39m: store,\n\u001b[1;32m    493\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstream\u001b[39m\u001b[38;5;124m\"\u001b[39m: stream,\n\u001b[1;32m    494\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtemperature\u001b[39m\u001b[38;5;124m\"\u001b[39m: temperature,\n\u001b[1;32m    495\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtool_choice\u001b[39m\u001b[38;5;124m\"\u001b[39m: tool_choice,\n\u001b[1;32m    496\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtools\u001b[39m\u001b[38;5;124m\"\u001b[39m: tools,\n\u001b[1;32m    497\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtop_logprobs\u001b[39m\u001b[38;5;124m\"\u001b[39m: top_logprobs,\n\u001b[1;32m    498\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtop_p\u001b[39m\u001b[38;5;124m\"\u001b[39m: top_p,\n\u001b[1;32m    499\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124muser\u001b[39m\u001b[38;5;124m\"\u001b[39m: user,\n\u001b[1;32m    500\u001b[0m             },\n\u001b[1;32m    501\u001b[0m             completion_create_params\u001b[38;5;241m.\u001b[39mCompletionCreateParams,\n\u001b[1;32m    502\u001b[0m         ),\n\u001b[1;32m    503\u001b[0m         options\u001b[38;5;241m=\u001b[39mmake_request_options(\n\u001b[1;32m    504\u001b[0m             extra_headers\u001b[38;5;241m=\u001b[39mextra_headers, extra_query\u001b[38;5;241m=\u001b[39mextra_query, extra_body\u001b[38;5;241m=\u001b[39mextra_body, timeout\u001b[38;5;241m=\u001b[39mtimeout\n\u001b[1;32m    505\u001b[0m         ),\n\u001b[1;32m    506\u001b[0m         cast_to\u001b[38;5;241m=\u001b[39mChatCompletion,\n\u001b[1;32m    507\u001b[0m         stream\u001b[38;5;241m=\u001b[39mstream \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m,\n\u001b[1;32m    508\u001b[0m         stream_cls\u001b[38;5;241m=\u001b[39mStream[ChatCompletionChunk],\n\u001b[1;32m    509\u001b[0m     )\n",
      "File \u001b[0;32m/opt/anaconda3/lib/python3.12/site-packages/groq/_base_client.py:1284\u001b[0m, in \u001b[0;36mSyncAPIClient.post\u001b[0;34m(self, path, cast_to, body, content, options, files, stream, stream_cls)\u001b[0m\n\u001b[1;32m   1275\u001b[0m     warnings\u001b[38;5;241m.\u001b[39mwarn(\n\u001b[1;32m   1276\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPassing raw bytes as `body` is deprecated and will be removed in a future version. \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m   1277\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPlease pass raw bytes via the `content` parameter instead.\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m   1278\u001b[0m         \u001b[38;5;167;01mDeprecationWarning\u001b[39;00m,\n\u001b[1;32m   1279\u001b[0m         stacklevel\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m2\u001b[39m,\n\u001b[1;32m   1280\u001b[0m     )\n\u001b[1;32m   1281\u001b[0m opts \u001b[38;5;241m=\u001b[39m FinalRequestOptions\u001b[38;5;241m.\u001b[39mconstruct(\n\u001b[1;32m   1282\u001b[0m     method\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpost\u001b[39m\u001b[38;5;124m\"\u001b[39m, url\u001b[38;5;241m=\u001b[39mpath, json_data\u001b[38;5;241m=\u001b[39mbody, content\u001b[38;5;241m=\u001b[39mcontent, files\u001b[38;5;241m=\u001b[39mto_httpx_files(files), \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39moptions\n\u001b[1;32m   1283\u001b[0m )\n\u001b[0;32m-> 1284\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m cast(ResponseT, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mrequest(cast_to, opts, stream\u001b[38;5;241m=\u001b[39mstream, stream_cls\u001b[38;5;241m=\u001b[39mstream_cls))\n",
      "File \u001b[0;32m/opt/anaconda3/lib/python3.12/site-packages/groq/_base_client.py:1071\u001b[0m, in \u001b[0;36mSyncAPIClient.request\u001b[0;34m(self, cast_to, options, stream, stream_cls)\u001b[0m\n\u001b[1;32m   1068\u001b[0m             err\u001b[38;5;241m.\u001b[39mresponse\u001b[38;5;241m.\u001b[39mread()\n\u001b[1;32m   1070\u001b[0m         log\u001b[38;5;241m.\u001b[39mdebug(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRe-raising status error\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m-> 1071\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_status_error_from_response(err\u001b[38;5;241m.\u001b[39mresponse) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m   1073\u001b[0m     \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[1;32m   1075\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m response \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcould not resolve response (should never happen)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "\u001b[0;31mAuthenticationError\u001b[0m: Error code: 401 - {'error': {'message': 'Invalid API Key', 'type': 'invalid_request_error', 'code': 'invalid_api_key'}}"
     ]
    }
   ],
   "source": [
    "from groq import Groq\n",
    "import time\n",
    "\n",
    "client = Groq(\n",
    "    api_key=\"YOUR_API_KEY\"\n",
    ")\n",
    "\n",
    "tokens = []\n",
    "\n",
    "start_time = time.time()\n",
    "\n",
    "stream = client.chat.completions.create(\n",
    "    model=\"llama-3.1-8b-instant\",\n",
    "    messages=[\n",
    "        {\n",
    "            \"role\": \"user\",\n",
    "            \"content\": \"Write a short poem about the moon.\"\n",
    "        }\n",
    "    ],\n",
    "    temperature=0.7,\n",
    "    stream=True\n",
    ")\n",
    "\n",
    "print(\"Generated Poem:\\n\")\n",
    "\n",
    "for chunk in stream:\n",
    "\n",
    "    token = chunk.choices[0].delta.content\n",
    "\n",
    "    if token:\n",
    "\n",
    "        tokens.append(token)\n",
    "\n",
    "        print(token, end=\"\", flush=True)\n",
    "\n",
    "end_time = time.time()\n",
    "\n",
    "total_time = end_time - start_time\n",
    "\n",
    "full_text = \"\".join(tokens)\n",
    "\n",
    "token_count = len(tokens)\n",
    "\n",
    "tokens_per_second = token_count / total_time\n",
    "\n",
    "print(\"\\n\")\n",
    "print(\"=\" * 60)\n",
    "\n",
    "print(\"Total Tokens:\", token_count)\n",
    "print(f\"Generation Time: {total_time:.2f} seconds\")\n",
    "print(f\"Tokens Per Second: {tokens_per_second:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d60f933-7fae-4c24-987e-fe211a69d384",
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
