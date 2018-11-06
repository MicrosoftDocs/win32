---
title: DeactivateInput Event
description: DeactivateInput Event
ms.assetid: 59747932-82be-45d5-8465-73798904e8a7
ms.topic: article
ms.date: 05/31/2018
---

# DeactivateInput Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a client becomes non-input-active.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent***\_DeactivateInput** **(ByVal** *CharacterID***)**



| Part          | Description                                                                    |
|---------------|--------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the character that makes the client become non-input-active. |



 

</dd> </dl>

### Remarks

A non-input-active client no longer receives mouse or speech events from the server (unless it becomes input-active again). The server sends this event only to the client that becomes non-input-active.

This event occurs when your client application is input-active and the user chooses the caption of another client in a character's pop-up menu or the Voice Commands Window or you call the [**Activate**](activate-method.md) method and set the **State** parameter to 0. It may also occur when the user selects the name of another character by clicking or speaking. You also get this event when your character is hidden or another character becomes visible.

### See Also

[**ActivateInput event**](activateinput-event.md)


 

 




