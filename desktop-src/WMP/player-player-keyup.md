---
title: Player.KeyUp event
description: The KeyUp event occurs when a key is released. | Player.KeyUp event
ms.assetid: 8b624374-403f-4d41-8481-5e94cee70861
keywords:
- KeyUp event Windows Media Player
- KeyUp event Windows Media Player , Player class
- Player class Windows Media Player , KeyUp event
topic_type:
- apiref
api_name:
- Player.KeyUp
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.KeyUp event

The **KeyUp** event occurs when a key is released.

## Syntax


```JScript
Player.KeyUp(
  nKeyCode,
  nShiftState
)
```



## Parameters

<dl> <dt>

*nKeyCode* 
</dt> <dd>

**Number** (**int**) specifying which physical key is pressed. For possible values, see [Player.KeyDown Event](player-player-keydown.md).

</dd> <dt>

*nShiftState* 
</dt> <dd>

**Number** (**int**) specifying a bitfield with the least significant bits corresponding to the SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. The shift argument indicates the state of these keys. Some, all, or none of the bits can be set, indicating that some, all, or none of the keys are pressed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





