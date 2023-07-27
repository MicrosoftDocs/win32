---
description: The Eject method ejects or inserts a disc from or into the DVD drive.
ms.assetid: 855a19ee-97a6-4abd-872d-cc815d286582
title: Eject Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Eject Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Eject` method ejects or inserts a disc from or into the DVD drive.

``` syntax
        MSWebDVD.Eject()
```

## Return Value

No return value.

## Remarks

On some DVD drives, this method acts as a toggle, ejecting and inserting on alternate calls. This is hardware-dependent.

 

 



