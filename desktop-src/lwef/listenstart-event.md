---
title: ListenStart Event
description: ListenStart Event
ms.assetid: 59feacd6-0b9f-4bf4-b544-48de49384312
ms.topic: article
ms.date: 05/31/2018
---

# ListenStart Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when Listening mode (speech recognition) begins.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent.***ListenStart (ByVal** *CharacterID***)**



| Part          | Description                                            |
|---------------|--------------------------------------------------------|
| *CharacterID* | Returns the ID of the listening character as a string. |



 

</dd> </dl>

### Remarks

This event is sent to all clients when Listening mode begins because the user pressed the Listening key or the input-active client called the [**Listen**](listen-method.md) method with **True**. You can use this event to avoid having your character speak while the Listening mode is on.

If you turn on Listening mode with the [**Listen**](listen-method.md) method and then the user presses the Listening key, the Listening mode resets and continues until the Listening key time-out completes, the Listening key is released, or the user finishes speaking, whichever is later. In this situation, when Listening mode is already on, you will not get an additional **ListenStart** event when the user presses the Listening key.

The event returns the character to the clients that currently have this character loaded. All other clients receive a null character (empty string).

### See Also

[**ListenComplete event**](listencomplete-event.md), [**Listen method**](listen-method.md)


 

 




