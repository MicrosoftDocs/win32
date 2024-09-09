---
description: The VTrackInsBefore method inserts a virtual track into the composition at the specified priority.
ms.assetid: 82ae0867-13b6-41ae-adb9-a55ac78e21cb
title: IAMTimelineComp::VTrackInsBefore method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineComp.VTrackInsBefore
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineComp::VTrackInsBefore method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `VTrackInsBefore` method inserts a virtual track into the composition at the specified priority.

## Syntax


```C++
HRESULT VTrackInsBefore(
   IAMTimelineObj *pVirtualTrack,
   long           Priority
);
```



## Parameters

<dl> <dt>

*pVirtualTrack* 
</dt> <dd>

Pointer to the [**IAMTimelineObj**](iamtimelineobj.md) interface of the virtual track.

</dd> <dt>

*Priority* 
</dt> <dd>

Priority at which to insert the virtual track, or –1 to insert the virtual track at the end of the priority list. The priority list determines which clips are visible. See Remarks for more information.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                   | Description                               |
|-----------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid argument.<br/>              |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | Object is not a virtual track.<br/> |



 

## Remarks

Each virtual track in composition has a unique priority level. Priority levels range from 0 to *n* - 1, where *n* is the number of virtual tracks in the composition. For video groups, a virtual track hides any virtual tracks with a lower priority level, except in places where the track is empty or contains a transition. You can think of virtual tracks as being layers in the final composition. Track 1 is layered on top of track 0, track 2 is layered on top of track 1, and so forth.

If you specify -1 for the *Priority* parameter, the virtual track is inserted at the end of the list, with a higher priority value than the existing tracks. If you specify a priority value that already exists in the composition, every track with an equal or greater priority moves up one priority level.

**Example**: Track A has priority 0, and track B has priority 1. If track C is inserted at priority 0, track A moves to priority 1, and track B moves to priority 2.

If the specified priority is greater than the current number of tracks in the composition, the method fails.

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

 

 




