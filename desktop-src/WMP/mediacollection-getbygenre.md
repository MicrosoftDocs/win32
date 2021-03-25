---
title: MediaCollection.getByGenre method
description: The getByGenre method retrieves a playlist of the media items with the specified genre.
ms.assetid: '022a0c52-93e1-4ab4-90a7-632bcd6fc004'
keywords:
- getByGenre method Windows Media Player
- getByGenre method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , getByGenre method
topic_type:
- apiref
api_name:
- MediaCollection.getByGenre
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollection.getByGenre method

The **getByGenre** method retrieves a playlist of the media items with the specified genre.

## Syntax


```JScript
retVal = MediaCollection.getByGenre(
  genre
)
```



## Parameters

<dl> <dt>

*genre* \[in\]
</dt> <dd>

**String** containing the name of the genre.

</dd> </dl>

## Return value

This method returns a **Playlist** object.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *MediaCollection*.**getByGenre** to retrieve a playlist of media items. The playlist contains items with the genre specified by the user in an HTML TEXT input element named GetGenre. The **Player** object was created with ID = "Player".


```JScript
<!-- Use an HTML BUTTON element to create the playlist and play 
the media items. -->
<INPUT TYPE = "BUTTON"  
       NAME = "PlayGenre"  
       ID = "PlayGenre"  
       VALUE = "Play Genre"

onClick = "
    /* Retrieve the genre text from the user. */
    var genre = GetGenre.value;

    /* Create the playlist using getByGenre. */
    var pl = Player.mediaCollection.getByGenre(genre);

    /* Make the new playlist the current playlist. */
    Player.currentPlaylist = pl;

    /* Play the digital media item in the new playlist. */
    Player.controls.play();
">

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





