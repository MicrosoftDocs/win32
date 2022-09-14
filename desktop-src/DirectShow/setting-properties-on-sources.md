---
description: Setting Properties on Sources
ms.assetid: fa1c7c40-915b-4577-aa33-6bd06707d93a
title: Setting Properties on Sources
ms.topic: article
ms.date: 05/31/2018
---

# Setting Properties on Sources

\[This API is not supported and may be altered or unavailable in the future.\]

When you create a new source object, there are a few properties you are required to set and others you can optionally set. You must set the following properties.

-   The start and stop times, relative to the rest of the timeline. Call the [**IAMTimelineObj::SetStartStop**](iamtimelineobj-setstartstop.md) method. Do not set overlapping times on source objects within the same track, or it will cause undefined behavior.
-   The media file to use as a source clip. Call the [**IAMTimelineSrc::SetMediaName**](iamtimelinesrc-setmedianame.md).
-   The media start and stop times, relative to the original source file. Call the [**IAMTimelineSrc::SetMediaTimes**](iamtimelinesrc-setmediatimes.md) method. Exception: If the source is a still image, do not specify the media times. For more information about media times, see [Time in DirectShow Editing Services](time-in-directshow-editing-services.md).

A source object inherits its media type from the parent group, so it is not necessary to specify a media type.

Optional properties include the following:

-   The stretch mode. The stretch mode specifies how Microsoft® DirectShow® Editing Services (DES) renders a source whose size does not match the output dimensions. By default, DES stretches an image without preserving the aspect ratio. Alternatively, DES can crop an image or create a letterbox. Call the [**IAMTimelineSrc::SetStretchMode**](iamtimelinesrc-setstretchmode.md) method to specify the stretch mode.
-   The duration of the source file. If you set this property before setting the media times, DES validates the media stop time and truncates the stop time if it exceeds the file duration. This can help avoid rendering errors later. You can obtain the duration of the file using the media detector, as described in [Using the Media Detector](using-the-media-detector.md). Call the [**IAMTimelineSrc::SetMediaLength**](iamtimelinesrc-setmedialength.md) method to specify the file duration.
-   The stream number. By default, a source object uses the first stream in the file that matches the media type of the parent group. If a file contains two or more streams of the same media type, select which stream to use by calling [**IAMTimelineSrc::SetStreamNumber**](iamtimelinesrc-setstreamnumber.md). You can use the media detector to find the number of streams.

## Related topics

<dl> <dt>

[Working with Sources](working-with-sources.md)
</dt> </dl>

 

 



