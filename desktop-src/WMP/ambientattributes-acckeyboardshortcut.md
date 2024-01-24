---
title: AmbientAttributes.accKeyboardShortcut
description: The accKeyboardShortcut attribute specifies or retrieves a keyboard shortcut description for any element.
ms.assetid: f97cffc9-4e7c-4226-9e02-0ea7f84b7450
keywords:
- AmbientAttributes.accKeyboardShortcut Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.accKeyboardShortcut
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.accKeyboardShortcut

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **accKeyboardShortcut** attribute specifies or retrieves a keyboard shortcut description for any element.

``` syntax
        elementID.accKeyboardShortcut
```

## Possible Values

This attribute is a read/write **String** with a default value of "" (empty string). For the **BUTTON** element, this attribute has a default value of "Spacebar or Enter". For the **SLIDER** element, the default value is "Right/Up Arrow to increase, Left/Down Arrow to decrease".

## Remarks

This attribute is used for accessibility purposes. It allows a description of the keyboard shortcut for any element to be read aloud by a reader program. This attribute does not set the shortcut. The scripter must do that work.

This attribute also applies to button elements inside the button group control.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





