---
Description: 'Proxy function for the CreateBitmap method.'
ms.assetid: '5647521b-231d-4819-97ab-4dfb5f796211'
title: 'IWICImagingFactory\_CreateBitmap\_Proxy function'
---

# IWICImagingFactory\_CreateBitmap\_Proxy function

Proxy function for the [**CreateBitmap**](-wic-codec-iwicimagingfactory-createbitmap.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateBitmap_Proxy(
  _In_  IWICImagingFactory         *pFactory,
  _In_  UINT                       uiWidth,
  _In_  UINT                       uiHeight,
  _In_  REFWICPixelFormatGUID      pixelFormat,
  _In_  WICBitmapCreateCacheOption option,
  _Out_ IWICBitmap                 **ppIBitmap
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*uiWidth* \[in\]
</dt> <dd>

Type: **UINT**

The width of the new bitmap .

</dd> <dt>

*uiHeight* \[in\]
</dt> <dd>

Type: **UINT**

The height of the new bitmap.

</dd> <dt>

*pixelFormat* \[in\]
</dt> <dd>

Type: **REFWICPixelFormatGUID**

The pixel format of the new bitmap.

</dd> <dt>

*option* \[in\]
</dt> <dd>

Type: **[**WICBitmapCreateCacheOption**](-wic-codec-wicbitmapcreatecacheoption.md)**

The cache creation options of the new bitmap.

</dd> <dt>

*ppIBitmap* \[out\]
</dt> <dd>

Type: **[**IWICBitmap**](-wic-codec-iwicbitmap.md)\*\***

A pointer that receives a pointer to the new bitmap.

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



 

 




