---
description: The CursorType property sets or retrieves the current cursor type.
ms.assetid: f362e790-a7c7-4fb6-86f3-7cd25f78fe0e
title: CursorType Property
ms.topic: reference
ms.date: 05/31/2018
---

# CursorType Property

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

 

 



