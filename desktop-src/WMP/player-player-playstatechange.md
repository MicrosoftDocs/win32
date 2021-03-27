---
title: Player.PlayStateChange event
description: The PlayStateChange event occurs when there is a change in the playState property.
ms.assetid: d4c4b114-04b6-4079-b6a2-52b336fc6dc1
keywords:
- PlayStateChange event Windows Media Player
- PlayStateChange event Windows Media Player , Player class
- Player class Windows Media Player , PlayStateChange event
topic_type:
- apiref
api_name:
- Player.PlayStateChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.PlayStateChange event

The **PlayStateChange** event occurs when there is a change in the **playState** property.

## Syntax


```JScript
Player.PlayStateChange(
  NewState
)
```



## Parameters

<dl> <dt>

*NewState* 
</dt> <dd>

Number (**long**) which specifies the new **playState**. See [playState](player-playstate.md) for a table of possible values.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

Windows Media Player states are not guaranteed to occur in any particular order. Furthermore, not every state necessarily occurs during a sequence of events. You should not write code that relies upon state order.

## Examples

The following example demonstrates an event handler for the *Player*.**playStateChange** event. An HTML text element, named "myText", displays the new play state. The player object was created with ID = "Player".


```JScript
<SCRIPT LANGUAGE = "JScript"  FOR = Player EVENT = playStateChange(NewState)>

// Test for the player current state, display a message for each.
switch (NewState){
    case 1:
        myText.value = "Stopped";
        break;

    case 2:
        myText.value = "Paused";
        break;

    case 3:
        myText.value = "Playing";
        break;

    // Other cases go here.

    default:
        myText.value = "";
}
</SCRIPT>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.playState**](player-playstate.md)
</dt> </dl>

 

 





