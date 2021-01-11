---
description: The KaraokeAudioPresentationMode property sets or retrieves the right-left speaker mix for the auxiliary karaoke channels.
ms.assetid: f32706eb-7f97-433d-854a-17d57cc60190
title: KaraokeAudioPresentationMode Property
ms.topic: reference
ms.date: 05/31/2018
---

# KaraokeAudioPresentationMode Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `KaraokeAudioPresentationMode` property sets or retrieves the right-left speaker mix for the auxiliary karaoke channels.

``` syntax
[iMode ] = MSWebDVD.KaraokeAudioPresentationMode
```

## Return Value

Returns an integer value containing a set of bit flags indicating how the auxiliary karaoke channels are downmixed to the left and right speakers.

## Remarks

This property is read/write with a default value of zero.

Audio channels are zero-based, so channels 0 and 1 generally represent the right and left speaker channels and channels 2 through 4 are the three auxiliary karaoke channels. When the MSWebDVD object enters karaoke mode, it automatically mutes channels 2 and higher. Use bitwise **OR** operations to set the appropriate bit in order to send an auxiliary channel to the left speaker, right speaker, both speakers (both bits on), or to no speakers (both bits off). These bits are all off by default whenever the DVD Navigator enters karaoke mode. The value of the bits and their corresponding action is given in the following table.



| Value  | Description                            |
|--------|----------------------------------------|
| 0x0004 | Downmix Channel 2 to the left speaker  |
| 0x0008 | Downmix Channel 3 to the left speaker  |
| 0x0010 | Downmix Channel 4 to the left speaker  |
| 0x0400 | Downmix Channel 2 to the right speaker |
| 0x0800 | Downmix Channel 3 to the right speaker |
| 0x1000 | Downmix Channel 4 to the right speaker |



 

 

 



