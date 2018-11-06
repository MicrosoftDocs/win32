---
title: Show Event
description: Show Event
ms.assetid: 'vs|msagent|~\pacontrol_7wrw.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Show Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a character is displayed.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent***\_Show (ByVal** *CharacterID*, **ByVal** *Cause***)**



| Part          | Description                                                                                                                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the character shown as a string.                                                                                                                                                                                                                          |
| *Cause*       | Returns a value that indicates what caused the character to display. 2 The user showed the character (using the menu or voice command).<br/> 4 Your client application showed the character.<br/> 6 Another client application showed the character.<br/> |



 

</dd> </dl>

### Remarks

The server sends this event to all clients of the character. To query the current state of the character, use the [**Visible**](visible-property.md) property.

### See Also

[**Hide event**](hide-event.md), [**VisibilityCause**](visibilitycause-property.md)


 

 





