---
description: The GetNextVTrack method retrieves the next virtual track after a specified virtual track.
ms.assetid: c43e6b16-a3e4-4407-b48d-b04c4bb66688
title: IAMTimelineComp::GetNextVTrack method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineComp.GetNextVTrack
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineComp::GetNextVTrack method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetNextVTrack` method retrieves the next virtual track after a specified virtual track.

## Syntax


```C++
HRESULT GetNextVTrack(
        IAMTimelineObj *pVirtualTrack,
  [out] IAMTimelineObj **ppNextVirtualTrack
);
```



## Parameters

<dl> <dt>

*pVirtualTrack* 
</dt> <dd>

Pointer to the previous virtual track, or **NULL** to retrieve the first virtual track in the composition.

</dd> <dt>

*ppNextVirtualTrack* \[out\]
</dt> <dd>

Receives a pointer to the [**IAMTimelineObj**](iamtimelineobj.md) interface of the next virtual track, in order of priority.

</dd> </dl>

## Return value

Returns S\_OK if the method retrieves a virtual track, or S\_FALSE otherwise.

## Remarks

If the method succeeds, the **IAMTimelineObj** interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

[**IAMTimelineComp Interface**](iamtimelinecomp.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




