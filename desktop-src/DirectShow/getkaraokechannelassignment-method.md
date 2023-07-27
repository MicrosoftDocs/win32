---
description: The GetKaraokeChannelAssignment method retrieves a value that indicates how the karaoke channels are assigned to the speakers.
ms.assetid: 08e35fa6-fa1b-4f9f-8f56-d953c4422226
title: GetKaraokeChannelAssignment Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetKaraokeChannelAssignment Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetKaraokeChannelAssignment` method retrieves a value that indicates how the karaoke channels are assigned to the speakers.

``` syntax
[ iAssignment = ] MSWebDVD.GetKaraokeChannelAssignment(iStream)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the audio stream as an Integer.

</dd> </dl>

## Return Value

Returns an integer indicating the speaker assignment for the specified stream.



| Return code | Description                                                             |
|-------------|-------------------------------------------------------------------------|
| 2           | The stream is assigned to the left and right speakers.                  |
| 3           | The stream is assigned to the left, right, and middle speakers.         |
| 4           | The stream is assigned to the left, right, and audio1 speakers.         |
| 5           | The stream is assigned to the left, right, middle, and audio1 speakers. |
| 6           | The stream is assigned to the left, right, and audio2 speakers.         |
| 7           | The stream is assigned to the left, right, middle, and audio2 speakers. |



 

## See also

<dl> <dt>

[**KaraokeAudioPresentationMode**](karaokeaudiopresentationmode-property.md)
</dt> </dl>

 

 



