---
title: Player.CurrentItemChange event
description: The CurrentItemChange event occurs when Controls.currentItem changes.
ms.assetid: e6f68aeb-d7e7-460b-adc9-647f28c678a1
keywords:
- CurrentItemChange event Windows Media Player
- CurrentItemChange event Windows Media Player , Player class
- Player class Windows Media Player , CurrentItemChange event
topic_type:
- apiref
api_name:
- Player.CurrentItemChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.CurrentItemChange event

The **CurrentItemChange** event occurs when *Controls*.**currentItem** changes.

## Syntax


```JScript
Player.CurrentItemChange()
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Examples

The following JScript example demonstrates an event handler for the *Player*.**currentItemChange** event. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an HTML text box to display the media item name. -->
<INPUT TYPE="TEXT" NAME="MEDIA">

<!-- Create an event handler. -->
<SCRIPT LANGUAGE = "JScript"  FOR = Player EVENT = currentItemChange()>

   // Display the name of the new media item.
   MEDIA.value = Player.currentMedia.name;

</SCRIPT>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls.currentItem**](controls-currentitem.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





