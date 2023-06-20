---
title: TEXT.scrollingDelay
description: The scrollingDelay attribute specifies or retrieves the time delay between scrolling movements.
ms.assetid: b965fe8f-c809-431f-b8fe-f7c3060068ac
keywords:
- TEXT.scrollingDelay Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.scrollingDelay
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.scrollingDelay

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **scrollingDelay** attribute specifies or retrieves the time delay between scrolling movements.

``` syntax
        elementID.scrollingDelay
```

## Possible Values

This attribute is a read/write **Number** (**int**) specifying the delay in milliseconds. It has a minimum value of 30, and a default value of 85. If a value less than the minimum is specified, the default is used.

## Remarks

If **scrolling** is set to false, **scrollingDelay** is ignored.

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

 

 





