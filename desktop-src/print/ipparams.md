---
Description: 'The IPPARAMS structure is used as an input parameter to a rendering plug-in''s IPrintOemUni::ImageProcessing method.'
ms.assetid: '14ed4180-9ac1-46dd-af76-8d79a2a1fd2d'
title: IPPARAMS structure
---

# IPPARAMS structure

The IPPARAMS structure is used as an input parameter to a rendering plug-in's [**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md) method.

## Syntax


```C++
typedef struct {
  DWORD dwSize;
  POINT ptOffset;
  PSTR  pHalftoneOption;
  BOOL  bBanding;
  BOOL  bBlankBand;
} IPPARAMS, *PIPPARAMS;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes of the IPPARAMS structure. Supplied by Unidrv.

</dd> <dt>

**ptOffset**
</dt> <dd>

Pointer to a [**POINT**](display.point) structure containing the banded image's offset from the upper left corner of the drawing area. Supplied by Unidrv.

</dd> <dt>

**pHalftoneOption**
</dt> <dd>

Pointer to a string containing the name of the currently selected halftoning option. Supplied by Unidrv.

</dd> <dt>

**bBanding**
</dt> <dd>

Specifies whether image banding is active. If **TRUE**, image banding is active. If **FALSE**, image banding is not active. Supplied by Unidrv.

</dd> <dt>

**bBlankBand**
</dt> <dd>

Specifies whether a blank band was drawn in the source bitmap supplied to [**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md). A value of **TRUE** indicates that nothing was drawn in the source bitmap supplied to **IPrintOemUni::ImageProcessing**. A **TRUE** value also indicates that data in the source bitmap is invalid and should not be processed. Supplied by Unidrv.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md)
</dt> <dt>

[**POINT**](display.point)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPPARAMS%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





