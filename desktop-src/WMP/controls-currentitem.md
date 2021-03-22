---
title: Controls.currentItem
description: The currentItem property specifies or retrieves the current media item.
ms.assetid: 77e21585-3cc8-41f5-97b5-da6eb992c7bc
keywords:
- Controls.currentItem Windows Media Player
topic_type:
- apiref
api_name:
- Controls.currentItem
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.currentItem

The **currentItem** property specifies or retrieves the current media item.

``` syntax
player.controls.currentItem
      
```

## Possible Values

This property is a read/write **Media** object.

## Remarks

This method works only with items in *Player*.**currentPlaylist**. Calling **currentItem** with a reference to a saved media item is not supported.

## Examples

The following JScript example uses **currentItem** to set the player control current media item to the selected value in an HTML SELECT element. The current playlist was first specified by using *PlaylistCollection*.**getByName**. The **Player** object was created with ID = "Player".


```JScript
<SELECT ID = playItem  NAME = "playItem"  LANGUAGE = "JScript"

    /* Specify the current item when the selected list value changes. */
    onChange = "Player.controls.currentItem = Player.currentPlaylist.item(playItem.value);">

    /* Fill the SELECT element list with three items that match
       the songs in the playlist. */
    <OPTION VALUE = 0 >Laure
    <OPTION VALUE = 1 >Jeanne
    <OPTION VALUE = 2 >House
</SELECT>

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

[**Media Object**](media-object.md)
</dt> <dt>

[**PlaylistCollection.getByName**](playlistcollection-getbyname.md)
</dt> </dl>

 

 





