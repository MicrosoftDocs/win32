---
title: Width Property (Characters Object)
description: Learn about the Width Property of the Characters object, which returns or sets the width of the frame for the specified character.
ms.assetid: ebada4cc-dbe6-4540-be1f-1f61e176765b
ms.topic: article
ms.date: 05/31/2018
---

# Width Property (Characters Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the width of the frame for the specified character.

</dd> <dt>

<span id="Syntax_"></span><span id="syntax_"></span><span id="SYNTAX_"></span>**Syntax** 
</dt> <dd>

*agent***.Characters ("***CharacterID***").Width** \[= *value*\]



| Part    | Description                                                |
|---------|------------------------------------------------------------|
| *value* | A Long integer that specifies the character's frame width. |



 

</dd> </dl>

## Remarks

The [**Width**](width-property.md) property is always expressed in pixels. This property's setting applies to all clients of the character.

Even though the character appears in an irregularly shaped region window, the location of the character is based on the external dimensions of the rectangular animation frame used when the character was compiled with the Microsoft Agent Character Editor.

 

 




