---
description: Setting and Retrieving the Position
ms.assetid: 06b0e2d7-9539-41ad-a631-7e8da556feeb
title: Setting and Retrieving the Position
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting and Retrieving the Position

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The filter graph maintains two position values, current position and stop position. These are defined as follows:

-   When the graph is running, the current position is the current playback position, relative to the beginning of the source. When the graph is stopped or paused, the current position is the point where streaming will begin on the next run command.
-   The stop position is the point where the stream will end. When the graph reaches the stop position, no more data is streamed, and the filter graph manager posts an [**EC\_COMPLETE**](ec-complete.md) event. (The graph does not automatically switch to a stopped state, however. For more information, see [Responding to Events](responding-to-events.md).)

To retrieve these values, call the [**IMediaSeeking::GetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getpositions) method. The returned values are always relative to the original media source. By default, the values are in reference time units. In some cases, you can change the time units; for more information, see [Time Formats For Seek Commands](time-formats-for-seek-commands.md).

To seek to a new position or set a new stop position, call the [**IMediaSeeking::SetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setpositions) method, as shown in the following example:


```C++
#define ONE_SECOND 10000000
REFERENCE_TIME rtNow  = 2 * ONE_SECOND, 
               rtStop = 5 * ONE_SECOND;

hr = pSeek->SetPositions(
    &rtNow,  AM_SEEKING_AbsolutePositioning, 
    &rtStop, AM_SEEKING_AbsolutePositioning
    );
```



> [!Note]  
> One second is 10,000,000 units of reference time. For convenience, the example defines this value as ONE\_SECOND. If you are using the DirectShow base-class library, the constant UNITS has the same value.

 

The *rtNow* parameter specifies the new current position. The second parameter is a flag that defines how to interpret *rtNow*. In this example, the AM\_SEEKING\_AbsolutePositioning flag indicates that *rtNow* specifies an absolute position in the source. Therefore, the filter graph will seek to a position two seconds from the start of the stream. The *rtStop* parameter gives the stop time. The last parameter specifies that *rtStop* is also an absolute position.

To specify a position relative to the previous position value, use the AM\_SEEKING\_RelativePositioning flag. To leave one of the position values unchanged, use the AM\_SEEKING\_NoPositioning flag. The corresponding time parameter can be **NULL** in that case. The following example seeks forward by 10 seconds but leaves the stop position unchanged:


```C++
REFERENCE_TIME rtNow = 10 * ONE_SECOND;
hr = pSeek->SetPositions(
    &rtNow, AM_SEEKING_RelativePositioning, 
    NULL, AM_SEEKING_NoPositioning
    );
```



If the filter graph is stopped, the video renderer does not update the image after a seek operation. To the user, it will appear as if the seek did not happen. To update the image, pause the graph after the seek operation. Pausing the graph cues a new video frame for the video renderer. You can use the [**IMediaControl::StopWhenReady**](/windows/desktop/api/Control/nf-control-imediacontrol-stopwhenready) method, which pauses the graph and then stops it.

 

 



