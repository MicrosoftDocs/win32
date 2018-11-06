---
title: Size Event
description: Size Event
ms.assetid: 06089f84-8e75-475f-a492-536c83fa6730
ms.topic: article
ms.date: 05/31/2018
---

# Size Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a character's size changes.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent*\_**Size (ByVal** *CharacterID*, **ByVal** *Width*, **ByVal** *Height*)



| Part          | Description                                                         |
|---------------|---------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the character that moved.                         |
| *Width*       | Returns the character frame's new width (in pixels) as an integer.  |
| *Height*      | Returns the character frame's new height (in pixels) as an integer. |



 

</dd> </dl>

### Remarks

This event occurs when an application changes the size of a character. This event is sent only to the clients of the character (applications that have loaded the character).

### See Also

[**Move event**](move-event.md)


 

 




