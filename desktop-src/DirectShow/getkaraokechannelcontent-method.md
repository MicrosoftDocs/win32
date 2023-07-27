---
description: The GetKaraokeChannelContent method retrieves a value that indicates the type of content in the specified karaoke channel in the specified stream.
ms.assetid: e36a88b8-7184-44a4-8e02-204440f651bc
title: GetKaraokeChannelContent Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetKaraokeChannelContent Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetKaraokeChannelContent` method retrieves a value that indicates the type of content in the specified karaoke channel in the specified stream.

``` syntax
[ iContent = ] MSWebDVD.GetKaraokeChannelContent(iStream, iChannel)
```

## Parameters

<dl> <dt>

<span id="iStream"></span><span id="istream"></span><span id="ISTREAM"></span>*iStream*
</dt> <dd>

Specifies the audio stream as an Integer.

</dd> <dt>

<span id="iChannel"></span><span id="ichannel"></span><span id="ICHANNEL"></span>*iChannel*
</dt> <dd>

Specifies the channel as an Integer. The possible values for each channel are:



| Value  | Description    |
|--------|----------------|
| 0x0001 | Guide Vocal 1  |
| 0x0002 | Guide Vocal 2  |
| 0x0004 | Guide Melody 1 |
| 0x0008 | Guide Melody 2 |
| 0x0010 | Guide Melody A |
| 0x0020 | Guide Melody B |
| 0x0040 | Sound Effect A |
| 0x0080 | Sound Effect B |



 

</dd> </dl>

## Return Value

Returns an integer value whose individual bits specify the contents of the karaoke channel.

## Remarks

DVD audio channel numbering is zero-based, so channels 2, 3, and 4 are the auxiliary karaoke channels. After the method returns, perform a bitwise AND operation on *iContent* to determine the contents of each channel. Because a single channel might have more than one type of content recorded on it, you should test for all the possible values even after a match is found.

After the user knows the contents of each channel, he or she must be able to adjust the volume or turn the individual channels on or off as needed. Implement this functionality in your application by using the [**KaraokeAudioPresentationMode**](karaokeaudiopresentationmode-property.md) property.

> [!Note]  
> To play karaoke discs, the audio decoder on the user's system must be compatible with the DirectShow 8 karaoke implementation.

 

 

 



