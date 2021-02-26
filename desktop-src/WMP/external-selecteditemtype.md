---
title: External.selectedItemType
description: Note This topic describes functionality designed for use by online stores. | External.selectedItemType
ms.assetid: f566e41e-127b-4596-99e6-bb07fc97249e
keywords:
- External.selectedItemType Windows Media Player
topic_type:
- apiref
api_name:
- External.selectedItemType
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.selectedItemType

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **selectedItemType** property retrieves the type of the media item that is currently selected in Windows Media Player.

## Syntax

window.external.selectedItemType()

## Possible Values

This property is a read-only **String** that contains one of the [library location constants](library-location-constants.md).

## Remarks

This property is used in combination with the **External.selectedItemID** property. For example, if **selectedItemType** is equal to CPTrackID, then **selectedItemID** is the ID of the selected track. For more information about how Windows Media Player characterizes views of online store content, see [Location and Selected Item](location-and-selected-item.md).

Certain views in Windows Media Player have a particular media item that is selected. For example, suppose the current view represents an album. An album is a container of tracks, so **selectedItemType** is equal to CPTrackID, and **selectedItemID** is the ID of the selected track. Other views do not have a selected media item. For example, if the user clicks the online store's root node in the tree-view control, Windows Media Player displays a discovery page provided by the online store. The Player does not display any container of media items in the Player user interface. In that case, **selectedItemType** is equal to UnknownLocation, and **selectedItemID** is equal to the empty string.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.selectedItemID**](external-selecteditemid.md)
</dt> <dt>

[**Location and Selected Item**](location-and-selected-item.md)
</dt> </dl>

 

 





