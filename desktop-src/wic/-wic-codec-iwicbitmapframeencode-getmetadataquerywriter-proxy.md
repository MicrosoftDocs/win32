---
Description: 'Proxy function for the GetMetadataQueryWriter method.'
ms.assetid: 'b2c61dee-b72b-408c-8cb9-de2587587f1f'
title: 'IWICBitmapFrameEncode\_GetMetadataQueryWriter\_Proxy function'
---

# IWICBitmapFrameEncode\_GetMetadataQueryWriter\_Proxy function

Proxy function for the [**GetMetadataQueryWriter**](-wic-codec-iwicbitmapframeencode-getmetadataquerywriter.md) method.

## Syntax


```C++
HRESULT IWICBitmapFrameEncode_GetMetadataQueryWriter_Proxy(
  _In_  IWICBitmapFrameEncode   *THIS_PTR,
  _Out_ IWICMetadataQueryWriter **ppIMetadataQueryWriter
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md)\***

Pointer to this [**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md) object.

</dd> <dt>

*ppIMetadataQueryWriter* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryWriter**](-wic-codec-iwicmetadataquerywriter.md)\*\***

A pointer that receives a metadata query writer for the frame.

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



 

 




