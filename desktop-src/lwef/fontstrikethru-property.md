---
title: FontStrikeThru Property
description: FontStrikeThru Property
ms.assetid: 2d87fded-2f3e-44cd-b2a5-5f9c76ca1cf5
ms.topic: article
ms.date: 05/31/2018
---

# FontStrikeThru Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns the font style currently displayed in the word balloon window for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Balloon.FontStrikeThru**



| Value     | Description                                             |
|-----------|---------------------------------------------------------|
| **True**  | The balloon font uses the strikethrough effect.         |
| **False** | The balloon font does not use the strikethrough effect. |



 

</dd> </dl>

## Remarks

The default value for the font settings of a character's word balloon are set in the Microsoft Agent Character Editor. In addition, the user can override font settings for all characters in the Microsoft Agent property sheet.

 

 




