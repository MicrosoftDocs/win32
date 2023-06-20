---
description: The BackColor property sets or retrieves the color of the bars that appear around the edges of the video rectangle when the aspect ratio of the native video is not the same as that of the object's display area.
ms.assetid: 51576836-c648-4268-8475-0312dbd60963
title: BackColor Property (DirectShow)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BackColor Property (DirectShow)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `BackColor` property sets or retrieves the color of the bars that appear around the edges of the video rectangle when the aspect ratio of the native video is not the same as that of the object's display area.

``` syntax
[ iBackColor = ] MSWebDVD.BackColor
```

## Return Value

Returns an integer value representing the RGB values of the back color.

## Remarks

This property is read/write with a default value of off-black (0x100010).

 

 



