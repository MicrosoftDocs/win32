---
title: BalloonHide Event
description: BalloonHide Event
ms.assetid: dd1f3e83-f3d9-496e-9a54-b3a23b2403da
ms.topic: article
ms.date: 05/31/2018
---

# BalloonHide Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a character's word balloon is hidden.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent*\_**BalloonHide** **(ByVal** *CharacterID***)**



| Part          | Description                                                       |
|---------------|-------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the character associated with the word balloon. |



 

</dd> </dl>

### Remarks

The server sends this event only to the clients of the character (applications that have loaded the character) that uses the word balloon.

### See Also

[**BalloonShow event**](balloonshow-event.md)


 

 




