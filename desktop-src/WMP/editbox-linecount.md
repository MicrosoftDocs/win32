---
title: EDITBOX.lineCount
description: The lineCount attribute retrieves the number of lines in the edit box control.
ms.assetid: 8922aa4a-2b39-431d-b876-82fd368df17a
keywords:
- EDITBOX.lineCount Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.lineCount
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EDITBOX.lineCount

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **lineCount** attribute retrieves the number of lines in the edit box control.

``` syntax
        elementID.lineCount
```

## Possible Values

This attribute is a read-only **Number** (**long**).

## Remarks

This attribute is useful only when **editStyle** is set to "multiline".

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**EDITBOX Element**](editbox-element.md)
</dt> <dt>

[**EDITBOX.editStyle**](editbox-editstyle.md)
</dt> </dl>

 

 





