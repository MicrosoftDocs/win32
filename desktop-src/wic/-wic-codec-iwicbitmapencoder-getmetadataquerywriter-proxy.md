---
Description: 'Proxy function for the GetMetadataQueryWriter method.'
ms.assetid: '3186d473-f8a7-405a-8429-3f50104bee4a'
title: 'IWICBitmapEncoder\_GetMetadataQueryWriter\_Proxy function'
---

# IWICBitmapEncoder\_GetMetadataQueryWriter\_Proxy function

Proxy function for the [**GetMetadataQueryWriter**](-wic-codec-iwicbitmapencoder-getmetadataquerywriter.md) method.

## Syntax


```C++
HRESULT IWICBitmapEncoder_GetMetadataQueryWriter_Proxy(
  _In_  IWICBitmapEncoder       *THIS_PTR,
  _Out_ IWICMetadataQueryWriter **ppIMetadataQueryWriter
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)\***

Pointer to this [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md) object.

</dd> <dt>

*ppIMetadataQueryWriter* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryWriter**](-wic-codec-iwicmetadataquerywriter.md)\*\***

A pointer that receives a pointer to an [**IWICMetadataQueryWriter**](-wic-codec-iwicmetadataquerywriter.md).

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



 

 




