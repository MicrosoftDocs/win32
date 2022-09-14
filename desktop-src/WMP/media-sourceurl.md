---
title: Media.sourceURL
description: The sourceURL property retrieves the URL of the media item.
ms.assetid: 98ff6ed4-ad3d-44f8-893d-f016e5217ce5
keywords:
- Media.sourceURL Windows Media Player
topic_type:
- apiref
api_name:
- Media.sourceURL
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Media.sourceURL

The **sourceURL** property retrieves the URL of the media item.

## Syntax

*player*.*currentMedia*.sourceURL

## Possible Values

This property is a read-only **String**.

## Examples

The following JScript example uses *Media*.**sourceURL** to retrieve the URL of the first media item in the sample playlist; the URL of the media item is then assigned to the player object **URL** property. The **Player** object was created with ID = "Player".


```JScript
// Store the sample playlist object in a variable. 
var pl = Player.playlistCollection.getByName("Sample Playlist").item(0);

// Store the first media item from the sample playlist.
var media = pl.item(0);

// Change the URL property of the player to the URL of the media item.
Player.URL = media.sourceURL;

// Play the media item.
Player.controls.play();

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> </dl>

 

 





