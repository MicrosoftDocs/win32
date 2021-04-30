---
title: Player.close method
description: The close method releases Windows Media Player resources.
ms.assetid: '15bd5a05-dbfa-4bea-90c2-afd9f69631e0'
keywords:
- close method Windows Media Player
- close method Windows Media Player , Player class
- Player class Windows Media Player , close method
topic_type:
- apiref
api_name:
- Player.close
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.close method

The **close** method releases Windows Media Player resources.

## Syntax


```JScript
Player.close()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method closes the current digital media file, not Windows Media Player itself.

## Examples

The following example creates an HTML BUTTON element that, when clicked, stops playback in Windows Media Player and releases the resources in use. The **Player** object was created with ID = "Player".


```JScript
<INPUT  TYPE = "BUTTON"  ID = "CLOSEIT"  VALUE = "Close it"  onClick = "

        /* Close the Player object. */
        Player.close();
">

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

 

 





