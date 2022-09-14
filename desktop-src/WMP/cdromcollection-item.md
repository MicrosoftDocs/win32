---
title: CdromCollection.item method
description: The item method retrieves the Cdrom object at the given index.
ms.assetid: c1efa972-736d-4fa0-9835-14ee594ae719
keywords:
- item method Windows Media Player
- item method Windows Media Player , CdromCollection class
- CdromCollection class Windows Media Player , item method
topic_type:
- apiref
api_name:
- CdromCollection.item
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CdromCollection.item method

The **item** method retrieves the **Cdrom** object at the given index.

## Syntax


```JScript
retVal = CdromCollection.item(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) containing the index.

</dd> </dl>

## Return value

This method returns a **Cdrom** object.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *CdromCollection*.**item** to print the playlist name from each CD available on the computer. If the drive actually contains DVD content, Windows XP or later is required. An HTML TextArea element was created with ID = "playlists". The **Player** object was created with ID = "Player".


```JScript
// Create an array to store the CD playlists.
var cdPlaylists = new Array();

// Loop through the available CD drives.
for (var i = 0; i < Player.cdromCollection.count; i++){

     // Fill the cdPlaylists array with playlist objects.
     cdPlaylists[i] = Player.cdromCollection.item(i).Playlist;

     // Print each drive specifier.
     playlists.value+=Player.cdromCollection.item(i).driveSpecifier + " ";

     // Print the name of each CD playlist to the text area.
     playlists.value += cdPlaylists[i].name + "\n";
}

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cdrom.driveSpecifier**](cdrom-drivespecifier.md)
</dt> <dt>

[**CdromCollection Object**](cdromcollection-object.md)
</dt> <dt>

[**CdromCollection.count**](cdromcollection-count.md)
</dt> <dt>

[**Playlist.name**](playlist-name.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





