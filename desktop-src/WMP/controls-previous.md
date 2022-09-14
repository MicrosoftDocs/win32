---
title: Controls.previous method
description: The previous method sets the current item to the previous item in the playlist.
ms.assetid: 09f83306-5e82-4384-ad28-38e406a401d8
keywords:
- previous method Windows Media Player
- previous method Windows Media Player , Controls class
- Controls class Windows Media Player , previous method
topic_type:
- apiref
api_name:
- Controls.previous
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.previous method

The **previous** method sets the current item to the previous item in the playlist.

## Syntax


```JScript
Controls.previous()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If the playlist is on the first entry when **previous** is invoked, the last entry in the playlist will become the current one.

## Examples

The following example creates an HTML BUTTON element that uses **previous** to move to the preceding item in the current playlist. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "PREV"  NAME = "PREV"  VALUE = "|<<"
    onClick = "

        /* Check first to be sure the operation is valid. */
        if (Player.controls.isAvailable('Previous'))

            /* Move to the preceding item in the playlist. */
            Player.controls.previous();
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
</dt> <dt>

[**Controls.next**](controls-next.md)
</dt> <dt>

[**Controls.stop**](controls-stop.md)
</dt> </dl>

 

 





