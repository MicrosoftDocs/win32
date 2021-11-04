---
title: IAgentAudioOutputPropertiesEx GetStatus
description: IAgentAudioOutputPropertiesEx GetStatus
ms.assetid: 29bf1379-eebe-4b8b-b8d0-b86d2da78b64
ms.topic: article
ms.date: 05/31/2018
---

# IAgentAudioOutputPropertiesEx::GetStatus

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetStatus(
   long * plStatus,  // address of audio channel status
);
```

Retrieves the status of the audio channel.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plStatus"></span><span id="plstatus"></span><span id="PLSTATUS"></span>*plStatus*
</dt> <dd>

Status of the audio output channel, which may be one of the following values:



| Value                                                                         | Description                                                                                                    |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **const unsigned short** **AUDIO\_STATUS\_AVAILABLE = 0;**<br/>         | The audio output channel is available (not busy).                                                              |
| **const unsigned short** **AUDIO\_STATUS\_NOAUDIO = 1;**<br/>           | There is no support for audio output; for example, because there is no sound card.                             |
| **const unsigned short** **AUDIO\_STATUS\_CANTOPENAUDIO = 2;**<br/>     | The audio output channel can't be opened (is busy); for example, because another application is playing audio. |
| **const unsigned short** **AUDIO\_STATUS\_USERSPEAKING = 3;**<br/>      | The audio output channel is busy because the server is processing user speech input                            |
| **const unsigned short** **AUDIO\_STATUS\_CHARACTERSPEAKING = 4;**<br/> | The audio output channel is busy because a character is currently speaking.                                    |
| **const unsigned short** **AUDIO\_STATUS\_SROVERRIDEABLE = 5;**<br/>    | The audio output channel is not busy, but it is waiting for user speech input.                                 |
| **const unsigned short** **AUDIO\_STATUS\_ERROR = 6;**<br/>             | There was some other (unknown) problem in attempting to access the audio output channel.                       |



 

</dd> </dl>

This setting enables your client application to query the state of the audio output channel. You can use this to determine whether to have your character speak or to try to turn on Listening mode (using **IAgentCharacterEx::Listen**).

 

 





