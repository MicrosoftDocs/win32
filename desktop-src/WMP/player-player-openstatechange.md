---
title: Player.OpenStateChange event
description: The OpenStateChange event occurs when the openState property changes value. | Player.OpenStateChange event
ms.assetid: b6b840ab-72c7-4150-a259-1e7d8afcec81
keywords:
- OpenStateChange event Windows Media Player
- OpenStateChange event Windows Media Player , Player class
- Player class Windows Media Player , OpenStateChange event
topic_type:
- apiref
api_name:
- Player.OpenStateChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.OpenStateChange event

The **OpenStateChange** event occurs when the **openState** property changes value.

## Syntax


```JScript
Player.OpenStateChange(
  NewState
)
```



## Parameters

<dl> <dt>

*NewState* 
</dt> <dd>

**Number** (**long**) specifying the new open state. See [openState](player-openstate.md) for a table of values.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Windows Media Player can go through several open states while it attempts to open a network file, such as locating the server, connecting to the server, and finally opening the file. This event will be fired each time the open state changes.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

Windows Media Player states are not guaranteed to occur in any particular order. Furthermore, not every state necessarily occurs during a sequence of events. You should not write code that relies upon state order.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.openState**](player-openstate.md)
</dt> </dl>

 

 





