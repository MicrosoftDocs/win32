---
title: Top Property (Characters Object)
description: Top Property
ms.assetid: d5758a77-2d9a-44b8-bbbb-57ddf96c7fe4
ms.topic: article
ms.date: 05/31/2018
---

# Top Property (Characters Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the top edge of the specified character's frame.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Top** \[ = *value*\]



| Part    | Description                                             |
|---------|---------------------------------------------------------|
| *value* | A Long integer that specifies the character's top edge. |



 

</dd> </dl>

## Remarks

The **Top** property is always expressed in pixels, relative to screen origin (upper left). This property's setting applies to all clients of the character.

Even though the character appears in an irregularly shaped region window, the location of the character is based on the external dimensions of the rectangular animation frame used when the character was compiled with the Microsoft Agent Character Editor.

Use the [**MoveTo**](moveto-method.md) method to change the character's location.

## See Also

[**Left property**](left-property.md), [**MoveTo method**](moveto-method.md)


 

 




