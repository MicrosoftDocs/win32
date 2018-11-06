---
title: IAgentCharacterEx GetSRStatus
description: IAgentCharacterEx GetSRStatus
ms.assetid: ccb34108-8078-421a-a883-731b51fae179
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetSRStatus

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetSRStatus(
   long * plStatus  // address of the speech input status
);
```

Retrieves the status of the condition necessary to support speech input.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plStatus"></span><span id="plstatus"></span><span id="PLSTATUS"></span>*plStatus*
</dt> <dd>

Address of a variable that receives one of the following values for the state setting:



| Value                                                                               | Description                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **const unsigned long** **LISTEN\_STATUS\_CANLISTEN = 0;**<br/>               | Conditions support speech input.                                                                                                                                                                                                          |
| **const unsigned long** **LISTEN\_STATUS\_NOAUDIO = 1;**<br/>                 | There is no audio input device available on this system. (Note that this does not detect whether a microphone is installed; it can only detect whether the user has a properly installed input-enabled sound card with a working driver.) |
| **const unsigned long** **LISTEN\_STATUS\_NOTTOPMOST = 2;**<br/>              | Another client is the active client of this character, or the current character is not topmost.                                                                                                                                           |
| **const unsigned long** **LISTEN\_STATUS\_CANTOPENAUDIO = 3;**<br/>           | The audio input or output channel is currently busy, some other application is using audio.                                                                                                                                               |
| **const unsigned long** **LISTEN\_STATUS\_COULDNTINITIALIZESPEECH = 4;**<br/> | An unspecified error occurred in the process of initializing the speech recognition subsystem. This includes the possibility that there is no speech engine available matching the character's language setting.                          |
| **const unsigned long** **LISTEN\_STATUS\_SPEECHDISABLED = 5;**<br/>          | The user has disabled speech input in the Advanced Character Options window.                                                                                                                                                              |
| **const unsigned long** **LISTEN\_STATUS\_ERROR = 6;**<br/>                   | An error occurred in checking the audio status, but the cause of the error was not returned by the system.                                                                                                                                |



 

</dd> </dl>

This function enables you to query whether current conditions support speech recognition input, including the status of the audio device. If your application uses the [**IAgentCharacterEx::Listen**](iagentcharacterex--listen.md) method, you can use this function to better ensure that the call will succeed. Calling this method also loads the speech engine if it is not already loaded. However, it does not turn on Listening mode.

When speech input is enabled in the Agent property sheet (Advanced Character Options), querying the status will load the associated engine (if it is not already loaded), and start speech services. That is, the Listening key is available, and the Listening Tip is displayable. (The Listening key and Listening Tip are enabled only if they are also enabled in Advanced Character Options.) However, if you query the property when speech is disabled, the server does not start speech services.

This function returns only the setting for your client application's use of the character; the setting does not reflect other clients of the character or other characters of your client application.

 

 





