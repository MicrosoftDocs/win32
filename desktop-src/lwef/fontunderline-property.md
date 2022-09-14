---
title: FontUnderline Property
description: FontUnderline Property
ms.assetid: 6fe6c147-2969-470e-9742-da2e6b3614e1
ms.topic: article
ms.date: 05/31/2018
---

# FontUnderline Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns the font style currently displayed in the word balloon window for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Balloon.FontUnderline**



| Value     | Description                         |
|-----------|-------------------------------------|
| **True**  | The balloon font is underlined.     |
| **False** | The balloon font is not underlined. |



 

</dd> </dl>

## Remarks

The default value for the font settings of a character's word balloon are set in the Microsoft Agent Character Editor. In addition, the user can override font settings for all characters in the Microsoft Agent property sheet.

 

 




