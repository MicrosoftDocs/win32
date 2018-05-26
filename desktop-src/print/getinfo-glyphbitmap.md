---
Description: The GETINFO\_GLYPHBITMAP structure is used as input to the UNIFONTOBJ\_GetInfo callback function.
ms.assetid: 6a5887fd-0269-4cd1-acf1-f7242016d993
title: GETINFO\_GLYPHBITMAP structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GETINFO\_GLYPHBITMAP structure

The GETINFO\_GLYPHBITMAP structure is used as input to the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

## Syntax


```C++
typedef struct _GETINFO_GLYPHBITMAP {
  DWORD     dwSize;
  HGLYPH    hGlyph;
  GLYPHDATA *pGlyphData;
} GETINFO_GLYPHBITMAP, *PGETINFO_GLYPHBITMAP;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the GETINFO\_GLYPHBITMAP structure. Supplied by [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**hGlyph**
</dt> <dd>

Handle to the glyph. See the following Remarks section. Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**pGlyphData**
</dt> <dd>

Pointer to a [**GLYPHDATA**](display.glyphdata) structure. The structure is filled in by Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function. The pointer is supplied by the *UNIFONTOBJ\_GetInfo* caller.

</dd> </dl>

## Remarks

To obtain a glyph bitmap, a rendering plug-in can supply the address of a GETINFO\_GLYPHBITMAP structure when calling Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

The value that a rendering plug-in specifies for the **hGlyph** member must have been previously received as the *hGlyph* parameter to the [**IPrintOemUni::DownloadCharGlyph**](iprintoemuni-downloadcharglyph.md) method.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md)
</dt> <dt>

[**GLYPHDATA**](display.glyphdata)
</dt> <dt>

[**IPrintOemUni::DownloadCharGlyph**](iprintoemuni-downloadcharglyph.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GETINFO_GLYPHBITMAP%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





