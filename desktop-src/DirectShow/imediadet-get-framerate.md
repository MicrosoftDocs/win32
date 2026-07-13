---
description: The get\_FrameRate method retrieves the frame rate of the current stream. The stream must be a video stream.
ms.assetid: f128d118-1147-4a0a-946e-bd1716606cef
title: IMediaDet::get_FrameRate method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.get_FrameRate
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IMediaDet::get\_FrameRate method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_FrameRate` method retrieves the frame rate of the current stream. The stream must be a video stream.

## Syntax


```C++
HRESULT get_FrameRate(
  [out, retval] double *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the frame rate, in frames per second.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following:



| Return code                                                                                             | Description                                                   |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>                 | Video format header does not specify a frame rate.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Invalid argument.<br/>                                  |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | **NULL** pointer argument.<br/>                         |
| <dl> <dt>**VFW\_E\_INVALIDMEDIATYPE**</dt> </dl> | Invalid media type.<br/>                                |



 

## Remarks

This method cannot retrieve the frame rate from an ASF file.

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

 

 




