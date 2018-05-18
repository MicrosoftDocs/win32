---
Description: 'Proxy function for the CreateFastMetadataEncoderFromDecoder method.'
ms.assetid: 'eae7ed9c-9205-4e41-91b2-461fd1f5d093'
title: 'IWICImagingFactory\_CreateFastMetadataEncoderFromDecoder\_Proxy function'
---

# IWICImagingFactory\_CreateFastMetadataEncoderFromDecoder\_Proxy function

Proxy function for the [**CreateFastMetadataEncoderFromDecoder**](-wic-codec-iwicimagingfactory-createfastmetadataencoderfromdecoder.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateFastMetadataEncoderFromDecoder_Proxy(
  _In_  IWICImagingFactory      *pFactory,
  _In_  IWICBitmapDecoder       *pIDecoder,
  _Out_ IWICFastMetadataEncoder **ppIFME
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*pIDecoder* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)\***

The decoder to create the [**IWICFastMetadataEncoder**](-wic-codec-iwicfastmetadataencoder.md) from.

</dd> <dt>

*ppIFME* \[out\]
</dt> <dd>

Type: **[**IWICFastMetadataEncoder**](-wic-codec-iwicfastmetadataencoder.md)\*\***

A pointer that receives a pointer to the new [**IWICFastMetadataEncoder**](-wic-codec-iwicfastmetadataencoder.md).

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



 

 




