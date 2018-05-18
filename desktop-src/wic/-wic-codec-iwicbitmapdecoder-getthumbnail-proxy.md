---
Description: 'Proxy function for the GetThumbnail method.'
ms.assetid: '37a6ba78-0d1b-47f6-9b12-8ad123c8ee86'
title: 'IWICBitmapDecoder\_GetThumbnail\_Proxy function'
---

# IWICBitmapDecoder\_GetThumbnail\_Proxy function

Proxy function for the [**GetThumbnail**](-wic-codec-iwicbitmapdecoder-getthumbnail.md) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetThumbnail_Proxy(
  _In_  IWICBitmapDecoder *THIS_PTR,
  _Out_ IWICBitmapSource  **ppIThumbnail
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)\***

Pointer to this [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) object.

</dd> <dt>

*ppIThumbnail* \[out\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\*\***

A pointer that receives a pointer to the [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) of the thumbnail.

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



 

 




