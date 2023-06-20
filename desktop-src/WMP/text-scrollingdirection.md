---
title: TEXT.scrollingDirection
description: The scrollingDirection attribute specifies or retrieves the direction of the scrolling text.
ms.assetid: b7f6daf3-3180-4937-93e6-266d875dbbfd
keywords:
- TEXT.scrollingDirection Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.scrollingDirection
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.scrollingDirection

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **scrollingDirection** attribute specifies or retrieves the direction of the scrolling text.

``` syntax
        elementID.scrollingDirection
```

## Possible Values

This attribute is a read/write **String**.



| Value | Description                         |
|-------|-------------------------------------|
| Left  | Default. Scroll from right to left. |
| Right | Scroll from left to right.          |



 

## Remarks

If **scrolling** is set to false, **scrollingDirection** is ignored.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.scrolling**](text-scrolling.md)
</dt> </dl>

 

 





