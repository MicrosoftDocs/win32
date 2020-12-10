---
title: Height Property (Characters Object)
description: Height Property
ms.assetid: 2c8dc333-e3c1-4f25-833b-9a4262c75b9f
ms.topic: article
ms.date: 05/31/2018
---

# Height Property (Characters Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the height of the specified character's frame.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Height** \[= *value*\]



| Part    | Description                                                 |
|---------|-------------------------------------------------------------|
| *value* | A Long integer that specifies the character's frame height. |



 

</dd> </dl>

## Remarks

The **Height** property is always expressed in pixels, relative to screen coordinates (upper left). This property's setting applies to all clients of the character.

Even though the character appears in an irregularly shaped region window, the height of the character is based on the external dimensions of the rectangular animation frame used when the character was compiled with the Microsoft Agent Character Editor.

 

 




