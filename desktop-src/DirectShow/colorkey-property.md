---
description: The ColorKey property sets or retrieves the color key used in closed captioning.
ms.assetid: 4d4b38e6-bd29-4e16-8f82-a5da9312d272
title: ColorKey Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ColorKey Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ColorKey` property sets or retrieves the color key used in closed captioning.

``` syntax
[ iColorKey = ] MSWebDVD.ColorKey
```

## Return Value

Returns an integer value representing the color to use as a transparent background for closed-captioned text. The default value in 256 colors is magenta, and off-black in any other color depth.

## Remarks

This property is read/write. This property applies only to the closed-captions, if any exist, not to the subpicture stream.

 

 



