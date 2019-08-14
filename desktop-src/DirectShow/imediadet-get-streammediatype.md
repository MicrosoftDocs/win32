---
Description: The get\_StreamMediaType method retrieves the media type of the current stream. All video streams are converted to VIDEOINFOHEADER types, and all audio streams are converted to WAVEFORMATEX types.
ms.assetid: 7fc15cb3-af77-42c1-b5eb-d1d88bf9cd1d
title: IMediaDet::get_StreamMediaType method
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- IMediaDet.get_StreamMediaType
api_type:
- COM
api_location:
- strmiids.lib
- strmiids.dll
---

# IMediaDet::get\_StreamMediaType method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_StreamMediaType` method retrieves the media type of the current stream. All video streams are converted to [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) types, and all audio streams are converted to [**WAVEFORMATEX**](https://msdn.microsoft.com/en-us/library/Dd390970(v=VS.85).aspx) types.

## Syntax


```C++
HRESULT get_StreamMediaType(
  [out, retval] AM_MEDIA_TYPE *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/strmif/ns-strmif-am_media_type) structure that is filled with the media type.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Before calling this method, set the file name and stream by calling [**IMediaDet::put\_Filename**](imediadet-put-filename.md) and [**IMediaDet::put\_CurrentStream**](imediadet-put-currentstream.md).

If the media detector is in bitmap grab mode, this method returns E\_INVALIDARG. For more information, see [**IMediaDet::EnterBitmapGrabMode**](imediadet-enterbitmapgrabmode.md).

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IMediaDet Interface**](imediadet.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




