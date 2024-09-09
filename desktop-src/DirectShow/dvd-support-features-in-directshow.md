---
description: DVD Support Features in DirectShow
ms.assetid: 20dc1067-696e-4f53-9c77-0f2da237c5af
title: DVD Support Features in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Support Features in DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The functionality of the [DVD Navigator](dvd-navigator-filter.md) filter is exposed through two interfaces, [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2), which provides the "set" methods for the DVD Navigator, and [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2), which provides the "get" methods.

The DVD Navigator supports the following features:

-   Karaoke support: You can write a DVD-karaoke application using the DVD Navigator. (This requires a compatible decoder.)
-   Simplified access to DVD text information strings: The DVD Navigator parses these strings and enables applications to easily enumerate, identify, and retrieve them.
-   Audio volume control through [**IBasicAudio**](/windows/desktop/api/Control/nn-control-ibasicaudio)
-   Support for customizing the DVD Navigator's behavior when the Stop command is issued: Applications can instruct the DVD Navigator to either resume from the current location when restarting the filter graph, or start play from the beginning of the disc.
-   Digital Theater Systems (DTS) and Sony Dynamic Digital Sound (SDDS) audio support. DTS and SDDS audio streams are recognized by the DVD Navigator and passed to the audio decoder. (A third-party DTS-compatible or SDDS-compatible decoder is required to decode and play the audio.)
-   Improved support for parental level changes: The DVD Navigator enables an application to accept, reject, or ignore parental level change commands from the disc.
-   Advanced options for managing the state of the DVD Navigator and synchronizing commands
-   Support for frame stepping, frame-accurate seeking, and reverse play. These features require a video decoder that supports them.
-   The ability to save the current location in a title and return to it at any time.
-   Simplified support for time events in non-sequential PGC titles: For non-sequential PGC titles, the DVD Navigator relays the raw time code information to the application.
-   Time code information. The [**DVD\_HMSF\_TIMECODE**](/windows/win32/api/strmif/ns-strmif-dvd_hmsf_timecode) structure can be used in place of the binary coded decimal (BCD) format. **DVD\_HMSF\_TIMECODE** contains easily accessed members for hours, minutes, seconds, and frames, and can be cast to/from a **ULONG**.
-   The ability to control whether the filter graph flushes after a seek operation: The graph buffers can contain up to a few seconds of video at any given time. You can instruct the graph to either finish playing the buffered video after a seek, or begin playing immediately at the new location.
-   The ability to set values in general parameter registers: An advanced feature for those familiar with the DVD specification who wish to implement advanced functionality.
-   The ability to generate numeric disc identifiers that are for all practical purposes unique

### What Background Do I Need to Write a DVD Application?

All application developers should have a basic familiarity with the features provided by DVD technology such as parental management levels, multiple audio and subpicture streams, and angle blocks. [DVD Basics](dvd-basics.md) briefly describes each of these features; more complete descriptions are available in third-party publications. You don't need to refer to the DVD specification unless you intend to implement advanced features beyond the Annex J command set.

C/C++ developers using DirectShow should be familiar with COM client programming techniques such as creating COM objects and obtaining and releasing COM interface pointers. You might also need a general knowledge of filter graph operations, because you might need to access and manipulate the graph directly.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



