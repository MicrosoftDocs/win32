---
title: ListenComplete Event
description: ListenComplete Event
ms.assetid: 29e3f424-17b4-4287-b644-ed62b80e0035
ms.topic: article
ms.date: 05/31/2018
---

# ListenComplete Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when Listening mode (speech recognition) has ended.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent.***ListenComplete (ByVal** *CharacterID*, **ByVal** *Cause***)**



| Part          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the listening character as a string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Cause*       | Returns the cause of the complete event as an integer that may be one of the following: 1 Listening mode was turned off by program code.<br/> 2 Listening mode (turned on by program code) timed out.<br/> 3 Listening mode (turned on by the Listening key) timed out.<br/> 4 Listening mode was turned off because the user released the Listening key.<br/> 5 Listening mode ended because the user finished speaking.<br/> 6 Listening mode ended because the input-active client was deactivated.<br/> 7 Listening mode ended because the default character was changed.<br/> 8 Listening mode ended because the user disabled speech input.<br/> |



 

</dd> </dl>

### Remarks

This event is sent to all clients when the Listening mode time-out ends, after the user releases the Listening key, when the input active client calls the [**Listen**](listen-method.md) method with **False**, or the user finished speaking. You can use this event to determine when to resume character spoken (audio) output.

If you turn on Listening mode using the [**Listen**](listen-method.md) method and then the user presses the Listening key, the Listening mode resets and continues until the Listening key time-out completes, the Listening key is released, or the user finishes speaking, whichever is later. In this situation, you will not receive a **ListenComplete** event until the listening key's mode completes.

The event returns the character to the clients that currently have this character loaded. All other clients receive a null character (empty string).

### See Also

[**ListenStart event**](listenstart-event.md), [**Listen method**](listen-method.md)


 

 





