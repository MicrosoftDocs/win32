---
Description: Proxy function for the CreateFastMetadataEncoderFromDecoder method.
ms.assetid: eae7ed9c-9205-4e41-91b2-461fd1f5d093
title: IWICImagingFactory\_CreateFastMetadataEncoderFromDecoder\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICImagingFactory\_CreateFastMetadataEncoderFromDecoder\_Proxy function

Proxy function for the [**CreateFastMetadataEncoderFromDecoder**](/windows/win32/Wincodec/nf-wincodec-iwicimagingfactory-createfastmetadataencoderfromdecoder?branch=master) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateFastMetadataEncoderFromDecoder_Proxy(
  _In_  IWICImagingFactory      *pFactory,
  _In_  IWICBitmapDecoder       *pIDecoder,
  _Out_ IWICFastMetadataEncoder **ppIFME
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\***

</dd> <dt>

*pIDecoder* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)\***

The decoder to create the [**IWICFastMetadataEncoder**](/windows/win32/Wincodec/nn-wincodec-iwicfastmetadataencoder?branch=master) from.

</dd> <dt>

*ppIFME* \[out\]
</dt> <dd>

Type: **[**IWICFastMetadataEncoder**](/windows/win32/Wincodec/nn-wincodec-iwicfastmetadataencoder?branch=master)\*\***

A pointer that receives a pointer to the new [**IWICFastMetadataEncoder**](/windows/win32/Wincodec/nn-wincodec-iwicfastmetadataencoder?branch=master).

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



 

 




