---
description: The EnableResetOnStop property sets or retrieves a value that determines how play will resume when the filter graph makes a transition from a stopped state.
ms.assetid: ff2e2756-e3f3-4ddb-b99d-5fa65ec67f6b
title: EnableResetOnStop Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EnableResetOnStop Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `EnableResetOnStop` property sets or retrieves a value that determines how play will resume when the filter graph makes a transition from a stopped state.

``` syntax
[ bEnableReset = ] MSWebDVD.EnableResetOnStop
```

## Return Value

Returns a Boolean value indicating where the MSWebDVD object will start playing again after the filter graph is stopped.

## Remarks

This property is read/write.

The possible values of this property are: with a default value of true.



| Value | Description                                                                                       |
|-------|---------------------------------------------------------------------------------------------------|
| true  | DVD Navigator will reset and start play from the beginning of the disc. This is the default value |
| false | DVD Navigator will resume play where it left off.                                                 |



 

 

 



