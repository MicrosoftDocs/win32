---
title: MediaCollection.getByAlbum method
description: The GetByAlbum method retrieves a playlist containing the media items from the specified album.
ms.assetid: 'e7e72f0e-e0ae-4bbd-a8b7-966f0fc50059'
keywords:
- getByAlbum method Windows Media Player
- getByAlbum method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , getByAlbum method
topic_type:
- apiref
api_name:
- MediaCollection.getByAlbum
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollection.getByAlbum method

The **GetByAlbum** method retrieves a playlist containing the media items from the specified album.

## Syntax


```JScript
retVal = MediaCollection.getByAlbum(
  album
)
```



## Parameters

<dl> <dt>

*album* \[in\]
</dt> <dd>

**String** containing the name of the album.

</dd> </dl>

## Return value

This method returns a **Playlist** object.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following example uses *MediaCollection*.**getByAlbum** to retrieve a playlist of media items. The playlist contains items with the album specified by the user in an HTML TEXT input element named GetAlbum. The **Player** object was created with ID = "Player".


```JScript
<!-- Use an HTML BUTTON element to create the playlist and 
then play the digital media items. -->
<INPUT TYPE = "BUTTON"
       NAME = "PlayAlbum" 
       ID = "PlayAlbum"  
       VALUE = "Play Album"

onClick = "
    /* Retrieve the album title text from the user. */
    var album = GetAlbum.value;

    /* Create the playlist using getByAlbum. */
    var pl = Player.mediaCollection.getByAlbum(album);

    /* Make the new playlist the current playlist. */
    Player.currentPlaylist = pl;

    /* Play the media in the new playlist. */
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

 

 





