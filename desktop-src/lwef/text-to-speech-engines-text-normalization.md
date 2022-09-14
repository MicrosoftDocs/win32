---
title: Text-to-Speech Engines Text Normalization
description: Text-to-Speech Engines Text Normalization
ms.assetid: 1974d47b-4877-47e3-89d8-fd70967e7605
ms.topic: article
ms.date: 05/31/2018
---

# Text-to-Speech Engines Text Normalization

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Normalization is the process of identifying numbers, abbreviations, acronyms and idiomatics and transforming them into full text as needed, usually based on the context of the sentence.

For example, using the L&H TruVoice American English TTS Engine, the sentence:

King George VI of England died on Feb 6, 1952.

will be read under **normal context** as:

   King George V I of England, died on February six, nineteen fifty-two.

But under **E-mail context**, it will be read as:

   King George the sixth of England, died on February sixth, nineteen fifty-two.

Information about using the **Context** speech tag can be found in the Agent programming documentation [Microsoft Agent Speech Output Tags](microsoft-agent-speech-output-tags.md).

 

 




