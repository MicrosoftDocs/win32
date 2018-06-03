---
Description: The UNI\_GLYPHSEDATA structure is one of the structures used to define the contents of glyph translation table files (.gtt files).
ms.assetid: a2c98783-c463-435e-9d78-c10686f1c75c
title: UNI\_GLYPHSETDATA structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# UNI\_GLYPHSETDATA structure

The UNI\_GLYPHSEDATA structure is one of the structures used to define the contents of [glyph translation table files](https://www.bing.com/search?q=glyph translation table files) (.gtt files).

## Syntax


```C++
typedef struct _UNI_GLYPHSETDATA {
  DWORD dwSize;
  DWORD dwVersion;
  DWORD dwFlags;
  LONG  lPredefinedID;
  DWORD dwGlyphCount;
  DWORD dwRunCount;
  DWORD loRunOffset;
  DWORD dwCodePageCount;
  DWORD loCodePageOffset;
  DWORD loMapTableOffset;
  DWORD dwReserved[2];
} UNI_GLYPHSETDATA, *PUNI_GLYPHSETDATA;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the total size, in bytes, of the .gtt file. Note that this is the total size of all structures used to define the file. This value is not the size of the UNI\_GLYPHSETDATA structure.

</dd> <dt>

**dwVersion**
</dt> <dd>

Specifies the file version number, as defined in prntfont.h by a constant with a name format of UNI\_GLYPHSETDATA\_VERSION\_*x*\_*x*.

</dd> <dt>

**dwFlags**
</dt> <dd>

Not used.

</dd> <dt>

**lPredefinedID**
</dt> <dd>

Specifies one of the CC\_-prefixed code conversion identifiers defined in prntfont.h.

</dd> <dt>

**dwGlyphCount**
</dt> <dd>

Specifies the number of glyphs provided by this font.

</dd> <dt>

**dwRunCount**
</dt> <dd>

Specifies the number of [**GLYPHRUN**](glyphrun.md) structures in the array pointed to by **loRunOffset**.

</dd> <dt>

**loRunOffset**
</dt> <dd>

Specifies the byte offset from the beginning of the UNI\_GLYPHSETDATA structure to the beginning of an array of [**GLYPHRUN**](glyphrun.md) structures.

</dd> <dt>

**dwCodePageCount**
</dt> <dd>

Specifies the number of [**UNI\_CODEPAGEINFO**](uni-codepageinfo.md) structures in the array pointed to by **loCodePageOffset**.

</dd> <dt>

**loCodePageOffset**
</dt> <dd>

Specifies the byte offset from the beginning of the UNI\_GLYPHSETDATA structure to the beginning of an array of [**UNI\_CODEPAGEINFO**](uni-codepageinfo.md) structures.

</dd> <dt>

**loMapTableOffset**
</dt> <dd>

Specifies the byte offset from the beginning of the UNI\_GLYPHSETDATA structure to the beginning of a [**MAPTABLE**](maptable.md) structure.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Remarks

A UNI\_GLYPHSETDATA structure must be the first structure contained in a .gtt file.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**GLYPHRUN**](glyphrun.md)
</dt> <dt>

[**UNI\_CODEPAGEINFO**](uni-codepageinfo.md)
</dt> <dt>

[**MAPTABLE**](maptable.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UNI_GLYPHSETDATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





