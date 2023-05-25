---
title: EDITBOX.wordWrap
description: The wordWrap attribute specifies or retrieves a value indicating whether word wrap is enabled.
ms.assetid: 027817f0-e077-4db5-8216-f9a9f41fd210
keywords:
- EDITBOX.wordWrap Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.wordWrap
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EDITBOX.wordWrap

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **wordWrap** attribute specifies or retrieves a value indicating whether word wrap is enabled.

``` syntax
        elementID.wordWrap
```

## Possible Values

This attribute is a read/write **Boolean** with a default value of true.

## Remarks

This attribute is useful only when **editStyle** is set to "multiline".

If word wrap is disabled, and the text does not fit in the control, the text is truncated.

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

 

 





