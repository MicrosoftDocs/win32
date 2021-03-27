---
title: MediaCollection.add method
description: The add method adds a new media item or playlist to the library. | MediaCollection.add method
ms.assetid: '8adf93d1-368b-4916-937f-342901a1592b'
keywords:
- add method Windows Media Player
- add method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , add method
topic_type:
- apiref
api_name:
- MediaCollection.add
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollection.add method

The **add** method adds a new media item or playlist to the library.

## Syntax


```JScript
retVal = MediaCollection.add(
  path
)
```



## Parameters

<dl> <dt>

*path* \[in\]
</dt> <dd>

**String** containing the path.

</dd> </dl>

## Return value

This method returns a **Media** object.

## Remarks

This method loads an existing media item or playlist into the library, given a path to a file. This method does not move or change the file. This method fails if given an invalid local path, but digital media files are not checked for validity before they are added to the library.

This method accepts both static and auto playlist files. The *PlaylistCollection*.**importPlaylist** method can also be used to add a static playlist to the library.

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following Microsoft JScript example adds three media objects to the Windows Media Player media collection. The **Player** object was created with ID="Player".


```JScript
// Adding a media object using a website.
Player.mediaCollection.add("https://www.proseware.com/Media/Laure.wma");

// Adding a media object from a local network.
// You must add an escape sequence of a backslash for 
// every original backslash.
Player.mediaCollection.add("\\\\yourservername\\Public\\Jeanne.wma");

// Adding a media object from a file on a local drive.
// Be sure to add appropriate escape sequences.
Player.mediaCollection.add("C:\\WMSDK\\WMPSDK\\docs\\samples\\media\\house.wma");
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**MediaCollection.remove**](mediacollection-remove.md)
</dt> <dt>

[**PlaylistCollection.importPlaylist**](playlistcollection-importplaylist.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





