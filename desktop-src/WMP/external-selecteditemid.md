---
title: External.selectedItemID
description: Note This topic describes functionality designed for use by online stores. | External.selectedItemID
ms.assetid: 150aaa38-d4fe-493e-bda1-e5b0a27fccf7
keywords:
- External.selectedItemID Windows Media Player
topic_type:
- apiref
api_name:
- External.selectedItemID
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.selectedItemID

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **selectedItemID** property retrieves the identifier of the media item that is currently selected in Windows Media Player.

## Syntax

``` syntax
window.external.selectedItemID
```

## Possible Values

This property is a read-only **String**.

## Remarks

This property is used in combination with the [External.selectedItemType](external-selecteditemtype.md) property. For example, if **selectedItemType** is equal to CPTrackID, then **selectedItemID** is the ID of the selected track. For more information about how Windows Media Player characterizes views of online store content, see [Location and Selected Item](location-and-selected-item.md).

Certain views in Windows Media Player have a particular media item that is selected. For example, suppose the current view represents an album. An album is a container of tracks, so **selectedItemType** is equal to CPTrackID, and **selectedItemID** is the ID of the selected track. Other views do not have a selected media item. For example, if the user clicks the online store's root node in the tree-view control, Windows Media Player displays a discovery page provided by the online store. The Player does not display any container of media items in the Player user interface. In that case, **selectedItemType** is equal to UnknownLocation, and **selectedItemID** is equal to the empty string.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.selectedItemType**](external-selecteditemtype.md)
</dt> <dt>

[**Location and Selected Item**](location-and-selected-item.md)
</dt> </dl>

 

 





