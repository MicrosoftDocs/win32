---
title: Playlist.appendItem method
description: The appendItem method adds a media item to the end of the playlist.
ms.assetid: 'cc956491-7936-49e7-90ca-1f71e03448cd'
keywords:
- appendItem method Windows Media Player
- appendItem method Windows Media Player , Playlist class
- Playlist class Windows Media Player , appendItem method
topic_type:
- apiref
api_name:
- Playlist.appendItem
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Playlist.appendItem method

The **appendItem** method adds a media item to the end of the playlist.

## Syntax


```JScript
Playlist.appendItem(
  item
)
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

**Media** object to be added.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *Playlist*.**appendItem** to add the current media item to the playlist named "ThreeList". The **Player** object was created with ID="Player".


```JScript
// Get the current media item.
var currMedia = Player.currentMedia;

// Get the playlist object by name.
var plThreeList = Player.playlistCollection.getByName("ThreeList").item(0);

// Append the media item to the playlist.
plThreeList.appendItem(currMedia);

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





