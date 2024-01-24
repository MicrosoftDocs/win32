---
title: PLAYLIST.dropDownList
description: The dropDownList attribute specifies or retrieves a value indicating which elements show up in the drop-down list box for a given instance of the PLAYLIST element.
ms.assetid: 583041b0-25dc-4015-a3b2-37f3cfdcd496
keywords:
- PLAYLIST.dropDownList Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.dropDownList
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.dropDownList

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **dropDownList** attribute specifies or retrieves a value indicating which elements show up in the drop-down list box for a given instance of the **PLAYLIST** element.

``` syntax
        elementID.dropDownList
```

## Possible Values

This attribute is a read/write **String** containing one of the following values.



| Value       | Description                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------|
| showAlbums  | Shows albums.                                                                                    |
| showAll     | Default. Shows all available elements including CD playlists, user playlists, and radio presets. |
| showCD      | Shows the CD playlist.                                                                           |
| showClips   | Shows all clips.                                                                                 |
| showCurrent | Shows the current, unsaved playlist.                                                             |
| showLibrary | Shows only library playlists.                                                                    |
| showRadio   | Shows radio presets.                                                                             |
| showQueries | Shows queries.                                                                                   |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





