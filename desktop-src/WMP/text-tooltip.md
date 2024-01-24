---
title: TEXT.toolTip
description: The toolTip attribute specifies or retrieves the ToolTip text for the text control.
ms.assetid: 3e275607-e7ff-4424-8310-c628ede22629
keywords:
- TEXT.toolTip Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.toolTip
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.toolTip

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **toolTip** attribute specifies or retrieves the ToolTip text for the text control.

``` syntax
        elementID.toolTip
```

## Possible Values

This attribute is a read/write **String** with a maximum length of 1024 characters. It has no default value.

## Remarks

If this attribute is not specified, and the text in the **value** attribute is truncated in the Text control, or **wordWrap** is set to true, the ToolTip will display the full text of the **value** attribute.

When this attribute is set to "" (empty string), no ToolTip is displayed.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.value**](text-value.md)
</dt> <dt>

[**TEXT.wordWrap**](text-wordwrap.md)
</dt> </dl>

 

 





