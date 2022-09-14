---
title: IdleStart Event
description: IdleStart Event
ms.assetid: 3d97c26b-b88a-42e3-9072-0bc65510efc2
ms.topic: article
ms.date: 05/31/2018
---

# IdleStart Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when the server sets a character to the **Idling** state.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent***\_IdleStart** **(ByVal** *CharacterID***)**



| Part          | Description                                         |
|---------------|-----------------------------------------------------|
| *CharacterID* | Returns the ID of the idling character as a string. |



 

</dd> </dl>

### Remarks

The server sends this event to all clients of the character.

### See Also

[**IdleComplete event**](idlecomplete-event.md)


 

 




