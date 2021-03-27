---
title: Player.MouseUp event
description: The MouseUp event occurs when the user releases a mouse button. | Player.MouseUp event
ms.assetid: 0f209fc4-2aad-46b1-84ba-2bfbecbe2930
keywords:
- MouseUp event Windows Media Player
- MouseUp event Windows Media Player , Player class
- Player class Windows Media Player , MouseUp event
topic_type:
- apiref
api_name:
- Player.MouseUp
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MouseUp event

The **MouseUp** event occurs when the user releases a mouse button.

## Syntax


```JScript
Player.MouseUp(
  nButton,
  nShiftState,
  fX,
  fY
)
```



## Parameters

<dl> <dt>

*nButton* 
</dt> <dd>

**Number** (**int**) specifying a bitfield with bits corresponding to the left button (bit 0), right button (bit 1), and middle button (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Only one of the bits is set, indicating the button that caused the event.

</dd> <dt>

*nShiftState* 
</dt> <dd>

**Number** (**int**) specifying a bitfield with the least significant bits corresponding to the SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. The shift argument indicates the state of these keys. Some, all, or none of the bits can be set, indicating that some, all, or none of the keys are pressed.

</dd> <dt>

*fX* 
</dt> <dd>

**Number** (**long**) specifying the x coordinate of the mouse pointer relative to the upper-left corner of the control.

</dd> <dt>

*fY* 
</dt> <dd>

**Number** (**long**) specifying the y coordinate of the mouse pointer relative to the upper-left corner of the control.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

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

 

 





