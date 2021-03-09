---
title: Controls.playItem method
description: The playItem method plays the specified media item. | Controls.playItem method
ms.assetid: 410e315d-8d5f-4f45-82a7-4249e656c809
keywords:
- playItem method Windows Media Player
- playItem method Windows Media Player , Controls class
- Controls class Windows Media Player , playItem method
topic_type:
- apiref
api_name:
- Controls.playItem
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.playItem method

The **playItem** method plays the specified media item.

## Syntax


```JScript
Controls.playItem(
  theMediaItem
)
```



## Parameters

<dl> <dt>

*theMediaItem* \[in\]
</dt> <dd>

**Media** object to be played.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The media item will be loaded and played automatically, regardless of the value of the *Settings*.**autoStart** property. To load an item without playing it automatically, set *Settings*.**autoStart** to false and assign a value to *Player*.**URL**, after which **play** can be called to start playing the item.

Note

**playItem** works only with items in *currentPlaylist*. Calling **playItem** with a reference to a saved media item is not supported.

## Examples

The following JScript example uses **playItem** to play a media item from the current playlist. The item to play is chosen based upon its position in the playlist. The **Player** object was created with ID = "Player".


```JScript
// Declare a variable to hold the position of the media item 
// in the current playlist. An arbitrary value is supplied here.
var index = 3

// Retrieve the media item at the fourth position in the current playlist.
var media = Player.currentPlaylist.item(index);

// Play the media item.
Player.controls.playItem(media);

```



## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> <dt>

[**Playlist.item**](playlist-item.md)
</dt> </dl>

 

 





