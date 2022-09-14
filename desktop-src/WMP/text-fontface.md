---
title: TEXT.fontFace
description: The fontFace attribute specifies or retrieves the typeface for the Text control.
ms.assetid: 3b39e245-139a-4361-b678-0f9e962996b7
keywords:
- TEXT.fontFace Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.fontFace
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# TEXT.fontFace

The **fontFace** attribute specifies or retrieves the typeface for the Text control.

``` syntax
        elementID.fontFace
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

This attribute can be the name of any valid font available on Windows. Windows Media Player will not support installing fonts, so choose a font that you know will be on the intended system.

If the **fontFace** specified is not available on the user's system, the Text control defaults to the Windows system font.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.fontSize**](text-fontsize.md)
</dt> </dl>

 

 





