---
description: The put\_MediaType method sets the output media type on the resizer filter.
ms.assetid: e213179e-cc88-4365-aaa0-51d4b9c97476
title: IResize::put_MediaType method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IResize.put_MediaType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IResize::put\_MediaType method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_MediaType` method sets the output media type on the resizer filter.

## Syntax


```C++
HRESULT put_MediaType(
  [in] const AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pmt* \[in\]
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure that contains the media type.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

DES calls this method before it connects the filter's output pin. Use the media type as the output pin's media type. Return this media type in the [**CTransformFilter::GetMediaType**](ctransformfilter-getmediatype.md) method, and check agsint this type in the [**CTransformFilter::CheckTransform**](ctransformfilter-checktransform.md) method. DES never calls this method after the output pin is connected.

Currently, DES always sets the output media type to an uncompressed RGB format with a **VIDEOINFOHEADER** format block (format type equals FORMAT\_VideoInfo). The subtype might be MEDIASUBTYPE\_ARGB32, which indicates 32-bit RGB with an alpha channel.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | DirectX 9.0 or later<br/>                                                         |
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IResize Interface**](iresize.md)
</dt> </dl>

 

 




