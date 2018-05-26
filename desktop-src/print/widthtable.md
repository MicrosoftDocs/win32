---
Description: The WIDTHTABLE structure is used to define the contents of Unidrv font metrics files (.ufm files).
ms.assetid: 6c7b35a2-f9fd-41a9-a353-ec8b78259bf0
title: WIDTHTABLE structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WIDTHTABLE structure

The WIDTHTABLE structure is used to define the contents of [Unidrv font metrics files](print.customized_font_management#ddk-unidrv-font-metrics-files-gg) (.ufm files).

## Syntax


```C++
typedef struct _WIDTHTABLE {
  DWORD    dwSize;
  DWORD    dwRunNum;
  WIDTHRUN WidthRun[1];
} WIDTHTABLE, *PWIDTHTABLE;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the WIDTHTABLE structure, including the **WidthRun** array.

</dd> <dt>

**dwRunNum**
</dt> <dd>

Specifies the number of elements in the **WidthRun** array.

</dd> <dt>

**WidthRun**
</dt> <dd>

Is an array of [**WIDTHRUN**](widthrun.md) structures.

</dd> </dl>

## Remarks

A .ufm file's WIDTHTABLE structure, which describes character widths, is accessed by a pointer in the file's [**UNIFM\_HDR**](unifm-hdr.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**WIDTHRUN**](widthrun.md)
</dt> <dt>

[**UNIFM\_HDR**](unifm-hdr.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WIDTHTABLE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





