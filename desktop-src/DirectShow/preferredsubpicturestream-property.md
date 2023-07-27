---
description: The PreferredSubpictureStream property retrieves the preferred subpicture stream for the current viewing session.
ms.assetid: 9c15dc6f-c016-41bf-b03d-e8e5415215ae
title: PreferredSubpictureStream Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PreferredSubpictureStream Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PreferredSubpictureStream` property retrieves the preferred subpicture stream for the current viewing session.

``` syntax
[iStream = ] MSWebDVD.PreferredSubpictureStream
```

## Return Value

Returns an Integer value representing the current preferred subpicture stream in the system registry.

## Remarks

The preferred subpicture stream is set with [MSDVDAdm](msdvdadm-object.md) object's [**DefaultSubpictureLCID**](defaultsubpicturelcid-property.md).

 

 



