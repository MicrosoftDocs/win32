---
Description: 'Proxy function for the GetThumbnail method.'
ms.assetid: '377f8aac-3cdc-44dc-8c60-9b6bce915486'
title: 'IWICBitmapFrameDecode\_GetThumbnail\_Proxy function'
---

# IWICBitmapFrameDecode\_GetThumbnail\_Proxy function

Proxy function for the [**GetThumbnail**](-wic-codec-iwicbitmapframedecode-getthumbnail.md) method.

## Syntax


```C++
HRESULT IWICBitmapFrameDecode_GetThumbnail_Proxy(
  _In_  IWICBitmapFrameDecode *THIS_PTR,
  _Out_ IWICBitmapSource      **ppIThumbnail
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)\***

Pointer to this [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md) object.

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



 

 




