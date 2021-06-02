---
description: The TextStyle table lists different font styles used in controls having text.
ms.assetid: a351e67a-8f51-41bf-9202-56488b870fa7
title: TextStyle Table
ms.topic: article
ms.date: 05/31/2018
---

# TextStyle Table

The TextStyle table lists different font styles used in controls having text.

The TextStyle table has the following columns.



| Column    | Type                               | Key | Nullable |
|-----------|------------------------------------|-----|----------|
| TextStyle | [Identifier](identifier.md)       | Y   | N        |
| FaceName  | [Text](text.md)                   | N   | N        |
| Size      | [Integer](integer.md)             | N   | N        |
| Color     | [DoubleInteger](doubleinteger.md) | N   | Y        |
| StyleBits | [Integer](integer.md)             | N   | Y        |



 

## Columns

<dl> <dt>

<span id="TextStyle"></span><span id="textstyle"></span><span id="TEXTSTYLE"></span>TextStyle
</dt> <dd>

This column is the name of the font style. This name can be embedded in the text string to indicate a style change. Note that the font style name used in this field must not end with the characters: \_UL. See [Adding Controls and Text](adding-controls-and-text.md).

</dd> <dt>

<span id="FaceName"></span><span id="facename"></span><span id="FACENAME"></span>FaceName
</dt> <dd>

A string indicating the name of the font. The string must be no more than 31 characters long.

</dd> <dt>

<span id="Size"></span><span id="size"></span><span id="SIZE"></span>Size
</dt> <dd>

The font size measured in points. This must be a non-negative number.

</dd> <dt>

<span id="Color"></span><span id="color"></span><span id="COLOR"></span>Color
</dt> <dd>

This column specifies the text color displayed by a [Text Control](text-control.md). All other types of controls always use the default text color. The value put in this column should be computed using the following formula: 65536 \* blue + 256 \* green + red, where red, green, and blue are each in the range of 0-255. The value must not exceed 16777215, which is the value for white. The value is 0 for black, 255 for red, 65280 for green, 16711680 for blue and 8421504 for grey. Leaving the field empty specifies the default color.

Do not place transparent [Text controls](text-control.md) on top of colored bitmaps. The text may not be visible if the user changes the display color scheme. For example, text may become invisible if the user sets the high contrast parameter for accessibility.

</dd> <dt>

<span id="StyleBits"></span><span id="stylebits"></span><span id="STYLEBITS"></span>StyleBits
</dt> <dd>

A combination of bits indicating the formatting for the text.

The individual style bits have the following values.



| Constant                             | Hexadecimal | Decimal | Style      |
|--------------------------------------|-------------|---------|------------|
| **msidbTextStyleStyleBitsBold**      | 0x001       | 1       | Bold       |
| **msidbTextStyleStyleBitsItalic**    | 0x002       | 2       | Italic     |
| **msidbTextStyleStyleBitsUnderline** | 0x004       | 4       | Underline  |
| **msidbTextStyleStyleBitsStrike**    | 0x008       | 8       | Strike out |



 

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE31](ice31.md)  
[ICE45](ice45.md)  
</dl>

 

 



