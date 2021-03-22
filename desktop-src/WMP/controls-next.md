---
title: Controls.next method
description: The next method sets the current item to the next item in the playlist.
ms.assetid: 67436c76-8fb9-4350-86f3-67f5e9e6dca1
keywords:
- next method Windows Media Player
- next method Windows Media Player , Controls class
- Controls class Windows Media Player , next method
topic_type:
- apiref
api_name:
- Controls.next
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.next method

The **next** method sets the current item to the next item in the playlist.

## Syntax


```JScript
Controls.next()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If the playlist is on the last entry when **next** is invoked, the first entry in the playlist will become the current one.

For server-side playlists, this method skips to the next item in the server-side playlist, not the client playlist.

When playing a DVD, this method skips to the next logical chapter in the playback sequence, which may not be the next chapter in the playlist. When playing DVD stills, this method skips to the next still.

## Examples

The following example creates an HTML BUTTON element that uses **next** to move to the next item in the current playlist. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "NEXT"  NAME = "NEXT"  VALUE = ">>|"
    onClick = "

        /* Check first to be sure the operation is valid. */
        if (Player.controls.isAvailable('Next'))

            /* Move to the next item in the playlist. */
            Player.controls.next();
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

[**Controls.previous**](controls-previous.md)
</dt> <dt>

[**Controls.stop**](controls-stop.md)
</dt> </dl>

 

 





