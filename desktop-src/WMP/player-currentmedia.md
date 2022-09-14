---
title: Player.currentMedia
description: The currentMedia property specifies or retrieves the current Media object.
ms.assetid: 5cf45a10-9d0d-435e-97f1-d2c9c51f4b47
keywords:
- Player.currentMedia Windows Media Player
topic_type:
- apiref
api_name:
- Player.currentMedia
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.currentMedia

The **currentMedia** property specifies or retrieves the current Media object.

## Syntax

*player* .**currentMedia**

## Possible Values

This property is a read/write Media object.

## Remarks

If the *Settings*.**autoStart** property is true, playback begins automatically whenever you set **currentMedia**.

This property takes a Media object, which can be acquired by using *Playlist*.**item**. To load a **Media** item using a file name, set the URL property or use **newMedia**.

## Examples

The following JScript example retrieves the first media item in the library. It then uses **currentMedia** to make the retrieved media item the current media item, and then to display the name of the current media item. The **Player** object was created with ID = "Player".


```JScript
// Retrieve the first media item from the library.
var firstMedia = Player.mediaCollection.getAll().item(0);

// Make the retrieved media item the current media item.
Player.currentMedia = firstMedia;

// Display the name of the current media item.
document.write("Found first media item. Name = " + Player.currentMedia.name);
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.newMedia**](player-newmedia.md)
</dt> <dt>

[**Playlist.item**](playlist-item.md)
</dt> <dt>

[**Settings.autoStart**](settings-autostart.md)
</dt> </dl>

 

 





