---
title: TEXT.scrollingAmount
description: The scrollingAmount attribute specifies or retrieves the number of pixels that the text moves during each scrolling movement.
ms.assetid: 46f74531-69dd-4505-8937-5b48b6e9be7b
keywords:
- TEXT.scrollingAmount Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.scrollingAmount
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.scrollingAmount

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **scrollingAmount** attribute specifies or retrieves the number of pixels that the text moves during each scrolling movement.

``` syntax
        elementID.scrollingAmount
```

## Possible Values

This attribute is a positive read/write **Number** (**int**) with a default value of 6.

## Remarks

For smooth scrolling, **scrollingAmount** should be small. For fast drawing with big gaps, the **scrollingAmount** should be larger. If **scrolling** ="false", **scrollingAmount** is ignored.

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

 

 





