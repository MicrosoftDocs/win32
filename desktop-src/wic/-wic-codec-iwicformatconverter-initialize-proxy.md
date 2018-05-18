---
Description: 'Proxy function for the Initialize method.'
ms.assetid: '26112d52-95e2-4c67-83fc-cf5e28712730'
title: 'IWICFormatConverter\_Initialize\_Proxy function'
---

# IWICFormatConverter\_Initialize\_Proxy function

Proxy function for the [**Initialize**](-wic-codec-iwicformatconverter-initialize.md) method.

## Syntax


```C++
HRESULT IWICFormatConverter_Initialize_Proxy(
  _In_ IWICFormatConverter   *THIS_PTR,
  _In_ IWICBitmapSource      *pISource,
  _In_ REFWICPixelFormatGUID dstFormat,
  _In_ WICBitmapDitherType   dither,
  _In_ IWICPalette           *pIPalette,
  _In_ double                alphaThresholdPercent,
  _In_ WICBitmapPaletteType  paletteTranslate
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICFormatConverter**](-wic-codec-iwicformatconverter.md)\***

Pointer to this [**IWICFormatConverter**](-wic-codec-iwicformatconverter.md) object.

</dd> <dt>

*pISource* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\***

The input bitmap to convert

</dd> <dt>

*dstFormat* \[in\]
</dt> <dd>

Type: **REFWICPixelFormatGUID**

The destination pixel format GUID.

</dd> <dt>

*dither* \[in\]
</dt> <dd>

Type: **[**WICBitmapDitherType**](-wic-codec-wicbitmapdithertype.md)**

The [**WICBitmapDitherType**](-wic-codec-wicbitmapdithertype.md) used for conversion.

</dd> <dt>

*pIPalette* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\***

The palette to use for conversion.

</dd> <dt>

*alphaThresholdPercent* \[in\]
</dt> <dd>

Type: **double**

The alpha threshold to use for conversion.

</dd> <dt>

*paletteTranslate* \[in\]
</dt> <dd>

Type: **[**WICBitmapPaletteType**](-wic-codec-wicbitmappalettetype.md)**

The palette translation type to use for conversion.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




