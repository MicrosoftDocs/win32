---
description: The SetStartStop method sets the object's start and stop times, relative to the object's parent.
ms.assetid: 6275a36b-f963-4916-bf60-ea68008ad153
title: IAMTimelineObj::SetStartStop method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetStartStop
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineObj::SetStartStop method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetStartStop` method sets the object's start and stop times, relative to the object's parent.

## Syntax


```C++
HRESULT SetStartStop(
   REFERENCE_TIME Start,
   REFERENCE_TIME Stop
);
```



## Parameters

<dl> <dt>

*Start* 
</dt> <dd>

New start time, in 100-nanosecond units, or –1 to keep the existing start time.

</dd> <dt>

*Stop* 
</dt> <dd>

New stop time, in 100-nanosecond units, or –1 to keep the existing stop time.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                  | Description                  |
|----------------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument.<br/> |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>    | Not implemented.<br/>  |



 

## Remarks

Tracks, compositions, and groups do not implement this method. For these objects, the start time is always zero, and the stop time is the maximum stop time of the objects they contain.

Do not set overlapping times on source objects within the same track. Doing so can cause undefined behaviors.

For source objects, the start and stop times are independent of the media start and media stop times. Changing one pair of values does not change the other. To set the media start and stop times, call the [**IAMTimelineSrc::SetMediaTimes**](iamtimelinesrc-setmediatimes.md) method. For more information, see [Time in DirectShow Editing Services](time-in-directshow-editing-services.md).

To get frame-accurate cuts and transitions, set the *Start* and *Stop* parameters to frame boundaries. You can use the [**IAMTimelineObj::FixTimes**](iamtimelineobj-fixtimes.md) method to convert a time value into the nearest frame boundary, or use the following function to convert from frame number to reference time:


```C++
REFERENCE_TIME inline FrameNumToTime(LONGLONG frame, double fps)
{
    double dt = (frame * 10000000 / fps);
    if (frame >= 0) 
    {
        dt += 0.5;    }
    else
    {
        dt -= 0.5;
    }
    return (REFERENCE_TIME)dt;
}
```



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

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




