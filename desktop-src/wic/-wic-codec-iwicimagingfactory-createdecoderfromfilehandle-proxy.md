---
Description: 'Proxy function for the CreateDecoderFromFileHandle method.'
ms.assetid: 'bc7f8a07-6d82-4d95-88ef-979d571758f4'
title: 'IWICImagingFactory\_CreateDecoderFromFileHandle\_Proxy function'
---

# IWICImagingFactory\_CreateDecoderFromFileHandle\_Proxy function

Proxy function for the [**CreateDecoderFromFileHandle**](-wic-codec-iwicimagingfactory-createdecoderfromfilehandle.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateDecoderFromFileHandle_Proxy(
  _In_        IWICImagingFactory *pFactory,
  _In_        ULONG_PTR          hFile,
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

*hFile* \[in\]
</dt> <dd>

Type: **ULONG\_PTR**

The file handle to create the decoder from.

</dd> <dt>

*pguidVendor* \[in\]
</dt> <dd>

Type: **const GUID\***

The vendor GUID for the decoder.

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



 

 




