---
title: IAgentCharacter GetTTSPitch
description: IAgentCharacter GetTTSPitch
ms.assetid: b21ae1f1-daf6-42e5-9c52-f28722180021
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetTTSPitch

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetTTSPitch(
   long * pdwPitch  // address of variable for character TTS pitch
);
```

Retrieves the character's TTS output pitch setting.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwPitch"></span><span id="pdwpitch"></span><span id="PDWPITCH"></span>*pdwPitch*
</dt> <dd>

Address of a variable that receives the character's current TTS pitch setting in Hertz.

</dd> </dl>

Although your application cannot write this value, you can include pitch tags in your output text that will temporarily increase the pitch for a particular utterance. This method applies only to characters configured for TTS output. If the speech synthesis (TTS) engine is not enabled (or installed) or the character does not support TTS output, this method returns zero (0).

 

 




