---
description: The SetMediaTimes method sets the media stop and start times.
ms.assetid: 9fa7938c-8128-4c26-a738-771d57b315b5
title: IAMTimelineSrc::SetMediaTimes method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.SetMediaTimes
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::SetMediaTimes method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetMediaTimes` method sets the media stop and start times.

## Syntax


```C++
HRESULT SetMediaTimes(
   REFERENCE_TIME Start,
   REFERENCE_TIME Stop
);
```



## Parameters

<dl> <dt>

*Start* 
</dt> <dd>

Media start time, in 100-nanosecond units.

</dd> <dt>

*Stop* 
</dt> <dd>

Media stop time, in 100-nanosecond units.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The media times are the stop and start times relative to the original media file. Always set the media times when you add a video or audio source to the timeline. Otherwise, rendering problems might occur. The stop time must be greater than the start time.

To use a still frame from a video source, set the stop time to a fractional amount more than the start time, such as 100 nanoseconds. Setting them to the same value causes a rendering error.

If the timeline duration does not match the media duration, the source stretches or shrinks accordingly. This causes the clip to play slower or faster than the authored rate. (Pitch shifting will occur in an audio source.) For more information, see [Time in DirectShow Editing Services](time-in-directshow-editing-services.md).

You can specify the duration of the source file by calling the [**SetMediaLength**](iamtimelinesrc-setmedialength.md) method. If you set a media stop time that exceeds the duration, DES truncates the stop time.

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

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




