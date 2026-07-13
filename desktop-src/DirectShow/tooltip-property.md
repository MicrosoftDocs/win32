---
description: The ToolTip property sets the text for the ToolTip that appears when the mouse pointer is over the MSWebDVD video rectangle.
ms.assetid: b71ec573-6585-4b0c-8171-9f9c8fdb7394
title: ToolTip Property (Windows.ui.xaml.controls.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ToolTip
api_type: 
- HeaderDef
api_location: 
- windows.ui.xaml.controls.h
ms.custom: UpdateFrequency5
---

# ToolTip Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ToolTip` property sets the text for the ToolTip that appears when the mouse pointer is over the **MSWebDVD** video rectangle.

``` syntax
[ sToolTip = ] MSWebDVD.ToolTip
```

## Return Value

Returns the ToolTip text as a String.

## Remarks

This property is read/write with no default value. If the string is empty, no ToolTip appears.

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Windows.ui.xaml.controls.h</dt> </dl> |



 

 




