---
title: Controls.currentPosition
description: The currentPosition property specifies or retrieves the current position in the media item in seconds from the beginning.
ms.assetid: 374ad144-3f74-4d1b-bec5-1cd0f03777b7
keywords:
- Controls.currentPosition Windows Media Player
topic_type:
- apiref
api_name:
- Controls.currentPosition
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.currentPosition

The **currentPosition** property specifies or retrieves the current position in the media item in seconds from the beginning.

``` syntax
player.controls.currentPosition
      
```

## Possible Values

This property is a read/write **Number** (**double**).

## Examples

The following example uses **currentPosition** to seek to a position provided by the user. An HTML BUTTON element is created to execute the JScript code. An HTML TEXT input element, named setPosition, was created to accept a value, in seconds, from the user. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "Set"  NAME = "Set"  VALUE = "Set Position"

    /* Check to be sure the TEXT element contains a valid value. */
    if (!isNaN(setPosition.value) && (setPosition.value != '))

    /* Set the current position when the user clicks the button. */
    onClick = "Player.controls.currentPosition = setPosition.value;
">
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> </dl>

 

 





