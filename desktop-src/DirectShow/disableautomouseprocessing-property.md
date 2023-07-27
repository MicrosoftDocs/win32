---
description: The DisableAutoMouseProcessing property enables or disables the MSWebDVD object's mouse-processing functionality.
ms.assetid: d438deb8-3c6d-49c1-923b-d4c57e236fc9
title: DisableAutoMouseProcessing Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DisableAutoMouseProcessing Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DisableAutoMouseProcessing` property enables or disables the **MSWebDVD** object's mouse-processing functionality.

``` syntax
[ bMouseProcessing = ] MSWebDVD.DisableAutoMouseProcessing
```

## Return Value

Returns a boolean value indicating whether to disable the default mouse processing.

## Remarks

This property is read/write with a default value of false. The **MSWebDVD** object automatically handles mouse actions for DVD on-screen menus by default; users can highlight and activate menu buttons without special programming by the application. An application can turn off this default mouse-handling functionality by setting this property to **true**. When the automatic mouse processing is turned off, an application must use the various button-related methods and properties to handle mouse moves and mouse clicks on the on-screen menus. Also, an application can use the button-related methods to override the automatic mouse handling even when when `DisableAutoMouseProcessing` is set to **false**.

 

 



