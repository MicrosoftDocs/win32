---
title: FontSize Property (Balloon Object)
description: FontSize Property
ms.assetid: 36d5526a-1ae9-4ef2-94f6-0ad63ce86882
ms.topic: article
ms.date: 05/31/2018
---

# FontSize Property (Balloon Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the font size supported for the word balloon for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters** **("***CharacterID***").Balloon.FontSize** \[ = *Points*\]



| Part     | Description                                              |
|----------|----------------------------------------------------------|
| *Points* | A Long integer value specifying the font size in points. |



 

</dd> </dl>

## Remarks

The [**FontSize**](fontsize-property.md) property returns a Long integer value specifying the current font size in points. The maximum value for **FontSize** is 2160 points.

The default value for the font settings of a character's word balloon are set in the Microsoft Agent Character Editor. In addition, the user can override font settings for all characters in the Microsoft Agent property sheet.

 

 




