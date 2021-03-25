---
title: MediaCollection.getAll method
description: The getAll method retrieves a playlist containing all media items in the library.
ms.assetid: 'c22532ee-5714-4762-966f-7dc6543384f4'
keywords:
- getAll method Windows Media Player
- getAll method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , getAll method
topic_type:
- apiref
api_name:
- MediaCollection.getAll
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollection.getAll method

The **getAll** method retrieves a playlist containing all media items in the library.

## Syntax


```JScript
retVal = MediaCollection.getAll()
```



## Parameters

This method has no parameters.

## Return value

This method returns a **Playlist** object.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *MediaCollection*.**getAll** to play media items randomly from the media collection. The **Player** object was created with ID = "Player".


```JScript
// Store the count of all media items in the media collection.
var count = Player.mediaCollection.getAll().count;

// Generate a random number using the media count.
var rand = Math.random() * count;

// Round down the random number to the nearest integer.
rand = Math.floor(rand);

// Make the random media item the current media item.
Player.currentMedia = Player.mediaCollection.getAll().item(rand);

// Play the media item.
// Player.controls.play();

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





