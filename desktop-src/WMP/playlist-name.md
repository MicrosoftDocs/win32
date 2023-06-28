---
title: Playlist.name
description: The name property specifies or retrieves the name of the playlist.
ms.assetid: f951954a-c280-44e9-96e1-ae18738bc95a
keywords:
- Playlist.name Windows Media Player
topic_type:
- apiref
api_name:
- Playlist.name
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playlist.name

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `name` property specifies or retrieves the name of the playlist.

## Syntax

*player*.*currentPlaylist*.**name**

## Possible Values

This property is a read/write **String**.

## Remarks

To retrieve the value of this property, read access to the library is required. To specify the value, full access is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This property is read only.

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

 

 





