---
Description: Proxy function for the CreateDecoderFromStream method.
ms.assetid: 8395d647-c8c9-4715-b15d-a30755ae0a98
title: IWICImagingFactory\_CreateDecoderFromStream\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICImagingFactory\_CreateDecoderFromStream\_Proxy function

Proxy function for the [**CreateDecoderFromStream**](/windows/win32/Wincodec/nf-wincodec-iwicimagingfactory-createdecoderfromstream?branch=master) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateDecoderFromStream_Proxy(
  _In_        IWICImagingFactory *pFactory,
  _In_        IStream            *pIStream,
  _In_  const GUID               *pguidVendor,
  _In_        WICDecodeOptions   metadataOptions,
  _Out_       IWICBitmapDecoder  **ppIDecoder
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\***

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

Type: **[**WICDecodeOptions**](/windows/win32/Wincodec/ne-wincodec-wicdecodeoptions?branch=master)**

The [**WICDecodeOptions**](/windows/win32/Wincodec/ne-wincodec-wicdecodeoptions?branch=master) to use when creating the decoder.

</dd> <dt>

*ppIDecoder* \[out\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)\*\***

A pointer that receives a pointer to a new [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master).

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




