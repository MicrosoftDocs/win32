---
Description: 'Proxy function for the CreateFastMetadataEncoderFromFrameDecode method.'
ms.assetid: '0edc3387-47e9-401c-9153-76c8c32b52de'
title: 'IWICImagingFactory\_CreateFastMetadataEncoderFromFrameDecode\_Proxy function'
---

# IWICImagingFactory\_CreateFastMetadataEncoderFromFrameDecode\_Proxy function

Proxy function for the [**CreateFastMetadataEncoderFromFrameDecode**](-wic-codec-iwicimagingfactory-createfastmetadataencoderfromframedecode.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateFastMetadataEncoderFromFrameDecode_Proxy(
  _In_  IWICImagingFactory      *pFactory,
  _In_  IWICBitmapFrameDecode   *pIFrameDecoder,
  _Out_ IWICFastMetadataEncoder **ppIFME
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*pIFrameDecoder* \[in\]
</dt> <dd>

Type: **[**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md)\***

The [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md) to create the [**IWICFastMetadataEncoder**](-wic-codec-iwicfastmetadataencoder.md) from.

</dd> <dt>

*ppIFME* \[out\]
</dt> <dd>

Type: **[**IWICFastMetadataEncoder**](-wic-codec-iwicfastmetadataencoder.md)\*\***

A pointer that receives a pointer to a new [**IWICFastMetadataEncoder**](-wic-codec-iwicfastmetadataencoder.md).

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



 

 




