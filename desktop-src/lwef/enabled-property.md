---
title: Enabled Property (Balloon Object)
description: Learn about the Enabled Balloon object property. Microsoft Agent is deprecated as of Windows 7.
ms.assetid: 4d73acda-6fcc-4912-a466-570849aeb807
ms.topic: article
ms.date: 05/31/2018
---

# Enabled Property (Balloon Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns whether the word balloon is enabled for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Balloon.Enabled**



| Value     | Description              |
|-----------|--------------------------|
| **True**  | The balloon is enabled.  |
| **False** | The balloon is disabled. |



 

</dd> </dl>

## Remarks

The **Enabled** property returns a Boolean value specifying whether the balloon is enabled. The word balloon default state is set as part of a character's definition when the character is compiled in the Microsoft Agent Character Editor. If a character is defined to not support the word balloon, this property will always be **False** for the character.

 

 




