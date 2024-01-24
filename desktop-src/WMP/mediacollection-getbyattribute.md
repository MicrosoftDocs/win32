---
title: MediaCollection.getByAttribute method
description: The getByAttribute method retrieves a playlist of media items that contain a specified value for a specified attribute.
ms.assetid: 'a89f9c52-c655-4420-858e-c0eed661856f'
keywords:
- getByAttribute method Windows Media Player
- getByAttribute method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , getByAttribute method
topic_type:
- apiref
api_name:
- MediaCollection.getByAttribute
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MediaCollection.getByAttribute method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getByAttribute** method retrieves a playlist of media items that contain a specified value for a specified attribute.

## Syntax


```JScript
retVal = MediaCollection.getByAttribute(
  attribute,
  value
)
```



## Parameters

<dl> <dt>

*attribute* \[in\]
</dt> <dd>

**String** indicating the name of the attribute to search. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

</dd> <dt>

*value* \[in\]
</dt> <dd>

**String** indicating the value that the attribute should have.

</dd> </dl>

## Return value

This method returns a **Playlist** object.

## Remarks

This method can be used to create a generic query for media items that match a value for an attribute in the database. This is useful in the case of user-defined attributes. If the attribute does not exist, an error will result.

You can use this method to retrieve all of the media items of a specific type. Use the attribute name "MediaType" and one of the following values:



| Value    | Description                                                |
|----------|------------------------------------------------------------|
| audio    | Music and other audio-only items.                          |
| playlist | Playlists represented as **Media** objects.                |
| radio    | Radio station items. Not used by Windows Media Player 10.  |
| video    | Video items.                                               |
| photo    | Photo items. Requires Windows Media Player 10.             |
| other    | Other items, such as ASF files or URLs to streaming media. |



 

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *MediaCollection*.**getByAttribute** to play all content from the library by the artist named Triode 48. The **Player** object was created with ID = "Player".


```JScript
// Get a playlist object filled with media items by a 
// particular artist.
var pl = Player.mediaCollection.getByAttribute("Artist", "Triode 48");

// Make the new playlist the current one.
Player.currentPlaylist = pl;

// Start Windows Media Player.
Player.controls.play();

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

 

 





