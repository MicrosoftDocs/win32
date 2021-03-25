---
title: Player.MediaChange event
description: The MediaChange event occurs when a media item changes. | Player.MediaChange event
ms.assetid: c4bdd2ae-c51f-4577-b762-bc84aaf52f76
keywords:
- MediaChange event Windows Media Player
- MediaChange event Windows Media Player , Player class
- Player class Windows Media Player , MediaChange event
topic_type:
- apiref
api_name:
- Player.MediaChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MediaChange event

The **MediaChange** event occurs when a media item changes.

## Syntax


```JScript
Player.MediaChange(
  Item
)
```



## Parameters

<dl> <dt>

*Item* 
</dt> <dd>

**Media** object representing the item that changed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Examples

The following JScript example uses an HTML DIV element, named MediaName, to display the name of the current media item. The code updates the text in the DIV with each occurrence of the **mediaChange** event. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for media change. -->
<SCRIPT FOR = "Player" EVENT = "mediaChange(Item)">
   // Test whether a valid currentMedia object exists.
   if (Player.currentMedia){
      // Display the name of the current media item.
      MediaName.innerHTML = Player.currentMedia.name;
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
</dt> </dl>

 

 





