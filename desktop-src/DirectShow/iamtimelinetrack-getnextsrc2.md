---
description: The GetNextSrc2 method searches the track for the next source that appears at the specified time or later. This method is equivalent to IAMTimelineTrack::GetNextSrc, but takes a REFTIME value.
ms.assetid: f3f7b000-ec73-4ae9-802b-a9bc6f1840b3
title: IAMTimelineTrack::GetNextSrc2 method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.GetNextSrc2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTrack::GetNextSrc2 method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetNextSrc2` method searches the track for the next source that appears at the specified time or later. This method is equivalent to [**IAMTimelineTrack::GetNextSrc**](iamtimelinetrack-getnextsrc.md), but takes a [**REFTIME**](reftime.md) value.

## Syntax


```C++
HRESULT GetNextSrc2(
  [out] IAMTimelineObj **ppSrc,
        REFTIME        *pInOut
);
```



## Parameters

<dl> <dt>

*ppSrc* \[out\]
</dt> <dd>

Receives a pointer to the source object's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> <dt>

*pInOut* 
</dt> <dd>

On input, contains the start time for the search, in seconds. If the method retrieves a source, it sets the value to the stop time of the source. If the method does not retrieve a source, the value becomes invalid and the application should not use it.

</dd> </dl>

## Return value

Returns S\_OK if the method retrieves a source, or S\_FALSE otherwise.

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

[**IAMTimelineTrack Interface**](iamtimelinetrack.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




