---
title: SLIDER.useForegroundProgress
description: The useForegroundProgress attribute specifies or retrieves a value indicating whether the foreground progress bar will be used.
ms.assetid: 10f3b4d9-ba82-4e30-affa-50c15a809ed6
keywords:
- SLIDER.useForegroundProgress Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.useForegroundProgress
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.useForegroundProgress

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **useForegroundProgress** attribute specifies or retrieves a value indicating whether the foreground progress bar will be used.

``` syntax
        elementID.useForegroundProgress
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                              |
|-------|------------------------------------------|
| true  | Use foreground progress.                 |
| false | Default. Do not use foreground progress. |



 

## Remarks

This attribute allows the use of the **foregroundProgress** attribute, which is used primarily to track the download progress of a media file while simultaneously tracking the current play position of the file using the **value** attribute.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.foregroundProgress**](slider-foregroundprogress.md)
</dt> <dt>

[**SLIDER.value**](slider-value.md)
</dt> </dl>

 

 





