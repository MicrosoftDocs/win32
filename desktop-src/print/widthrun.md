---
Description: The WIDTHRUN structure is used to define the contents of Unidrv font metrics files (.ufm files).
ms.assetid: 18cc608e-b94d-4588-98e9-c22a7949a3b6
title: WIDTHRUN structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# WIDTHRUN structure

The WIDTHRUN structure is used to define the contents of [Unidrv font metrics files](print.customized_font_management#ddk-unidrv-font-metrics-files-gg) (.ufm files).

## Syntax


```C++
typedef struct _WIDTHRUN {
  WORD  wStartGlyph;
  WORD  wGlyphCount;
  DWORD loCharWidthOffset;
} WIDTHRUN, *PWIDTHRUN;
```



## Members

<dl> <dt>

**wStartGlyph**
</dt> <dd>

Is an index value indicating the first glyph of the width run.

</dd> <dt>

**wGlyphCount**
</dt> <dd>

Specifies the number of glyphs represented by the width run.

</dd> <dt>

**loCharWidthOffset**
</dt> <dd>

Specifies the offset from the beginning of a [**WIDTHTABLE**](widthtable.md) structure to the location containing the width of the set of glyphs contained in the width run.

</dd> </dl>

## Remarks

A width run describes the widths of a set of adjacent glyphs. Sets of width runs are described by an array of WIDTHRUN elements. The array is contained in a [**WIDTHTABLE**](widthtable.md) structure.

Index values contained in **dwStartGlyph** are integers, starting with 1, with each glyph in the font having an index. That is, the first glyph in the font is assigned an index value of 1, the next glyph's index is 2, and so on.

For example, suppose the first three elements of a WIDTHRUN array contain the following values:

<dl> WIDTHRUN\[0\]  
**wStartGlyph**=1  
**wGlyphCount**=3  
**IoCharWidthOffset**=*xxx*  
WIDTHRUN\[1\]  
**wStartGlyph**=4  
**wGlyphCount**=2  
**IoCharWidthOffset**=*yyy*  
WIDTHRUN\[2\]  
**wStartGlyph**=7  
**wGlyphCount**=4  
**IoCharWidthOffset**=*zzz*  
</dl>

At offset *xxx*: 56, 50, 60 (WORD-sized)

At offset *yyy*: 54, 60

At offset *zzz*: 54, 60, 43, 40

In this example, widths for the first three glyphs of the font are contained in an array at location WIDTHTABLE+*xxx*, the widths for the next two glyphs are contained in an array at location WIDTHTABLE+*yyy*, and widths for the next four glyphs are contained in an array at location WIDTHTABLE+*zzz*.

If a device font is proportional and has variable pitch characters, the WIDTHTABLE structure's **WidthRun** array contains only one WIDTHRUN element, and WIDTHTABLE+**loCharWidthOffset** points to a character width array for all characters in the font.

For Western device fonts, the **fwdAveCharWidth** member of the [**IFIMETRICS**](https://msdn.microsoft.com/fd2606ed-ec61-430a-aaad-38a4c3a207b6) structure is used for determining single-byte character widths, if the character widths are not specified using a WIDTHTABLE structure.

For East Asian device fonts, the **fwdAveCharWidth** and **fwdMaxCharInc** members of the IFIMETRICS structure are used for determining single-byte and double-byte character widths. If the font is proportional, the font's .ufm file should contain a WIDTHTABLE structure for the proportional glyphs.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**WIDTHTABLE**](widthtable.md)
</dt> <dt>

[**IFIMETRICS**](https://msdn.microsoft.com/fd2606ed-ec61-430a-aaad-38a4c3a207b6)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WIDTHRUN%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





