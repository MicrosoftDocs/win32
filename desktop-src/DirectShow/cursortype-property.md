---
description: The CursorType property sets or retrieves the current cursor type.
ms.assetid: f362e790-a7c7-4fb6-86f3-7cd25f78fe0e
title: CursorType Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CursorType Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CursorType` property sets or retrieves the current cursor type.

``` syntax
[ iCursorType = ] MSWebDVD.CursorType
```

## Return Value

Returns an integer value representing the cursor type.

## Remarks

The possible values for this property are:



| Value | Description |
|-------|-------------|
| 0     | Arrow       |
| 1     | Zoom In     |
| 2     | Zoom Out    |
| 3     | Hand        |
| -1    | None        |



 

This property is read/write with a default value of zero. When the picture is zoomed in, setting `CursorType` to **Hand** (0x3) puts the application into drag mode, enabling the user to move the image inside the video display area.

 

 



