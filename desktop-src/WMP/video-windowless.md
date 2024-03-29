---
title: VIDEO.windowless
description: The windowless attribute specifies or retrieves a value indicating whether the Video control will be windowed or windowless; that is, whether the entire rectangle of the control will be visible at all times or can be clipped.
ms.assetid: d59e6baf-374b-48f6-b99f-35a83af7feb6
keywords:
- VIDEO.windowless Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.windowless
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIDEO.windowless

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **windowless** attribute specifies or retrieves a value indicating whether the Video control will be windowed or windowless; that is, whether the entire rectangle of the control will be visible at all times or can be clipped. Can only be set at design time.

``` syntax
        elementID.windowless
```

## Possible Values

This attribute is a **Boolean** specified at design time and read-only thereafter.



| Value | Description                              |
|-------|------------------------------------------|
| true  | Video control will be windowless.        |
| false | Default. Video control will be windowed. |



 

## Remarks

If a non-rectangular video window is desired, or if you want to cover any part of the video window with an image, this attribute must be set to true. This sacrifices some performance to do the necessary clipping.

Video playback is optimized for unclipped playback. In this case, the **windowless** attribute is set to false, and the entire video rectangle is always displayed. Any image covering the video window is ignored, and the video window has the highest-level z-order.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIDEO Element**](video-element.md)
</dt> </dl>

 

 





