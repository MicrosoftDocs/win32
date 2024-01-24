---
title: MediaCollection.remove method
description: The remove method removes an item from the media collection.
ms.assetid: '7d4c03ed-01c8-4112-90b6-5de52eacb199'
keywords:
- remove method Windows Media Player
- remove method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , remove method
topic_type:
- apiref
api_name:
- MediaCollection.remove
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MediaCollection.remove method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **remove** method removes an item from the media collection.

## Syntax


```JScript
MediaCollection.remove(
  item,
  delete
)
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

**Media** object to be removed.

</dd> <dt>

*delete* \[in\]
</dt> <dd>

**Boolean** indicating whether to remove the item.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method deletes an item from the library. This method does not delete files from the user's computer.

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example, after prompting the user, permanently deletes the first media item in the media collection by using *MediaCollection*.**remove**. The **Player** object was created with ID = "Player".


```JScript
// Retrieve the first item from the media collection.
var mediaObject = Player.mediaCollection.getAll().item(0);

// Store the name of the retrieved object.
var mediaName = mediaObject.name;

// Prompt the user for permission to delete the object.
var answer = confirm("OK to permanently delete " + mediaName + "?");

// Check the user response.
if (answer){

    // Permanently delete the item.
    Player.mediaCollection.remove(mediaObject, true);

    // Report that the item was deleted.
    alert("Deleted item " + mediaName);
}

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

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**MediaCollection.add**](mediacollection-add.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





