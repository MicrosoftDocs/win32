---
description: Adding a Source
ms.assetid: 8c5d1050-a696-4a5d-be68-806420d0cd78
title: Adding a Source
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Adding a Source

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

Create a source object the same way you create other timeline objects. Before inserting it into the timeline, however, you must specify at least the following properties on the source.

-   The start and stop times, relative to the timeline. Call the [**IAMTimelineObj::SetStartStop**](iamtimelineobj-setstartstop.md) method.
-   The media file to use as a source. Call the [**IAMTimelineSrc::SetMediaName**](iamtimelinesrc-setmedianame.md) method with a wide-character string representing the name of the file.
-   The media start and stop times, which are relative to the original file. Call the [**IAMTimelineSrc::SetMediaTimes**](iamtimelinesrc-setmediatimes.md) method. For more information about media times, see [Time in DirectShow Editing Services](time-in-directshow-editing-services.md).

In the following example, the source clip starts four seconds into the file. The media duration is 10 seconds, twice the length of the timeline duration, meaning the source will play at twice normal speed. The constant UNITS is defined as 10000000 (10^7) and equals one second.


```C++
pSourceObj->SetStartStop(0, 50000000)
BSTR bstrFile = SysAllocStringLen(OLESTR("C:\\example.avi"), 15);
pSource->SetMediaName(bstrFile); 
SysFreeString(bstrFile);
pSource->SetMediaTimes(40000000, 140000000);
```



> [!Note]  
> Currently, DES cannot simultaneously render more than 75 sources that were compressed with Video Compression Manager (VCM) codecs. Also, if the project as a whole contains more than 75 such sources, you must use dynamic reconnection or DES cannot preview the project. For more information, see [**IRenderEngine::SetDynamicReconnectLevel**](irenderengine-setdynamicreconnectlevel.md).

 

For more information about sources, see [Working with Sources](working-with-sources.md).

## Related topics

<dl> <dt>

[Constructing a Timeline](constructing-a-timeline.md)
</dt> </dl>

 

 



