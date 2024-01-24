---
description: Playing Karaoke Audio Streams
ms.assetid: 1a8d0f42-35b8-4743-9ae7-619b99936f76
title: Playing Karaoke Audio Streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playing Karaoke Audio Streams

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The DVD Navigator can play DVD-Video discs with karaoke audio streams, but karaoke playback also requires a decoder that supports multichannel karaoke mixing. Specifically, the decoder must support the [**DVD Karaoke Property Set**](dvd-karaoke-property-set.md) (AM\_PROPERTY\_DVDKARAOKE).

Karaoke discs are a type of DVD-Video disc and have the same navigation structure. Songs are generally formatted as titles, and titles can be grouped into title sets based on performer, musical style, or other criteria. The main difference between karaoke and other types of DVD-Videos is the audio stream. Karaoke discs all contain multichannel audio, usually Dolby AC-3. Channels 0 and 1 always contain the background instrumental music, while channels 2 through 5 can each contain any combination of guide vocals, guide melodies, and sound effects. A karaoke application can control the volume and destination speaker for each auxiliary channel.

When the DVD Navigator detects karaoke content on a disc and goes into karaoke mode, it informs the decoder, which then should mute the upper three channels (the auxiliary channels) until any or all of them are explicitly turned on by an application. The basic tasks of a karaoke application are to:

1.  Determine the number of auxiliary channels and their contents using [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2) methods.
2.  Provide a user interface that displays the channel contents and enables users to turn any auxiliary channel on or off at any time, using [**IDvdControl2::SelectKaraokeAudioPresentationMode**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-selectkaraokeaudiopresentationmode).

These steps are illustrated in the DVD Sample application in DVDCore.cpp in the **GetAudioAttributes** method.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



