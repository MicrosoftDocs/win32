---
title: DefaultCharacterChange Event
description: DefaultCharacterChange Event
ms.assetid: 14b86a44-8fd2-4719-b7b5-cdcc618d27cd
ms.topic: article
ms.date: 05/31/2018
---

# DefaultCharacterChange Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when the user changes the default character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent.***DefaultCharacterChange** **(ByVal** *GUID***)**



| Part   | Description                                      |
|--------|--------------------------------------------------|
| *GUID* | Returns the unique identifier for the character. |



 

</dd> </dl>

### Remarks

This event indicates when the user has changed the character assigned as the user's default character. The server sends this only to clients that have loaded the default character.

When the new character appears, it assumes the same size as any already loaded instance of the character or the previous default character (in that order).

### See Also

[**ShowDefaultCharacterProperties method**](showdefaultcharacterproperties-method.md), [**Load method**](load-method.md)


 

 




