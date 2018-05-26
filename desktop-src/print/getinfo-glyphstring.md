---
Description: The GETINFO\_GLYPHSTRING structure is used as input to the UNIFONTOBJ\_GetInfo callback function.
ms.assetid: ebcc1ada-af6f-46c3-a025-97079eb08816
title: GETINFO\_GLYPHSTRING structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GETINFO\_GLYPHSTRING structure

The GETINFO\_GLYPHSTRING structure is used as input to the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

## Syntax


```C++
typedef struct _GETINFO_GLYPHSTRING {
  DWORD dwSize;
  DWORD dwCount;
  DWORD dwTypeIn;
  PVOID pGlyphIn;
  DWORD dwTypeOut;
  PVOID pGlyphOut;
  DWORD dwGlyphOutSize;
} GETINFO_GLYPHSTRING, *PGETINFO_GLYPHSTRING;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the GETINFO\_GLYPHSTRING structure. This value is supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**dwCount**
</dt> <dd>

Specifies the number of elements in the arrays pointed to by **pGlyphIn** and **pGlyphOut**. This value is supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**dwTypeIn**
</dt> <dd>

Specifies the type of glyph specifier array pointed to by **pGlyphIn**. Valid values are as follows:



| Value                        | Definition                                                                                                                                                                                                                                     |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE\_GLYPHHANDLE<br/> | The **pGlyphIn** array elements are of type HGLYPH, or handle to a device font glyph. For this value of **dwTypeIn**, valid values for **dwTypeOut** are either TYPE\_UNICODE or TYPE\_TRANSDATA.<br/>                                   |
| TYPE\_GLYPHID<br/>     | The **pGlyphIn** array elements are of type DWORD, and contain glyph identifiers for downloaded TrueType font glyphs. For this value of **dwTypeIn**, valid values for **dwTypeOut** are either TYPE\_UNICODE or TYPE\_GLYPHHANDLE.<br/> |



 

Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**pGlyphIn**
</dt> <dd>

Pointer to an array of glyph specifiers. The array element type is indicated by **dwTypeIn**. This value is supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**dwTypeOut**
</dt> <dd>

Specifies the type of glyph specifier array pointed to by **pGlyphOut**. Valid values are as follows:



| Value                        | Definition                                                                                                                                                                  |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE\_GLYPHHANDLE<br/> | The **pGlyphOut** array elements are of type HGLYPH, or handle to a device font glyph. This value is valid only when **dwTypeIn** has been set to TYPE\_GLYPHID.<br/> |
| TYPE\_TRANSDATA<br/>   | The **pGlyphOut** array elements are of type [**TRANSDATA**](transdata.md). This value is valid only when **dwTypeIn** has been set to TYPE\_GLYPHHANDLE.<br/>       |
| TYPE\_UNICODE<br/>     | The *pGlyph* array elements are of type WCHAR. This value is valid when **dwTypeIn** has been set to either TYPE\_GLYPHHANDLE or TYPE\_GLYPHID.<br/>                  |



 

<dl> <dd>

Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> </dl> </dd> <dt>

**pGlyphOut**
</dt> <dd>

Caller-supplied pointer to an empty array of glyph specifiers. The array is filled in by Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function. The array element type is indicated by **dwTypeOut**. This pointer is supplied by the <span class="underline">UNIFONTOBJ\_GetInfo</span> caller.

</dd> <dt>

**dwGlyphOutSize**
</dt> <dd>

Specifies the size, in bytes, of the buffer pointed to by **pGlyphOut**. This member is used only when **dwTypeIn** has been set to TYPE\_GLYPHHANDLE and **dwTypeOut** has been set to TYPE\_TRANSDATA. See the following Remarks section for more information.

</dd> </dl>

## Remarks

To convert an array of glyph specifiers from one type to another, a rendering plug-in can supply the address of a GETINFO\_GLYPHSTRING structure when calling Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

If the conversion is from TYPE\_GLYPHHANDLE to TYPE\_TRANSDATA, [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) must be called twice.

1.  Before the first call to [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md), the rendering plug-in fills in the **dwSize**, **dwCount**, **dwTypeIn**, and **pGlyphIn** members and sets **dwGlyphOutSize** member to zero.

    After [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) returns, the **dwGlyphOutSize** member contains the size, in bytes, of the buffer needed to store the converted string.

2.  The plug-in allocates a block of memory of the size received in the **dwGlyphOutSize** member, sets the **pGlyphOut** member to point to this memory block, and calls [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) once more. UNIDRV then converts the string from TYPE\_GLYPHHANDLE to TYPE\_TRANSDATA.

The values that a rendering plug-in specifies for the **dwTypeIn** and **pGlyphIn** members typically are those that were previously received as the **dwType** and *pGlyph* parameters to the [**IPrintOemUni::OutputCharStr**](iprintoemuni-outputcharstr.md) method.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md)
</dt> <dt>

[**IPrintOemUni::OutputCharStr**](iprintoemuni-outputcharstr.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GETINFO_GLYPHSTRING%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





