---
title: Move Event
description: Move Event
ms.assetid: 973e9e68-edbb-4741-b50e-57db96712df8
ms.topic: article
ms.date: 05/31/2018
---

# Move Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a character is moved.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent*\_**Move (ByVal** *CharacterID*, **ByVal** *X*, **ByVal** *Y*, **ByVal** *Cause***)**



| Part          | Description                                                                                                                                                                                                                                                                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the character that moved.                                                                                                                                                                                                                                                                                                   |
| *X*           | Returns the x-coordinate (in pixels) of the top edge of character frame's new location as an integer.                                                                                                                                                                                                                                         |
| *Y*           | Returns the y-coordinate (in pixels) of the left edge of character frame's new location as an integer.                                                                                                                                                                                                                                        |
| *Cause*       | Returns a value that indicates what caused the character to move. 1 The user dragged the character.<br/> 2 Your client application moved the character.<br/> 3 Another client application moved the character.<br/> 4 The Agent server moved the character to keep it onscreen after a screen resolution change.<br/> |



 

</dd> </dl>

### Remarks

This event occurs when the user or an application changes the character's position. Coordinates are relevant to the upper left corner of the screen. This event is sent only to the clients of the character (applications that have loaded the character).

**See Also**

[**MoveCause property**](movecause-property.md), [**Size event**](size-event.md)

 

 





