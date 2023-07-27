---
description: The CurrentDomain property retrieves the DVD domain that the MSWebDVD object is in.
ms.assetid: 9d545438-9a3d-4c57-a3df-5e75af2e4d1b
title: CurrentDomain Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CurrentDomain Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentDomain` property retrieves the DVD domain that the MSWebDVD object is in.

``` syntax
[ iDomain = ] MSWebDVD.CurrentDomain
```

## Return Value

Returns an integer value representing the current domain.

## Remarks

The possible values of the property are:



| Value | Description          |
|-------|----------------------|
| 1     | First play           |
| 2     | Video Manager Menu   |
| 3     | Video Title Set Menu |
| 4     | Title                |
| 5     | Stop                 |



 

Call this method to ensure that the DVD Navigator is in a valid domain for the method you are about to call. For example, before calling [**PlayTitle**](playtitle-method.md), check the `CurrentDomain` property to make sure that the DVD Navigator is not in the Stop or First Play domain.

 

 



