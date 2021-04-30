---
title: Playlist.item method
description: The item method retrieves the media item at the specified index.
ms.assetid: a564f6db-ede4-4c85-87ca-0e2539d914c2
keywords:
- item method Windows Media Player
- item method Windows Media Player , Playlist class
- Playlist class Windows Media Player , item method
topic_type:
- apiref
api_name:
- Playlist.item
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Playlist.item method

The **item** method retrieves the media item at the specified index.

## Syntax


```JScript
retVal = Playlist.item(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) containing the index of the item to be retrieved.

</dd> </dl>

## Return value

This method returns a **Media** object.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *Playlist*.**item** to retrieve a media item from the current playlist based on a user selection. An HTML SELECT element was created with name "weblist", and filled with the titles from the current playlist. The **Player** object was created with ID = "Player".


```JScript
// Store the value of the selected item in the list box
// using the selectedIndex property.
var index = weblist.selectedIndex;

// Store the corresponding digital media object from the current playlist.
var listItem = Player.currentPlaylist.item(index);

// Set the URL using the listItem variable.
Player.URL = listItem.sourceURL;

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**Playlist.insertItem**](playlist-insertitem.md)
</dt> <dt>

[**Playlist.removeItem**](playlist-removeitem.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





