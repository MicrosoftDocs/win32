---
title: PlaylistCollection.isDeleted method
description: The isDeleted method retrieves a value indicating whether the specified playlist is in the deleted items folder.
ms.assetid: 'ac3e3401-ac7e-44d2-9680-5abe69678fc7'
keywords: ["isDeleted method Windows Media Player", "isDeleted method Windows Media Player , PlaylistCollection class", "PlaylistCollection class Windows Media Player , isDeleted method"]
topic_type:
- apiref
api_name:
- PlaylistCollection.isDeleted
api_location:
- wmp.dll
api_type:
- COM
---

# PlaylistCollection.isDeleted method

The **isDeleted** method retrieves a value indicating whether the specified playlist is in the deleted items folder.

## Syntax


```JScript
bRetVal = PlaylistCollection.isDeleted(
  playlist
)
```



## Parameters

<dl> <dt>

*playlist* \[in\]
</dt> <dd>

The **Playlist** object to be searched for.

</dd> </dl>

## Return value

This method returns a **Boolean**.

**Windows Media Player 10 Mobile**: This method always returns **false**.

## Requirements



|                    |                                                                                                                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0, Windows Media Player version 7.1, or Windows Media Player for Windows XP. This method is not supported for Windows Media Player 9 Series or later.<br/> |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl>                                                                                                              |



## See also

<dl> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> </dl>

 

 





