---
Description: 'Proxy function for the CreateDecoderFromStream method.'
ms.assetid: '8395d647-c8c9-4715-b15d-a30755ae0a98'
title: 'IWICImagingFactory\_CreateDecoderFromStream\_Proxy function'
---

# IWICImagingFactory\_CreateDecoderFromStream\_Proxy function

Proxy function for the [**CreateDecoderFromStream**](-wic-codec-iwicimagingfactory-createdecoderfromstream.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateDecoderFromStream_Proxy(
  _In_        IWICImagingFactory *pFactory,
  _In_        IStream            *pIStream,
  _In_  const GUID               *pguidVendor,
  _In_        WICDecodeOptions   metadataOptions,
  _Out_       IWICBitmapDecoder  **ppIDecoder
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*pIStream* \[in\]
</dt> <dd>

Type: **[IStream](https://msdn.microsoft.com/library/windows/desktop/aa380034)\***

The stream to create the decoder from.

</dd> <dt>

*pguidVendor* \[in\]
</dt> <dd>

Type: **const GUID\***

The vendor GUID for the decoder .

</dd> <dt>

*metadataOptions* \[in\]
</dt> <dd>

Type: **[**WICDecodeOptions**](-wic-codec-wicdecodeoptions.md)**

The [**WICDecodeOptions**](-wic-codec-wicdecodeoptions.md) to use when creating the decoder.

</dd> <dt>

*ppIDecoder* \[out\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)\*\***

A pointer that receives a pointer to a new [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md).

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



 

 




