---
Description: 'Proxy function for negotiating the pixel format and the palette for the encoder.'
ms.assetid: '01179598-ba40-4aed-a7c4-888cb4e851f4'
title: 'WICSetEncoderFormat\_Proxy function'
---

# WICSetEncoderFormat\_Proxy function

Proxy function for negotiating the pixel format and the palette for the encoder.

## Syntax


```C++
HRESULT WICSetEncoderFormat_Proxy(
  _In_  IWICBitmapSource      *pSourceIn,
  _In_  IWICPalette           *pIPalette,
  _In_  IWICBitmapFrameEncode *pIFrameEncode,
  _Out_ IWICBitmapSource      **ppSourceOut
);
```



## Parameters

<dl> <dt>

*pSourceIn* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\***

Pointer to the source bitmap.

</dd> <dt>

*pIPalette* \[in\]
</dt> <dd>

Type: **[**IWICPalette**](-wic-codec-iwicpalette.md)\***

Pointer to the palette to use for encoding.

</dd> <dt>

*pIFrameEncode* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md)\***

Pointer to the frame encode object.

</dd> <dt>

*ppSourceOut* \[out\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\*\***

Pointer that receives a pointer to the output source.

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



 

 




