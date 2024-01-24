---
description: Time Formats For Seek Commands
ms.assetid: d9c1b860-f75f-4886-95d6-c62e9e5b69eb
title: Time Formats For Seek Commands
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Time Formats For Seek Commands

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Many of the methods in the **IMediaSeeking** interface have parameters that express position values, such as current position or stop position. By default, these parameters are expressed in units of 100 nanoseconds, also called reference time. Any filter that can seek must support seeking by reference time. Some filters can seek using other units of time as well, such as seeking to a particular frame number, or seeking to a given byte offset within a stream. Each of these time units is called a time format, and is defined by a globally unique identifier (GUID). For a list of the time formats that are defined by DirectShow, see [**Time Format GUIDs**](time-format-guids.md). Third parties can also define GUIDs for custom time formats.

To determine whether the filters currently in the filter graph support a particular time format, call the [**IMediaSeeking::IsFormatSupported**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-isformatsupported) method. The method returns S\_OK if the format is supported. Otherwise, it returns S\_FALSE or an error code. If a format is supported, you can switch to that format by calling the [**IMediaSeeking::SetTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-settimeformat) method. If the **SetTimeFormat** method succeeds, subsequent seek commands are expressed using the new time format.

The follow example checks whether the graph supports seeking by frame number. If so, it seeks to frame number 20:


```C++
hr = pSeek->IsFormatSupported(&TIME_FORMAT_FRAME);
if (hr == S_OK)
{
    hr = pSeek->SetTimeFormat(&TIME_FORMAT_FRAME);
    if (SUCCEEDED(hr))
    {
        // Seek to frame number 20.
        LONGLONG rtNow = 20;
        hr = pSeek->SetPositions(
            &rtNow, AM_SEEKING_AbsolutePositioning, 
            0, AM_SEEKING_NoPositioning);
    }
}
```



Note that time formats only apply to seek commands. They do not affect graph playback or other actions.

 

 



