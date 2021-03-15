---
title: External.templateBeingDisplayedInLocalLibrary
description: Note This topic describes functionality designed for use by online stores. | External.templateBeingDisplayedInLocalLibrary
ms.assetid: a1399c20-804b-4413-be9d-bcf160d75d29
keywords:
- External.templateBeingDisplayedInLocalLibrary Windows Media Player
topic_type:
- apiref
api_name:
- External.templateBeingDisplayedInLocalLibrary
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.templateBeingDisplayedInLocalLibrary

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **templateBeingDisplayedInLocalLibrary** property indicates whether the feed represented by the current discovery page is being displayed in the local library tree-view control.

## Syntax

``` syntax
window.external.templateBeingDisplayedInLocalLibrary
```

## Possible Values

This property is a read-only **Boolean**. **TRUE** indicates that the feed is being displayed in the local library tree-view control.

## Remarks

A discovery page that represents a feed for a dynamic playlist can display a button that allows the user to "save" the feed in his or her local library. Saving the feed, in this context, means that some metadata is saved on the user's computer, and the feed is listed under the **Playlists** node in the local library tree-view control. Script on the discovery page can inspect the **templateBeingDisplayedInLocalLibrary** property to determine whether the user has already saved the feed in the local library. If the user has already saved the feed, the discovery page should not display the save button.

A discovery page that represents a radio feed should inspect the **templateBeingDisplayedInLocalLibrary** property for the same reason.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





