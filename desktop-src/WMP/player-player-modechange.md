---
title: Player.ModeChange event
description: The ModeChange event occurs when a mode of Windows Media Player is changed. | Player.ModeChange event
ms.assetid: 45b57660-b186-4c0f-8735-61134058b8c9
keywords:
- ModeChange event Windows Media Player
- ModeChange event Windows Media Player , Player class
- Player class Windows Media Player , ModeChange event
topic_type:
- apiref
api_name:
- Player.ModeChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.ModeChange event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ModeChange** event occurs when a mode of Windows Media Player is changed.

## Syntax


```JScript
Player.ModeChange(
  ModeName,
  NewValue
)
```



## Parameters

<dl> <dt>

*ModeName* 
</dt> <dd>

**String** indicating the mode that was changed. Contains one of the following values.



| Value   | Description                                         |
|---------|-----------------------------------------------------|
| shuffle | Tracks are played in random order.                  |
| loop    | The entire sequence of tracks is played repeatedly. |



 

</dd> <dt>

*NewValue* 
</dt> <dd>

**Boolean** indicating the new state of the specified mode.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Settings.getMode**](settings-getmode.md)
</dt> <dt>

[**Settings.setMode**](settings-setmode.md)
</dt> </dl>

 

 





