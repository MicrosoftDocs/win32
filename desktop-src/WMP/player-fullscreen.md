---
title: Player.fullScreen
description: The fullScreen property specifies or retrieves a value indicating whether video content is played back in full-screen mode.
ms.assetid: 43eeeddd-13a6-44d8-9cff-a60e976fc189
keywords:
- Player.fullScreen Windows Media Player
topic_type:
- apiref
api_name:
- Player.fullScreen
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.fullScreen

The **fullScreen** property specifies or retrieves a value indicating whether video content is played back in full-screen mode.

## Syntax

*player* .**fullScreen**

## Possible Values

This property is a read/write **Boolean**.



| Value | Description                                                    |
|-------|----------------------------------------------------------------|
| true  | Video content is played back in full-screen mode.              |
| false | Default. Video content is not played back in full-screen mode. |



 

## Remarks

For full-screen mode to work properly when embedding the Windows Media Player control, the video display area must have a height and width of at least one pixel. If **uiMode** is set to "mini" or "full", the height of the control itself must be 65 or greater to accommodate the video display area in addition to the user interface.

If **uiMode** is set to "invisible", then setting this property to true raises an error and does not affect the behavior of the control.

During full-screen playback, Windows Media Player hides the mouse cursor when **enableContextMenu** equals false and **uiMode** equals "none".

If **uiMode** is set to "full" or "mini", Windows Media Player displays transport controls in full-screen mode when the mouse cursor moves. After a brief interval of no mouse movement, the transport controls are hidden. If **uiMode** is set to "none", no controls are displayed in full-screen mode.

**Note**

Displaying transport controls in full-screen mode requires the Windows XP operating system.

If transport controls are not displayed in full-screen mode, then Windows Media Player automatically exits full-screen mode when playback stops.

**Note**

Always be sure to inform the user how to return from full-screen mode.

## Examples

The following example creates an HTML input button that uses *Player*.**fullScreen** to switch an embedded player object to full-screen mode. The **Player** object was created with ID = "Player".


```
<INPUT type = button 
       value = "Full Screen" 
       name = FSBUTTON
       onclick = "
               /* Check to be sure the player is playing. */
               if (Player.playState == 3) 
                  Player.fullScreen = 'true';
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

 

 





