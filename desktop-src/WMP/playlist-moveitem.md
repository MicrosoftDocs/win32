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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playlist.moveItem method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





