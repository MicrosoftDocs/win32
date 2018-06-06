---
Description: The KERNDATA structure is used for describing printer kerning pairs.
ms.assetid: b3f68c08-7097-46e7-ad47-6e5e1f2cb8b2
title: KERNDATA structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# KERNDATA structure

The KERNDATA structure is used for describing printer kerning pairs.

## Syntax


```C++
typedef struct _KERNDATA {
  DWORD          dwSize;
  DWORD          dwKernPairNum;
  FD_KERNINGPAIR KernPair[1];
} KERNDATA, *PKERNDATA;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of KERNDATA structure, including the **KernPair** array.

</dd> <dt>

**dwKernPairNum**
</dt> <dd>

Specifies the number of elements in the **KernPair** array.

</dd> <dt>

**KernPair**
</dt> <dd>

Is an array of [**FD\_KERNINGPAIR**](https://msdn.microsoft.com/5c5eced6-a0a3-448e-bcb3-57be1b703797) structures.

</dd> </dl>

## Remarks

A .ufm file's KERNDATA structures are accessed by a pointer in the file's [**UNIFM\_HDR**](unifm-hdr.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**FD\_KERNINGPAIR**](https://msdn.microsoft.com/5c5eced6-a0a3-448e-bcb3-57be1b703797)
</dt> <dt>

[**UNIFM\_HDR**](unifm-hdr.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20KERNDATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





