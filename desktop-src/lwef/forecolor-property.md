---
title: ForeColor Property
description: ForeColor Property
ms.assetid: b5cef81b-55e1-49a5-bdbf-f7101520a13a
ms.topic: article
ms.date: 05/31/2018
---

# ForeColor Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns the foreground color currently displayed in the word balloon window for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Balloon.ForeColor**

</dd> </dl>

## Remarks

The **ForeColor** property returns a value that specifies the color of text in the word balloon. The valid range for a normal RGB color is 0 to 16,777,215 (&HFFFFFF). The high byte of a number in this range equals 0; the lower 3 bytes, from least to most significant byte, determine the amount of red, green, and blue, respectively. The red, green, and blue components are each represented by a number between 0 and 255 (&HFF).

 

 




