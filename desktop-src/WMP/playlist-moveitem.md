---
title: Playlist.moveItem method
description: The moveItem method changes the location of an item in the playlist.
ms.assetid: '82a8de86-4419-48a7-89f8-f7b9084b51d4'
keywords:
- moveItem method Windows Media Player
- moveItem method Windows Media Player , Playlist class
- Playlist class Windows Media Player , moveItem method
topic_type:
- apiref
api_name:
- Playlist.moveItem
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Playlist.moveItem method

The **moveItem** method changes the location of an item in the playlist.

## Syntax


```JScript
Playlist.moveItem(
  oldIndex,
  newIndex
)
```



## Parameters

<dl> <dt>

*oldIndex* \[in\]
</dt> <dd>

**Number** (**long**) containing the old index.

</dd> <dt>

*newIndex* \[in\]
</dt> <dd>

**Number** (**long**) containing the new index.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Playlists stored in the library can change outside your control. Be sure to monitor and handle all appropriate playlist-related events so that the order of items in the playlist does not change unexpectedly.

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

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

 

 





