---
title: BalloonShow Event
description: BalloonShow Event
ms.assetid: 8a73e883-c003-480b-8a0a-e699caffe54c
ms.topic: article
ms.date: 05/31/2018
---

# BalloonShow Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a character's word balloon is shown.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent*\_**BalloonShow** **(ByVal** *CharacterID***)**



| Part          | Description                                                       |
|---------------|-------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the character associated with the word balloon. |



 

</dd> </dl>

### Remarks

The server sends this event only to the clients of the character (applications that have loaded the character) that uses the word balloon.

### See Also

[**BalloonHide event**](balloonhide-event.md)


 

 




