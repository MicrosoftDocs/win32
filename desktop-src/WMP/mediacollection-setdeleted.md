---
title: MediaCollection.setDeleted method
description: The setDeleted method moves the specified media item to the deleted items folder. | MediaCollection.setDeleted method
ms.assetid: '3e3c9a16-37e1-41b4-8593-58aaf4541eb9'
keywords:
- setDeleted method Windows Media Player
- setDeleted method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , setDeleted method
topic_type:
- apiref
api_name:
- MediaCollection.setDeleted
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MediaCollection.setDeleted method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setDeleted** method moves the specified media item to the deleted items folder.

## Syntax


```JScript
MediaCollection.setDeleted(
  item,
  true
)
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

**Media** object being moved.

</dd> <dt>

*true* \[in\]
</dt> <dd>

Always specify this value.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method does not remove files from the user's computer.

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following JScript example uses *MediaCollection*.**setDeleted** to move a particular media item, stored in the variable named mediaObject, to the deleted items folder. The *MediaCollection*.**isDeleted** method first tests whether the item has already been deleted. The **Player** object was created with ID = "Player".


```JScript
// Test whether the media item is in the deleted items folder.
if (!Player.mediaCollection.isDeleted(mediaObject)){

    // The item is available to be deleted; move it to 
    // the deleted items folder.
    Player.mediaCollection.setDeleted(mediaObject, true);

    // Inform the user that the operation succeeded.
    alert("Item moved to deleted items folder.");}

else
    // Tell the user the operation is unnecessary.
    alert("Item is already deleted!");
}

```



## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0, Windows Media Player version 7.1, or Windows Media Player for Windows XP. This method is not supported for Windows Media Player 9 Series or later.<br/> |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl>                                                                                                              |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**MediaCollection.isDeleted**](mediacollection-isdeleted.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





