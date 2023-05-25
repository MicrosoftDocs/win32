---
description: The Mute property turns the audio stream output on or off.
ms.assetid: 61ed2e28-ec6e-48ee-8640-29152b15c9ad
title: Mute Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Mute Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Mute` property turns the audio stream output on or off.

``` syntax
[ bMute = ] MSWebDVD.Mute
```

## Return Value

Returns a Boolean value indicating whether the audio stream should be muted.

## Remarks

This property is read/write with a default value of false.

 

 



