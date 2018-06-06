---
Description: The UFF\_FILEHEADER structure is used to define the contents of Unidrv font format files (.uff files).
ms.assetid: 18eb526b-d615-4f02-b724-236c6bf16945
title: UFF\_FILEHEADER structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# UFF\_FILEHEADER structure

The UFF\_FILEHEADER structure is used to define the contents of [Unidrv font format files](print.customized_font_management#ddk-unidrv-font-format-files-gg) (.uff files).

## Syntax


```C++
typedef struct _UFF_FILEHEADER {
  DWORD dwSignature;
  DWORD dwVersion;
  DWORD dwSize;
  DWORD nFonts;
  DWORD nGlyphSets;
  DWORD nVarData;
  DWORD offFontDir;
  DWORD dwFlags;
  DWORD dwReserved[4];
} UFF_FILEHEADER, *PUFF_FILEHEADER;
```



## Members

<dl> <dt>

**dwSignature**
</dt> <dd>

Specifies the signature for .uff files. This value must be UFF\_FILE\_MAGIC.

</dd> <dt>

**dwVersion**
</dt> <dd>

Specifies the format version for .uff files. This value must be UFF\_VERSION\_NUMBER. The HIWORD contains the major version number and the LOWORD contains the minor version number.

</dd> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the UFF\_FILEHEADER structure.

</dd> <dt>

**nFonts**
</dt> <dd>

Specifies the number of fonts specified within the .uff file and identified by [**DATA\_HEADER**](data-header.md) structures. This is also the number of [**UFF\_FONTDIRECTORY**](uff-fontdirectory.md) structures within the .uff file.

</dd> <dt>

**nGlyphSets**
</dt> <dd>

Specifies the number of glyph sets specified within the .uff file and identified by DATA\_HEADER structures. Some fonts might share a glyph set.

</dd> <dt>

**nVarData**
</dt> <dd>

Specifies the number of variable data sections specified within the .uff file and identified by DATA\_HEADER structures.

</dd> <dt>

**offFontDir**
</dt> <dd>

Specifies the offset, in bytes, from the beginning of the .uff file to the beginning of the first [**UFF\_FONTDIRECTORY**](uff-fontdirectory.md) structure.

</dd> <dt>

**dwFlags**
</dt> <dd>

Is a set of bit flags, as specified in the following table.



| Flag                         | Definition                                                                                                                                            |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| FONT\_DIR\_SORTED<br/> | The array of UFF\_FONTDIRECTORY structures (specified by **offFontDir**) is sorted by the contents of that structure's **wFontID** member.<br/> |



 

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved. Must be set to zero.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**UFF\_FONTDIRECTORY**](uff-fontdirectory.md)
</dt> <dt>

[**DATA\_HEADER**](data-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UFF_FILEHEADER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





