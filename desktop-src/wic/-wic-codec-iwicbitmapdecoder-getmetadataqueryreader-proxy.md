---
Description: 'Proxy function for the GetMetadataQueryReader method.'
ms.assetid: 'cc32bdf1-d807-46ac-87b7-77bf2d498e72'
title: 'IWICBitmapDecoder\_GetMetadataQueryReader\_Proxy function'
---

# IWICBitmapDecoder\_GetMetadataQueryReader\_Proxy function

Proxy function for the [**GetMetadataQueryReader**](-wic-codec-iwicbitmapdecoder-getmetadataqueryreader.md) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetMetadataQueryReader_Proxy(
  _In_  IWICBitmapDecoder       *THIS_PTR,
  _Out_ IWICMetadataQueryReader **ppIMetadataQueryReader
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)\***

Pointer to this [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) object.

</dd> <dt>

*ppIMetadataQueryReader* \[out\]
</dt> <dd>

Type: **[**IWICMetadataQueryReader**](-wic-codec-iwicmetadataqueryreader.md)\*\***

A pointer that receives a pointer to the metadata.

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



 

 




