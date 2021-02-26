---
title: External.libraryLocationID
description: Note This topic describes functionality designed for use by online stores. | External.libraryLocationID
ms.assetid: 9a9bea89-c05c-4759-be22-86588bbeca2c
keywords:
- External.libraryLocationID Windows Media Player
topic_type:
- apiref
api_name:
- External.libraryLocationID
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.libraryLocationID

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **libraryLocationID** property retrieves the identifier of the specific media item that is currently displayed in the Player's view.

``` syntax
window.external.libraryLocationID
      
```

## Possible Values

This property is a read-only **String**.

## Remarks

This property works in combination with the [External.libraryLocationType](external-librarylocationtype.md) property. For example, suppose **libraryLocationType** is equal to CPAlbumID and **libraryLocationID** is equal to 3. That means the current view in Windows Media Player is showing the album that has an ID of 3. For more information about how Windows Media Player characterizes views of online store content, see [Location and Selected Item](location-and-selected-item.md).

Certain views in Windows Media Player are associated with a particular media item. For example, if the current view represents an individual album, **libraryLocationType** is equal to CPAlbumID, and **libraryLocationID** is the ID of the album. Other views are not associated with any particular media item. For example, if the current view represents all albums, **libraryLocationType** is equal to AllCPAlbumIDs, but there is no meaningful value that can be assigned to **libraryLocationID**. In cases where the **libraryLocationID** property has no meaningful value, it is equal to the empty string.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.libraryLocationType**](external-librarylocationtype.md)
</dt> <dt>

[**Location and Selected Item**](location-and-selected-item.md)
</dt> </dl>

 

 





