---
description: The GetMediaLength method retrieves the media length of this source object.
ms.assetid: 70298d8f-67e7-4774-a7ae-f0b48e4afda7
title: IAMTimelineSrc::GetMediaLength method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.GetMediaLength
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineSrc::GetMediaLength method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetMediaLength` method retrieves the media length of this source object.

## Syntax


```C++
HRESULT GetMediaLength(
   REFERENCE_TIME *pLength
);
```



## Parameters

<dl> <dt>

*pLength* 
</dt> <dd>

Receives the media length in 100-nanosecond units.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                     | Description                                        |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>            | Success.<br/>                                |
| <dl> <dt>**E\_NOTDETERMINED**</dt> </dl> | Media times are not set on this object.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>       | **NULL** pointer argument.<br/>              |



 

## Remarks

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[**IAMTimelineSrc::SetMediaLength**](iamtimelinesrc-setmedialength.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




