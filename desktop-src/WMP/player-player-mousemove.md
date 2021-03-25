---
title: Player.MouseMove event
description: The MouseMove event occurs when the mouse pointer is moved. | Player.MouseMove event
ms.assetid: 026928a3-25a6-4e67-837a-df71c05e49ee
keywords:
- MouseMove event Windows Media Player
- MouseMove event Windows Media Player , Player class
- Player class Windows Media Player , MouseMove event
topic_type:
- apiref
api_name:
- Player.MouseMove
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MouseMove event

The **MouseMove** event occurs when the mouse pointer is moved.

## Syntax


```JScript
Player.MouseMove(
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

**Number** (**int**) specifying a bitfield with bits corresponding to the left button (bit 0), right button (bit 1), and middle button (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Some, all, or none of the bits can be set, indicating that some, all, or none of the buttons are pressed.

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

 

 





