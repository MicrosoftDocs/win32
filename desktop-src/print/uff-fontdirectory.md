---
Description: 'The UFF\_FONTDIRECTORY structure is used to specify the directory of font descriptions contained in a Unidrv font format file (.uff file).'
ms.assetid: 'd1cde8a4-f27b-440c-bfb1-c9a564c59c04'
title: 'UFF\_FONTDIRECTORY structure'
---

# UFF\_FONTDIRECTORY structure

The UFF\_FONTDIRECTORY structure is used to specify the directory of font descriptions contained in a Unidrv font format file (.uff file).

## Syntax


```C++
typedef struct _UFF_FONTDIRECTORY {
  DWORD dwSignature;
  WORD  wSize;
  WORD  wFontID;
  SHORT sGlyphID;
  WORD  wFlags;
  DWORD dwInstallerSig;
  DWORD offFontName;
  DWORD offCartridgeName;
  DWORD offFontData;
  DWORD offGlyphData;
  DWORD offVarData;
} UFF_FONTDIRECTORY, *PUFF_FONTDIRECTORY;
```



## Members

<dl> <dt>

**dwSignature**
</dt> <dd>

Specifies the font metrics record signature. This value must be FONT\_REC\_SIG.

</dd> <dt>

**wSize**
</dt> <dd>

Specifies the size, in bytes, of the UFF\_FONTDIRECTORY structure.

</dd> <dt>

**wFontID**
</dt> <dd>

Specifies the font identifier. This value must match the **wDataID** member of a [**DATA\_HEADER**](data-header.md) structure that specifies font metrics information within the .uff file.

</dd> <dt>

**sGlyphID**
</dt> <dd>

Specifies the glyph set identifier. This value specifies the glyph set that is to be associated with the font. See the following Remarks section.

</dd> <dt>

**wFlags**
</dt> <dd>

Is a set of bit flags. One or more of the following flags can be specified.



| Flag                               | Definition                                                                                                                                                                |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FONT\_FL\_DEVICEFONT<br/>    | The font is a device font.<br/>                                                                                                                                     |
| FONT\_FL\_GLYPHSET\_GTT<br/> | The glyph set is specified in Windows 2000 and later [*GTT*](wdkgloss.g#wdkgloss-glyph-translation-table--gtt-) format.<br/> |
| FONT\_FL\_GLYPHSET\_RLE<br/> | The glyph set is specified in Windows NT 4.0 [*RLE*](wdkgloss.r#wdkgloss-run-length-encoded--rle--bitmap) format.<br/>     |
| FONT\_FL\_IFI<br/>           | Font metrics are specified in Windows NT 4.0 IFI format.<br/>                                                                                                       |
| FONT\_FL\_PERMANENT\_SF<br/> | The font is a PCL permanent soft font.<br/>                                                                                                                         |
| FONT\_FL\_SOFTFONT<br/>      | The font is a [*PCL*](wdkgloss.p#wdkgloss-pcl) soft font.<br/>                                                                                         |
| FONT\_FL\_UFM<br/>           | Font metrics are specified in Windows 2000 and later [*UFM*](wdkgloss.u#wdkgloss-unidrv-font-metrics--ufm-) format.<br/>         |



 

</dd> <dt>

**dwInstallerSig**
</dt> <dd>

Specifies the signature value of the font installer that installed the font.

</dd> <dt>

**offFontName**
</dt> <dd>

Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned, NULL-terminated, Unicode string representing the name of the font.

</dd> <dt>

**offCartridgeName**
</dt> <dd>

Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned, NULL-terminated, Unicode string representing the name of the font cartridge containing the font. If the font is not contained in a cartridge, this value should be zero.

</dd> <dt>

**offFontData**
</dt> <dd>

Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned [**DATA\_HEADER**](data-header.md) structure specifying a font metrics section.

</dd> <dt>

**offGlyphData**
</dt> <dd>

Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned DATA\_HEADER structure specifying a glyph set section. If **sGlyphID** is zero or negative, **offGlyphData** should be zero.

</dd> <dt>

**offVarData**
</dt> <dd>

Specifies the offset, in bytes, from the beginning of the .uff file to a DWORD-aligned [**DATA\_HEADER**](data-header.md) structure specifying a data section. If the FONT\_FL\_PERMANENT\_SF flag is set in **wFlags**, **offVarData** must be zero.

</dd> </dl>

## Remarks

If **sGlyphID** is a greater than zero, it must match the **wDataID** member of a [**DATA\_HEADER**](data-header.md) structure that specifies a glyph set within the .uff file.

If **sGlyphID** is less than zero, it must be one of the CC\_-prefixed constants defined in prntfont.h, which identify predefined glyph sets.

If **sGlyphID** is zero, Unidrv uses the glyph set resource identifier contained in the font's UNIFM\_HDR structure. The glyph set resource must be contained in the minidriver's resource DLL, or else Unidrv uses the default glyph translation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**DATA\_HEADER**](data-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UFF_FONTDIRECTORY%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





