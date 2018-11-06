---
title: IdleComplete Event
description: IdleComplete Event
ms.assetid: 1d684f75-f23e-4ed8-a60a-5e6792332103
ms.topic: article
ms.date: 05/31/2018
---

# IdleComplete Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when the server ends the **Idling** state of a character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent***\_IdleComplete** **(ByVal** *CharacterID***)**



| Part          | Description                                         |
|---------------|-----------------------------------------------------|
| *CharacterID* | Returns the ID of the idling character as a string. |



 

</dd> </dl>

### Remarks

The server sends this event to all clients of the character.

### See Also

[**IdleStart event**](idlestart-event.md)


 

 




