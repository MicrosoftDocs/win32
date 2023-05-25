---
title: PlaylistCollection.getAll method
description: The getAll method retrieves a PlaylistArray object containing all the playlists in the library.
ms.assetid: 'ec3cb7d7-9c03-4dec-a0aa-ec8bf23547a5'
keywords:
- getAll method Windows Media Player
- getAll method Windows Media Player , PlaylistCollection class
- PlaylistCollection class Windows Media Player , getAll method
topic_type:
- apiref
api_name:
- PlaylistCollection.getAll
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlaylistCollection.getAll method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getAll** method retrieves a **PlaylistArray** object containing all the playlists in the library.

## Syntax


```JScript
retVal = PlaylistCollection.getAll()
```



## Parameters

This method has no parameters.

## Return value

This method returns a **PlaylistArray** object.

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

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





