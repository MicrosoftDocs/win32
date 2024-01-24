---
title: EDITBOX.justification
description: The justification attribute specifies or retrieves the alignment of the text within the editbox control.
ms.assetid: e1b62381-3975-45d9-8c9c-1e30770cebdb
keywords:
- EDITBOX.justification Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.justification
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EDITBOX.justification

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **justification** attribute specifies or retrieves the alignment of the text within the editbox control.

``` syntax
        elementID.justification
```

## Possible Values

This attribute is a read/write **String** containing one of the following values.



| Value  | Description                                                        |
|--------|--------------------------------------------------------------------|
| Left   | Default. Aligns the text to the left edge of the edit box control. |
| Right  | Aligns the text to the right edge of the edit box control.         |
| Center | Aligns the text to the horizontal center of the edit box control.  |



 

## Remarks

There is a margin of two pixels.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**EDITBOX Element**](editbox-element.md)
</dt> </dl>

 

 





