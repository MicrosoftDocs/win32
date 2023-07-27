---
description: Audio and Subpicture Streams
ms.assetid: 8d361da3-a33a-401c-a750-f9b952022cf6
title: Audio and Subpicture Streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio and Subpicture Streams

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A DVD-Video disc can have up to eight audio streams, numbered zero through seven, each with up to six discrete channels. (Note that audio and subpicture streams are numbered from zero, whereas titles, angles, and parental levels are numbered from one.) Only one of these streams can be selected at any given time. For subpictures, up to 32 streams are available, although only one stream can be activated at any given time. Discs are generally authored with default audio and subpicture streams, but an application can enable users to view a list of all the available streams, and select the one in the language they prefer. The basic steps in this process are the same for both audio and subpicture streams.

1.  Determine the number of streams available for a title.
2.  Iterate through the streams and retrieve the stream attributes for each.
3.  Retrieve the language code from the returned locale identifier (LCID) and create a human-readable string.
4.  Populate a list box or other user interface (UI) control to enable the user to select a preferred stream.

In the DVD sample application, the CAudioLangDlg::MakeAudioStreamList method in Dialogs.cpp demonstrates the basic steps.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



