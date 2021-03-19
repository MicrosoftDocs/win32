---
title: MediaCollection.isDeleted method
description: The isDeleted method retrieves a value indicating whether the specified media item is in the deleted items folder.
ms.assetid: bb3ce9c9-9e43-45a5-8802-dc6783cf2ad7
keywords:
- isDeleted method Windows Media Player
- isDeleted method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , isDeleted method
topic_type:
- apiref
api_name:
- MediaCollection.isDeleted
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MediaCollection.isDeleted method

The **isDeleted** method retrieves a value indicating whether the specified media item is in the deleted items folder.

## Syntax


```JScript
bRetVal = MediaCollection.isDeleted(
  item
)
```



## Parameters

<dl> <dt>

*item* \[in\]
</dt> <dd>

**Media** object that might be deleted.

</dd> </dl>

## Return value

This method returns a **Boolean**.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This method always returns **false**.

## Examples

The following JScript example uses *MediaCollection*.**isDeleted** to test whether a particular media item, stored in the variable named mediaObject, is in the deleted items folder. If the media item has not been deleted already, it is moved to the deleted items folder. The **Player** object was created with ID = "Player".


```JScript
// Test whether the media item is in the deleted items folder.
if (!Player.mediaCollection.isDeleted(mediaObject)){

    // The media item is available to be deleted, move it to 
    // the deleted items folder.
    Player.mediaCollection.setDeleted(mediaObject, true);

    // Inform the user that the operation succeeded.
    alert("Media item moved to deleted items folder.");}

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

[**MediaCollection.setDeleted**](mediacollection-setdeleted.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





