---
description: The get\_StreamType method retrieves the globally unique identifier (GUID) for the media type of the current stream.
ms.assetid: 2f61b3fe-c041-4031-9211-2f5fc189542b
title: IMediaDet::get_StreamType method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.get_StreamType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IMediaDet::get\_StreamType method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_StreamType` method retrieves the globally unique identifier (GUID) for the media type of the current stream.

## Syntax


```C++
HRESULT get_StreamType(
  [out, retval] GUID *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the major type GUID for the media type.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method retrieves the **majortype** member of the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure. The **AM\_MEDIA\_TYPE** structure describes the format of the stream, and the **majortype** member is a GUID that indicates the general category, such as audio or video. For a video stream, the GUID is MEDIATYPE\_Video. For audio, it is MEDIATYPE\_Audio. To retrieve the entire **AM\_MEDIA\_TYPE** structure, call the [**IMediaDet::get\_StreamMediaType**](imediadet-get-streammediatype.md) method.

Before calling this method, set the file name and stream by calling [**IMediaDet::put\_Filename**](imediadet-put-filename.md) and [**IMediaDet::put\_CurrentStream**](imediadet-put-currentstream.md).

If the media detector is in bitmap grab mode, this method returns E\_INVALIDARG. For more information, see [**IMediaDet::EnterBitmapGrabMode**](imediadet-enterbitmapgrabmode.md).

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IMediaDet Interface**](imediadet.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




