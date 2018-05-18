---
Description: 'The GETINFO\_FONTOBJ structure is used as input to the UNIFONTOBJ\_GetInfo callback function.'
ms.assetid: 'f5116986-aa0c-4cc3-9893-c93e83e922f7'
title: 'GETINFO\_FONTOBJ structure'
---

# GETINFO\_FONTOBJ structure

The GETINFO\_FONTOBJ structure is used as input to the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

## Syntax


```C++
typedef struct _GETINFO_FONTOBJ {
  DWORD   dwSize;
  FONTOBJ *pFontObj;
} GETINFO_FONTOBJ, *PGETINFO_FONTOBJ;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the GETINFO\_FONTOBJ structure. Supplied by the UNIFONTOBJ\_GetInfo caller.

</dd> <dt>

**pFontObj**
</dt> <dd>

Pointer to an empty [**FONTOBJ**](display.fontobj) structure. The structure is filled in by Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function. The pointer is supplied by the UNIFONTOBJ\_GetInfo caller.

</dd> </dl>

## Remarks

To obtain a font's FONTOBJ structure contents, a rendering plug-in can supply the address of a GETINFO\_FONTOBJ structure when calling Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md)
</dt> <dt>

[**FONTOBJ**](display.fontobj)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GETINFO_FONTOBJ%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





