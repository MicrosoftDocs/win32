---
title: Hide Event
description: Hide Event
ms.assetid: 'vs|msagent|~\pacontrol_9yuk.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Hide Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a character is hidden.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent***\_Hide(** **ByVal** *CharacterID*, **ByVal** *Cause***)**



| Part          | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the hidden character as a string.                                                                                                                                                                                                                                                                                                                                                               |
| *Cause*       | Returns a value that indicates what caused the character to hide. 1 User hid the character by selecting the command on the character's taskbar icon pop-up menu or using speech input.<br/> 3 Your client application hid the character.<br/> 5 Another client application hid the character.<br/> 7 User hid the character by selecting the command on the character's pop-up menu.<br/> |



 

</dd> </dl>

### Remarks

The server sends this event to all clients of the character. To query the current state of the character, use the [**Visible**](visible-property.md) property.

### See Also

[**Show event**](show-event.md), [**VisibilityCause**](visibilitycause-property.md)


 

 





