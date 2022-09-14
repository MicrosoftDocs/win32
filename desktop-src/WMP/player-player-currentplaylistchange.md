---
title: Player.CurrentPlaylistChange event
description: The CurrentPlaylistChange event occurs when something changes within the current playlist. | Player.CurrentPlaylistChange event
ms.assetid: 5270373e-e401-40c6-bf8c-ef0557610372
keywords:
- CurrentPlaylistChange event Windows Media Player
- CurrentPlaylistChange event Windows Media Player , Player class
- Player class Windows Media Player , CurrentPlaylistChange event
topic_type:
- apiref
api_name:
- Player.CurrentPlaylistChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.CurrentPlaylistChange event

The **CurrentPlaylistChange** event occurs when something changes within the current playlist.

## Syntax


```JScript
Player.CurrentPlaylistChange(
  change
)
```



## Parameters

<dl> <dt>

*change* 
</dt> <dd>

**Number** (**long**) indicating what type of change occurred to the playlist. See the *Player*.**PlaylistChange** event for a table of possible values.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event does not occur when a different playlist becomes the current playlist. It only occurs when a change happens within the current playlist, such as a media item being appended to the playlist.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

## Examples

The following JScript example updates the text in an HTML DIV element, named PlItems, to display the names of the media items in the current playlist. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for current playlist change. -->
<SCRIPT FOR = "Player" EVENT = "currentPlaylistChange(change)">
   switch (change){
      // Only update for move, delete, insert, and append events.
      case 3, 4, 5, 6:

         // Clear the contents of the DIV.
         PlItems.innerHTML = "";

         // Loop through the playlist and display each item name.
         for (var i = 0; i < Player.currentPlaylist.count; i++){
            PlItems.innerHTML += Player.currentPlaylist.item(i).name;
            PlItems.innerHTML += "<br>";
         }
         break;
      
      default:
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

[**Player.currentPlaylist**](player-currentplaylist.md)
</dt> <dt>

[**Player.PlaylistChange**](player-player-playlistchange.md)
</dt> </dl>

 

 





