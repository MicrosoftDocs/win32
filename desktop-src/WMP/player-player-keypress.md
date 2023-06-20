---
title: Player.KeyPress event
description: The KeyPress event occurs when a key is pressed and released. | Player.KeyPress event
ms.assetid: fc51dfd3-7968-464a-a4e2-669ffcb52a59
keywords:
- KeyPress event Windows Media Player
- KeyPress event Windows Media Player , Player class
- Player class Windows Media Player , KeyPress event
topic_type:
- apiref
api_name:
- Player.KeyPress
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.KeyPress event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **KeyPress** event occurs when a key is pressed and released.

## Syntax


```JScript
Player.KeyPress(
  nKeyAscii
)
```



## Parameters

<dl> <dt>

*nKeyAscii* 
</dt> <dd>

**Number** (**int**) specifying the standard numeric ANSI code for the character.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event occurs when the keystroke results in any printable keyboard character, the CTRL key combined with a character from the standard alphabet or one of a few special characters, and the ENTER or BACKSPACE key.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





