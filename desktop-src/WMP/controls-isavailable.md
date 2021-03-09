---
title: Controls.isAvailable
description: The isAvailable property indicates whether a specified type of information is available or a specified action can be performed. | Controls.isAvailable
ms.assetid: d2bfaa67-eac9-4fc4-9424-636ddb4b35d6
keywords:
- Controls.isAvailable Windows Media Player
topic_type:
- apiref
api_name:
- Controls.isAvailable
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.isAvailable

The **isAvailable** property indicates whether a specified type of information is available or a specified action can be performed.

``` syntax
player.controls.isAvailable(
        name
        )
```

## Parameters

*name*

**String** containing one of the following values.



| String          | Description                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| currentItem     | Determines whether the user can set the **currentItem** property.                                                                                                 |
| currentMarker   | Determines whether the user can seek to a specific marker.                                                                                                        |
| currentPosition | Determines whether the user can seek to a specific position in the file. Some files do not support seeking.                                                       |
| fastForward     | Determines whether the file supports fast forwarding and whether that functionality can be invoked. Many file types (or live streams) do not support fastForward. |
| fastReverse     | Determines whether the file supports fastReverse and whether that functionality can be invoked. Many file types (or live streams) do not support fastReverse.     |
| next            | Determines whether the user can seek to the next entry in a playlist.                                                                                             |
| pause           | Determines whether the **pause** method is available.                                                                                                             |
| play            | Determines whether the **play** method is available.                                                                                                              |
| previous        | Determines whether the user can seek to the previous entry in a playlist.                                                                                         |
| step            | Determines whether the **step** method is available during playback.                                                                                              |
| stop            | Determines whether the **stop** method is available.                                                                                                              |



 

## Return Values

This method returns a **Boolean** value.

## Examples

The following example creates an HTML BUTTON element that seeks to the starting position of the current media item. The JScript code uses **isAvailable** to verify that the file supports the seek operation. The **Player** object was created with ID = "Player".


```JScript
<INPUT TYPE = "BUTTON"  ID = "START"  NAME = "START"  VALUE = "Seek To Zero"

    /* If supported, seek to position zero. */
    onClick = "if (Player.controls.isAvailable('CurrentPosition'))
        Player.controls.currentPosition = 0;
">
```



## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/>                               |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> </dl>

 

 





