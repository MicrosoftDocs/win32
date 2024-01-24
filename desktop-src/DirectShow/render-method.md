---
description: The Render method initializes the DVD filter graph.
ms.assetid: 910f1e3f-b3bb-498b-93da-3a974a3117e8
title: Render Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Render Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Render` method initializes the DVD filter graph.

``` syntax
MSWebDVD.Render(iRender = 0)
```

## Parameters

<dl> <dt>

<span id="iRender"></span><span id="irender"></span><span id="IRENDER"></span>*iRender*
</dt> <dd>

Specifies an integer value indicating whether the filter graph will be destroyed and rebuilt.



| Value | Description                                                                                         |
|-------|-----------------------------------------------------------------------------------------------------|
| 0     | The filter graph will not be destroyed and rebuilt if it already exists. This is the default value. |
| 1     | The filter graph will be destroyed and rebuilt if it already exists.                                |



 

</dd> </dl>

## Return Value

No return value.

## Remarks

The `Render` method enables the **MSWebDVD** object to fully initialize the underlying DirectShow filter graph on startup. This eliminates the slight delay that otherwise occurs when the user issues the first command to play a disc or show a menu. There is no case in which `Render` needs to be called before calling any other method. For example, if the application calls [**PlayTitle**](playtitle-method.md) before the filter graph has been initialized, the **MSWebDVD** object calls `Render` automatically before attempting to play the disc.

 

 



