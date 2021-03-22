---
title: EDITBOX.fontFace
description: The fontFace attribute specifies or retrieves the font for text in the edit box control.
ms.assetid: 5fb5e6d2-8535-402e-9ca1-d43e334e94e3
keywords:
- EDITBOX.fontFace Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.fontFace
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EDITBOX.fontFace

The **fontFace** attribute specifies or retrieves the font for text in the edit box control.

``` syntax
        elementID.fontFace
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

This attribute can be the name of any valid font available in Windows. Windows Media Player will not support installing fonts, so choose a font that you know will be on the intended system.

If the **fontFace** specified is not available on the user's system, the edit box control defaults to the Windows system font. The default value for English-language systems is "Tahoma". For international systems, the default is loaded from a resource file.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**EDITBOX Element**](editbox-element.md)
</dt> <dt>

[**EDITBOX.fontSize**](editbox-fontsize.md)
</dt> <dt>

[**EDITBOX.fontStyle**](editbox-fontstyle.md)
</dt> </dl>

 

 





