---
Description: The GETINFO\_GLYPHWIDTH structure is used as input to the UNIFONTOBJ\_GetInfo callback function.
ms.assetid: bc01b363-71e9-4c50-ad14-a101abbfe6ec
title: GETINFO\_GLYPHWIDTH structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# GETINFO\_GLYPHWIDTH structure

The GETINFO\_GLYPHWIDTH structure is used as input to the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

## Syntax


```C++
typedef struct _GETINFO_GLYPHWIDTH {
  DWORD dwSize;
  DWORD dwType;
  DWORD dwCount;
  PVOID pGlyph;
  PLONG plWidth;
} GETINFO_GLYPHWIDTH, *PGETINFO_GLYPHWIDTH;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Size, in bytes, of the GETINFO\_GLYPHWIDTH structure. Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**dwType**
</dt> <dd>

Specifies the type of the glyph specifier array pointed to by **pGlyph**. Valid values are:

<dl> <dd>

TYPE\_GLYPHHANDLE

</dd> <dd>

TYPE\_GLYPHID

</dd> </dl>

Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**dwCount**
</dt> <dd>

Specifies the number of elements in the array pointed to by **pGlyph**. Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**pGlyph**
</dt> <dd>

Pointer to an array of glyph specifiers. The array element type is indicated by **dwType**. Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**plWidth**
</dt> <dd>

Pointer to a location into which Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function places the width value. The pointer is supplied by the *UNIFONTOBJ\_GetInfo* caller.

</dd> </dl>

## Remarks

To obtain the width of a set of glyphs, a rendering plug-in can supply the address of a GETINFO\_GLYPHWIDTH structure when calling Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function. The callback function calculates the total width of all the glyphs described by the input array, and places the calculated value in the location pointed to by **plWidth**.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GETINFO_GLYPHWIDTH%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





