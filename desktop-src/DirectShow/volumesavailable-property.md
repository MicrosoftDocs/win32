---
description: The VolumesAvailable property retrieves the number of volumes in a multivolume set.
ms.assetid: d056b6d5-f4a4-480b-96a5-8e95dce23dfb
title: VolumesAvailable Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VolumesAvailable Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `VolumesAvailable` property retrieves the number of volumes in a multivolume set.

``` syntax
[ iVolumes = ] MSWebDVD.VolumesAvailable
```

## Return Value

Returns the number of volumes in the set as an Integer.

## Remarks

This property is read-only with no default value. Some DVD titles might be released as a multidisc set or series. Use this method to determine the volume number for the current disc.

 

 



