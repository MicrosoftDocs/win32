---
Description: The GLYPHRUN structure is one of the structures used to define the contents of glyph translation table files (.gtt files).
ms.assetid: 21f6631c-dff1-459f-a83e-7aa1d5d2ab2b
title: GLYPHRUN structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GLYPHRUN structure

The GLYPHRUN structure is one of the structures used to define the contents of [glyph translation table files](print.customized_font_management#ddk-glyph-translation-table-files-gg) (.gtt files).

## Syntax


```C++
typedef struct _GLYPHRUN {
  WCHAR wcLow;
  WORD  wGlyphCount;
} GLYPHRUN, *PGLYPHRUN;
```



## Members

<dl> <dt>

**wcLow**
</dt> <dd>

Specifies a Unicode value representing the first glyph in the glyph run.

</dd> <dt>

**wGlyphCount**
</dt> <dd>

Specifies the number of glyphs represented by the glyph run.

</dd> </dl>

## Remarks

A .gtt (glyph translation table) file contains an array of GLYPHRUN structures. Each structure identifies a set of Unicode values for which the printer provides glyphs. The array is described by the **IoRunOffset** and **dwRunCount** members of a .gtt file's [**UNI\_GLYPHSETDATA**](uni-glyphsetdata.md) structure.

The GLYPHRUN structures must be defined in ascending order, based on the value of **wcLow**. Unidrv uses the GLYPHRUN array to generate glyph handles. Unidrv stores these glyph handles in a [**WCRUN**](display.wcrun) array within an [**FD\_GLYPHSET**](display.fd_glyphset) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**UNI\_GLYPHSETDATA**](uni-glyphsetdata.md)
</dt> <dt>

[**WCRUN**](display.wcrun)
</dt> <dt>

[**FD\_GLYPHSET**](display.fd_glyphset)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GLYPHRUN%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





