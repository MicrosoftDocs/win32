---
title: Player.Error event
description: The Error event occurs when there is an error condition.
ms.assetid: 1e418a56-ae81-4ff0-b721-3390be08970d
keywords:
- Error event Windows Media Player
- Error event Windows Media Player , Player class
- Player class Windows Media Player , Error event
topic_type:
- apiref
api_name:
- Player.Error
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.Error event

The **Error** event occurs when there is an error condition.

## Syntax


```JScript
Player.Error()
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Examples

The following JScript example creates an event handler to display the description text for the first error in the error queue. The **Player** object was created with ID = "Player".


```JScript
<SCRIPT LANGUAGE = "JScript"  FOR = Player  EVENT = error()>

// Get the description of the first error. 
var errDesc = Player.error.item(0).errorDescription;

// Display the error description.
alert(errDesc);

</SCRIPT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem.errorDescription**](erroritem-errordescription.md)
</dt> <dt>

[**Error.item**](error-item.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





