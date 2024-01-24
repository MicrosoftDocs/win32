---
title: TEXT.textWidth
description: The textWidth attribute retrieves the width in pixels of the text contained in the value attribute.
ms.assetid: 46c34659-f441-467c-8846-45785f7a2736
keywords:
- TEXT.textWidth Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.textWidth
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.textWidth

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **textWidth** attribute retrieves the width in pixels of the text contained in the **value** attribute.

``` syntax
        elementID.textWidth
```

## Possible Values

This attribute is a read-only **Number** (**int**).

## Remarks

The value returned is based on the **fontFace**, **fontSize**, and **fontStyle** attributes as well as on the actual characters in the **value** attribute string.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.fontFace**](text-fontface.md)
</dt> <dt>

[**TEXT.fontSize**](text-fontsize.md)
</dt> <dt>

[**TEXT.fontStyle**](text-fontstyle.md)
</dt> <dt>

[**TEXT.value**](text-value.md)
</dt> </dl>

 

 





