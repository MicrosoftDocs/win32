---
title: VIDEO.fullScreen
description: The fullScreen attribute specifies or retrieves a value indicating whether the video is displayed in full-screen mode.
ms.assetid: de74d95a-31a2-4f65-811c-4e8018ee484a
keywords:
- VIDEO.fullScreen Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.fullScreen
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIDEO.fullScreen

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **fullScreen** attribute specifies or retrieves a value indicating whether the video is displayed in full-screen mode.

``` syntax
        elementID.fullScreen
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                          |
|-------|------------------------------------------------------|
| true  | Video displays in full-screen mode.                  |
| false | Default. Video does not display in full-screen mode. |



 

## Remarks

This property can be specified only at run time, after a file has been loaded. It must therefore be set within a script event handler. The escape button is used to return to normal viewing.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIDEO Element**](video-element.md)
</dt> <dt>

[**VIDEO.maintainAspectRatio**](video-maintainaspectratio.md)
</dt> <dt>

[**VIDEO.shrinkToFit**](video-shrinktofit.md)
</dt> <dt>

[**VIDEO.stretchToFit**](video-stretchtofit.md)
</dt> </dl>

 

 





