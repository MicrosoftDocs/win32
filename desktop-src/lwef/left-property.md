---
title: Left Property (Characters Object)
description: Left Property
ms.assetid: f496f075-6430-4806-a237-1c7b626d355e
ms.topic: article
ms.date: 05/31/2018
---

# Left Property (Characters Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the left edge of the specified character's frame.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Left** \[ = *value*\]



| Part    | Description                                                           |
|---------|-----------------------------------------------------------------------|
| *value* | A Long integer that specifies the left edge of the character's frame. |



 

</dd> </dl>

## Remarks

The **Left** property is always expressed in pixels, relative to screen origin (upper left). This property's setting applies to all clients of the character.

Even though the character appears in an irregularly shaped region window, the location of the character is based on the external dimensions of the rectangular animation frame used when the character was compiled with the Microsoft Agent Character Editor.

 

 




