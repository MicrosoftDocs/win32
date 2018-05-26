---
title: Playlist.removeItem method
description: The removeItem method removes the specified item from the playlist.
ms.assetid: 7a17b0e0-2eaf-4570-a297-c2540ae4b6c5
keywords:
- removeItem method Windows Media Player
- removeItem method Windows Media Player , Playlist class
- Playlist class Windows Media Player , removeItem method
topic_type:
- apiref
api_name:
- Playlist.removeItem
api_location:
- wmp.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Playlist.removeItem method

The **removeItem** method removes the specified item from the playlist.

## Syntax


```JScript
Playlist.removeItem(
  item
)
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

**Media** object to be removed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the item removed is the currently playing track (*Player*.**currentMedia**), playback stops and the next item in the playlist becomes the current one. If there is no next item, the previous item is used, or if there are no other items, then *Player*.**currentMedia** is set to **NULL**.

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player.currentMedia**](player-currentmedia.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**Playlist.insertItem**](playlist-insertitem.md)
</dt> <dt>

[**Playlist.item**](playlist-item.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





