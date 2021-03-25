---
title: PlaylistArray.item method
description: The item method retrieves the playlist at the given index.
ms.assetid: 'cc851695-f9a2-4594-8bd3-3555c18bfa10'
keywords:
- item method Windows Media Player
- item method Windows Media Player , PlaylistArray class
- PlaylistArray class Windows Media Player , item method
topic_type:
- apiref
api_name:
- PlaylistArray.item
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# PlaylistArray.item method

The **item** method retrieves the playlist at the given index.

## Syntax


```JScript
retVal = PlaylistArray.item(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) containing the index of the playlist to be retrieved.

</dd> </dl>

## Return value

This method returns a **Playlist** object.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**PlaylistArray Object**](playlistarray-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





