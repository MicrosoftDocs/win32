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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Controls.currentItem

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





