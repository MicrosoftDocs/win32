---
description: The IAMTimelineSrc interface provides methods for manipulating and setting properties on source objects in DirectShow Editing Services (DES).
ms.assetid: 39a64718-1fac-4d90-8340-b712d3bad2ec
title: IAMTimelineSrc interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineSrc interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimelineSrc` interface provides methods for manipulating and setting properties on source objects in [DirectShow Editing Services](directshow-editing-services.md) (DES). A source object represents one stream from a media source.

You can use a portion of the data within a source file by setting the media start and media stop times. These values specify the beginning and end of the source object, relative to the original media source. The media times can differ from the object's start and stop times on the timeline, allowing for fast- or slow-motion playback. (With audio sources, pitch shifting occurs.)

To create a source object, call [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) with the value TIMELINE\_MAJOR\_TYPE\_SOURCE. You can query the returned [**IAMTimelineObj**](iamtimelineobj.md) pointer for the **IAMTimelineSrc** interface. For more information, see [Constructing a Timeline](constructing-a-timeline.md) and [Working with Sources](working-with-sources.md).

## Members

The **IAMTimelineSrc** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimelineSrc** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimelineSrc** interface has these methods.



| Method                                                    | Description                                                                                              |
|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [**FixMediaTimes**](iamtimelinesrc-fixmediatimes.md)     | Rounds the specified time values to the nearest frame boundary.<br/>                               |
| [**FixMediaTimes2**](iamtimelinesrc-fixmediatimes2.md)   | Rounds the specified time values, given as **REFTIME** values, to the nearest frame boundary.<br/> |
| [**GetDefaultFPS**](iamtimelinesrc-getdefaultfps.md)     | Retrieves the source object's default frame rate.<br/>                                             |
| [**GetMediaLength**](iamtimelinesrc-getmedialength.md)   | Retrieves the media length of this source object.<br/>                                             |
| [**GetMediaLength2**](iamtimelinesrc-getmedialength2.md) | Retrieves the media length of this source object, as a **REFTIME** value.<br/>                     |
| [**GetMediaName**](iamtimelinesrc-getmedianame.md)       | Retrieves the name of the source file represented by this source object.<br/>                      |
| [**GetMediaTimes**](iamtimelinesrc-getmediatimes.md)     | Retrieves the media start and stop times.<br/>                                                     |
| [**GetMediaTimes2**](iamtimelinesrc-getmediatimes2.md)   | Retrieves the media start and stop times, as **REFTIME** values.<br/>                              |
| [**GetStreamNumber**](iamtimelinesrc-getstreamnumber.md) | Retrieves the current stream number for the source object.<br/>                                    |
| [**GetStretchMode**](iamtimelinesrc-getstretchmode.md)   | Retrieves the stretch mode of a video source.<br/>                                                 |
| [**IsNormalRate**](iamtimelinesrc-isnormalrate.md)       | Indicates whether the clip will play at the normal playback rate.<br/>                             |
| [**ModifyStopTime**](iamtimelinesrc-modifystoptime.md)   | Sets the stop time, relative to the timeline.<br/>                                                 |
| [**ModifyStopTime2**](iamtimelinesrc-modifystoptime2.md) | Sets the stop time, as a **REFTIME** value.<br/>                                                   |
| [**SetDefaultFPS**](iamtimelinesrc-setdefaultfps.md)     | Sets the source object's default frame rate.<br/>                                                  |
| [**SetMediaLength**](iamtimelinesrc-setmedialength.md)   | Specifies the duration of the source file.<br/>                                                    |
| [**SetMediaLength2**](iamtimelinesrc-setmedialength2.md) | Specifies the duration of the source file, as a **REFTIME** value.<br/>                            |
| [**SetMediaName**](iamtimelinesrc-setmedianame.md)       | Specifies the name of the source file represented by this source object.<br/>                      |
| [**SetMediaTimes**](iamtimelinesrc-setmediatimes.md)     | Sets the media stop and start times.<br/>                                                          |
| [**SetMediaTimes2**](iamtimelinesrc-setmediatimes2.md)   | Sets the media stop and start times, as **REFTIME** values.<br/>                                   |
| [**SetStreamNumber**](iamtimelinesrc-setstreamnumber.md) | Specifies which stream to read from the source file associated with this source object.<br/>       |
| [**SetStretchMode**](iamtimelinesrc-setstretchmode.md)   | Sets the stretch mode of a video source.<br/>                                                      |
| [**SpliceWithNext**](iamtimelinesrc-splicewithnext.md)   | Joins this source object to another source object.<br/>                                            |



 

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



 

 
