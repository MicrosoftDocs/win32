---
description: The SaveBookmark method saves the current disc position and state of the MSWebDVD object so the user can return to the same place later.
ms.assetid: 975687c5-f93e-4473-b23b-63e0ae6bbb5d
title: SaveBookmark Method (Segment.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SaveBookmark Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SaveBookmark` method saves the current disc position and state of the **MSWebDVD** object so the user can return to the same place later.

``` syntax
MSWebDVD.SaveBookmark()
```

## Return Value

No return value.

## Remarks

A bookmark is a snapshot of the DVD Navigator's current state. This includes information such as where it is playing on the disc, and which audio and subpictures streams are selected. By saving a bookmark, the user can close the application, shut down the computer, and come back later to continue viewing the disc right where he or she left off, with all settings just as they were before. Only one bookmark can be saved at any given time. When you call `SaveBookmark`, the old bookmark is overwritten.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



## See also

<dl> <dt>

[**RestoreBookmark**](restorebookmark-method.md)
</dt> </dl>

 

 




