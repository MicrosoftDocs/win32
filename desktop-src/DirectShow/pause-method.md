---
description: The Pause method pauses playback at the current location.
ms.assetid: 0938c5ed-9046-4f1a-877a-c99235fbfb36
title: Pause Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Pause Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Pause` method pauses playback at the current location.

``` syntax
MSWebDVD.Pause()
```

## Return Value

No return value.

## Remarks

If playback is already paused, this method does nothing.

 

 



