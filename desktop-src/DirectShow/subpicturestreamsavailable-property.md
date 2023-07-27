---
description: The SubpictureStreamsAvailable property retrieves the number of subpicture streams available in the current title.
ms.assetid: 6a6d9d15-2f56-47fc-a7bb-2cf33f384f41
title: SubpictureStreamsAvailable Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SubpictureStreamsAvailable Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SubpictureStreamsAvailable` property retrieves the number of subpicture streams available in the current title.

``` syntax
[ iStreams = ] MSWebDVD.SubpictureStreamsAvailable
```

## Return Value

Returns the number of available streams as an Integer.

## Remarks

This property is read-only with no default value. To query each stream for its language attribute, first call this method to get the upper bound.

Stream numbering is zero-based.

 

 



