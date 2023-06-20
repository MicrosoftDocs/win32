---
title: PlaylistCollection.getByName method
description: The getByName method retrieves a PlaylistArray object containing playlists with the specified name, if any exist.
ms.assetid: '0308a98d-1149-4367-b602-33fa54c1760f'
keywords:
- getByName method Windows Media Player
- getByName method Windows Media Player , PlaylistCollection class
- PlaylistCollection class Windows Media Player , getByName method
topic_type:
- apiref
api_name:
- PlaylistCollection.getByName
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlaylistCollection.getByName method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getByName** method retrieves a **PlaylistArray** object containing playlists with the specified name, if any exist.

## Syntax


```JScript
retVal = PlaylistCollection.getByName(
  name
)
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the name of the playlists to be retrieved.

</dd> </dl>

## Return value

This method returns a **PlaylistArray** object.

## Remarks

Use *PlaylistArray*.**count** to determine whether a playlist exists. If **count** is zero, a playlist does not exist.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *playlistCollection*.**getByName** to check the **playlistCollection** object for a playlist named "ThreeList". If the "Threelist" playlist exists, **getByName** sets "ThreeList" as the current playlist. The **Player** object was created with the ID = "Player".


```JScript
//Retrieve the count of the playlists named "ThreeList".
var Checkit = Player.playlistCollection.getByName("ThreeList").count;

//Since duplicate playlist names are allowed, the count returned
//will be either zero (no playlist) or greater than zero 
//(playlist exists).
if (Checkit > 0){ 
    
   //Retrieve a playlistArray object containing "ThreeList". Assume that
   //there is only one playlist with that name, and assign it to the 
   //current playlist.
   Player.currentPlaylist = Player.playlistCollection.getByName("ThreeList").item(0);
}

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**PlaylistArray Object**](playlistarray-object.md)
</dt> <dt>

[**PlaylistArray.count**](playlistarray-count.md)
</dt> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





