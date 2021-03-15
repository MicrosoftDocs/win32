---
title: External.addToBasket method
description: Note This topic describes functionality designed for use by online stores. | External.addToBasket method
ms.assetid: c0dc8cd7-b924-47b8-b36c-caff8f1f892f
keywords:
- addToBasket method Windows Media Player
- addToBasket method Windows Media Player , External class
- External class Windows Media Player , addToBasket method
topic_type:
- apiref
api_name:
- External.addToBasket
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.addToBasket method

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **addToBasket** method adds media items to the list pane (also called the basket) in Windows Media Player.

## Syntax


```JScript
External.addToBasket(
  ViewType,
  ViewIDs
)
```



## Parameters

<dl> <dt>

*ViewType* \[in\]
</dt> <dd>

**String** that specifies the type of item being added to the list pane. The caller must set this parameter to one of the following [library location constants](library-location-constants.md):

CPListID

CPTrackID

CPAlbumID

CPArtist

CPGenreID

CPAlbumSubGenreID

CPRadioID

</dd> <dt>

*ViewIDs* \[in\]
</dt> <dd>

**String** containing the IDs, delimited by semicolons, of the items to be added to the list pane.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExternalObject for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.basketTitle**](external-baskettitle.md)
</dt> </dl>

 

 





