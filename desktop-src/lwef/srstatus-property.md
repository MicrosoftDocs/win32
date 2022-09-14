---
title: SRStatus Property
description: SRStatus Property
ms.assetid: 67618a35-05e4-4bb3-b910-c75de6e32578
ms.topic: article
ms.date: 05/31/2018
---

# SRStatus Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns whether speech input can be started for the character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").SRStatus**



| Value | Description                                                                                                                                                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | Conditions support speech input.                                                                                                                                                                                                          |
| 1     | There is no audio input device available on this system. (Note that this does not detect whether a microphone is installed; it can only detect whether the user has a properly installed input-enabled sound card with a working driver.) |
| 2     | Another client is the active client of this character, or the current character is not topmost.                                                                                                                                           |
| 3     | The audio input or output channel is currently busy, an application is using audio.                                                                                                                                                       |
| 4     | An unspecified error occurred in the process of initializing the speech recognition subsystem. This includes the possibility that there is no speech engine available matching the character's language setting.                          |
| 5     | The user has disabled speech input in the Advanced Character Options.                                                                                                                                                                     |
| 6     | An error occurred in checking the audio status, but the cause of the error was not returned by the system.                                                                                                                                |



 

</dd> </dl>

## Remarks

This property returns the conditions necessary to support speech input, including the status of the audio device. You can check this property before you call the [**Listen**](listen-method.md) method to better ensure its success.

When speech input is enabled in the Agent property sheet (Advanced Character Options), querying this property will load the associated engine, if it is not already loaded, and start speech services. That is, the Listening key is available, and the Listening Tip is automatically displayable. (The Listening key and Listening Tip are only enabled if they are also enabled in Advanced Character Options.) However, if you query the property when speech is disabled, the server does not start speech services.

This property only applies to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**Listen method**](listen-method.md)


 

 




