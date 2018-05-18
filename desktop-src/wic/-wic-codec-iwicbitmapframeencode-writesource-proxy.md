---
Description: 'Proxy function for the WriteSource method.'
ms.assetid: 'd95ad80f-7a26-45a7-8103-2673989143b7'
title: 'IWICBitmapFrameEncode\_WriteSource\_Proxy function'
---

# IWICBitmapFrameEncode\_WriteSource\_Proxy function

Proxy function for the [**WriteSource**](-wic-codec-iwicbitmapframeencode-writesource.md) method.

## Syntax


```C++
HRESULT IWICBitmapFrameEncode_WriteSource_Proxy(
  _In_ IWICBitmapFrameEncode *THIS_PTR,
  _In_ IWICBitmapSource      *pIBitmapSource,
  _In_ WICRect               *prc
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md)\***

Pointer to this [**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md) object.

</dd> <dt>

*pIBitmapSource* \[in\]
</dt> <dd>

Type: **[**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md)\***

The bitmap source to encode.

</dd> <dt>

*prc* \[in\]
</dt> <dd>

Type: **[**WICRect**](-wic-codec-wicrect.md)\***

The size rectangle of the bitmap source.

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



 

 




