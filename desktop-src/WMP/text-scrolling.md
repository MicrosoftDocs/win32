---
title: TEXT.scrolling
description: The scrolling attribute specifies or retrieves a value indicating whether the text scrolls.
ms.assetid: 1cd5cb4e-673f-4273-91ff-50165c2b08fa
keywords:
- TEXT.scrolling Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.scrolling
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.scrolling

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **scrolling** attribute specifies or retrieves a value indicating whether the text scrolls.

``` syntax
        elementID.scrolling
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                     |
|-------|---------------------------------|
| true  | Scrolling is enabled.           |
| false | Default. Scrolling is disabled. |



 

## Remarks

The scrolling feature provides a two-space buffer between the end of the text and the beginning of the repeated line.

The **justification** attribute specifies where the text first appears before the scrolling begins.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.justification**](text-justification.md)
</dt> <dt>

[**TEXT.scrollingAmount**](text-scrollingamount.md)
</dt> <dt>

[**TEXT.scrollingDelay**](text-scrollingdelay.md)
</dt> <dt>

[**TEXT.scrollingDirection**](text-scrollingdirection.md)
</dt> </dl>

 

 





