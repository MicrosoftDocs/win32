---
title: Status Property
description: Status Property
ms.assetid: 'vs|msagent|~\pacontrol_8xd6.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Status Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns the status of the audio output channel.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.AudioOutput.Status**



| Value | Description                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------|
| 0     | The audio output channel is available (not busy).                                                                 |
| 1     | There is no support for audio output; for example, because there is no sound card.                                |
| 2     | The audio output channel can't be opened (is busy); for example, because some other application is playing audio. |
| 3     | The audio output channel is busy because the server is processing user speech input.                              |
| 4     | The audio output channel is busy because a character is currently speaking.                                       |
| 5     | The audio output channel is not busy, but it is waiting for user speech input.                                    |
| 6     | There was some other (unknown) problem in attempting to access the audio output channel.                          |



 

</dd> </dl>

## Remarks

This setting enables your client application to query the audio output channel, returning an Integer value that indicates the status of the audio output channel. You can use this to determine whether it is appropriate to have your character speak or whether it is appropriate to try to turn on Listening mode (using the [**Listen**](listen-method.md) method).

## See Also

[**ListenComplete event**](listencomplete-event.md)


 

 




