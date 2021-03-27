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
ms.date: 05/31/2018
---

# Player.ModeChange event

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

 

 





