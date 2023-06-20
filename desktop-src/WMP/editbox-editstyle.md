---
title: EDITBOX.editStyle
description: The editStyle attribute specifies or retrieves the style of the edit box control.
ms.assetid: 1b3052c4-3087-4d41-af03-d7758680cc3b
keywords:
- EDITBOX.editStyle Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.editStyle
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EDITBOX.editStyle

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **editStyle** attribute specifies or retrieves the style of the edit box control.

``` syntax
        elementID.editStyle
```

## Possible Values

This attribute is a read/write **String** containing one of the following values.



| Value     | Description                                                                     |
|-----------|---------------------------------------------------------------------------------|
| normal    | Default. Displays normal text on a single line.                                 |
| password  | Displays asterisks (\*) in place of text. Can only be specified at design time. |
| uppercase | Displays text as all uppercase.                                                 |
| lowercase | Displays text as all lowercase.                                                 |
| number    | Only displays numbers.                                                          |
| multiline | Displays multiple lines of text. Can only be specified at design time.          |



 

## Remarks

This attribute can only be set to "password" or "multiline" at design time. If it is set to "multiline", the value cannot be changed at run time.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**EDITBOX Element**](editbox-element.md)
</dt> </dl>

 

 





