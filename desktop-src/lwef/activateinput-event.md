---
title: ActivateInput Event
description: ActivateInput Event
ms.assetid: bc395750-5da0-4379-8eca-3195e936052c
ms.topic: article
ms.date: 05/31/2018
---

# ActivateInput Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a client becomes input-active.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent*\_ActivateInput**(ByVal** *CharacterID***)**



| Part          | Description                                                                    |
|---------------|--------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the character through which the client becomes input-active. |



 

</dd> </dl>

### Remarks

The input-active client receives mouse and speech input events supplied by the server. The server sends this event only to the client that becomes input-active.

This event can occur when the user switches to your [Command](the-command-object.md) object, for example, by choosing your Command object entry in the Commands Window or in the pop-up menu for a character. It can also occur when the user selects a character (by clicking or speaking its name), when a character becomes visible, and when the character of another client application becomes hidden. You can also call the [Activate Method](activate-method.md) (with **State** set to 2) to explicitly make the character topmost, which results in your client application becoming input-active and triggers this event. However, this event does not occur if you use the Activate Method method only to specify whether your client is the active client of the character.

### See Also

[**DeactivateInput** event](deactivateinput-event.md), [**Activate** method](activate-method.md)


 

 




