---
title: EFFECTS.fullScreen
description: The fullScreen attribute specifies or retrieves a value indicating whether the current visualization is displayed full-screen. This attribute can only be set at run time.
ms.assetid: 319b46a4-b6c2-4dda-8285-f12af6836b25
keywords:
- EFFECTS.fullScreen Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.fullScreen
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EFFECTS.fullScreen

The **fullScreen** attribute specifies or retrieves a value indicating whether the current visualization is displayed full-screen. This attribute can only be set at run time.

``` syntax
        elementID.fullScreen
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                          |
|-------|------------------------------------------------------|
| true  | Visualization is displayed full-screen.              |
| false | Default. Visualization is not displayed full-screen. |



 

## Remarks

A visualization can be put into full-screen mode only while media is playing or paused. If *Player*.**currentMedia** is video, a video plug-in must be present. If it is audio, a visualization plug-in that supports full-screen display must be present.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> </dl>

 

 





