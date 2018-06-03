---
Description: The MAPTABLE structure is one of the structures used to define the contents of glyph translation table files (.gtt files).
ms.assetid: d3dcf7b0-4244-41c1-801e-cf41b20f2d54
title: MAPTABLE structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MAPTABLE structure

The MAPTABLE structure is one of the structures used to define the contents of [glyph translation table files](https://www.bing.com/search?q=glyph translation table files) (.gtt files).

## Syntax


```C++
typedef struct _MAPTABLE {
  DWORD     dwSize;
  DWORD     dwGlyphNum;
  TRANSDATA Trans[1];
} MAPTABLE, *PMAPTABLE;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the MAPTABLE structure, including the **Trans** array.

</dd> <dt>

**dwGlyphNum**
</dt> <dd>

Specifies the number of elements in the **Trans** array.

</dd> <dt>

**Trans**
</dt> <dd>

Is an array of [**TRANSDATA**](transdata.md) structures.

</dd> </dl>

## Remarks

A .gtt file's MAPTABLE structure, which contains a glyph mapping table, is accessed by a pointer in the file's [**UNI\_GLYPHSETDATA**](uni-glyphsetdata.md) structure. The table maps glyph handles to the character codes or commands that must be sent to the printer in order to print glyphs.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**TRANSDATA**](transdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20MAPTABLE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





