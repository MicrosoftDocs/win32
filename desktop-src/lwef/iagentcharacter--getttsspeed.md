---
title: IAgentCharacter GetTTSSpeed
description: IAgentCharacter GetTTSSpeed
ms.assetid: 25526ef7-581f-489c-a299-bd3b5ac9ea61
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetTTSSpeed

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetTTSSpeed(
   long * pdwSpeed  // address of variable for character TTS output speed
);
```

Retrieves the character's TTS output speed setting.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwSpeed"></span><span id="pdwspeed"></span><span id="PDWSPEED"></span>*pdwSpeed*
</dt> <dd>

Address of a variable that receives the output speed of the character in words per minute.

</dd> </dl>

Although your application cannot write this value, you can include speed tags in your output text that will temporarily speed up the output for a particular utterance.

This property returns the current speaking output speed setting for the character. For characters using TTS output, the property returns the actual TTS output for the character. If TTS is not enabled or the character does not support TTS output, the setting reflects the user setting for output speed.

 

 




