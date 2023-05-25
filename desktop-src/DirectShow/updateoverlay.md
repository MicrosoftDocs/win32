---
description: The UpdateOverlay event is sent when the overlay surface has been moved or resized or its color key has changed.
ms.assetid: '692cbd26-b7b3-4fa3-9157-ca96a33e3a1e'
title: UpdateOverlay (Ddraw.h)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# UpdateOverlay

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The **UpdateOverlay** event is sent when the overlay surface has been moved or resized or its color key has changed.

``` syntax
UpdateOverlay()
```

## Remarks

Applications should never be concerned about the overlay surface being resized or moved. This is all handled internally. But this event is also sent when the color key changes. That means that if an application is hosting MSWebDVD as a windowless control and displaying floating buttons on top of the video surface in full-screen mode, it should respond to this event by getting the new value of the **ColorKey** property so that it can draw the buttons properly.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ddraw.h</dt> </dl> |



 

 




