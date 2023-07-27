---
description: The DVDAdm property provides access to the MSDVDAdm object that contains methods and properties for saving application and user information.
ms.assetid: eb73a851-7118-42f3-be99-1cf356d2e37a
title: DVDAdm Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVDAdm Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm` property provides access to the [MSDVDAdm](msdvdadm-object.md) object that contains methods and properties for saving application and user information.

``` syntax
        MSWebDVD.DVDAdm
```

## Remarks

This property is read-only with no default value. There is no need to create a separate reference to the **MSDVDAdm** object. To access the methods and properties of the object, use the `DVDAdm` property as shown in the following example.

## Examples


```VB
DVD.DVDAdm.DisableScreenSaver = true
```



 

 



