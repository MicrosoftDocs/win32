---
title: PLAYLIST.itemCount
description: The itemCount attribute retrieves the number of items currently displayed in the PLAYLIST element.
ms.assetid: d090d95c-e3c3-41bc-951e-ffeb0a314a0c
keywords:
- PLAYLIST.itemCount Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.itemCount
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PLAYLIST.itemCount

The **itemCount** attribute retrieves the number of items currently displayed in the **PLAYLIST** element.

``` syntax
        elementID.itemCount
```

## Possible Values

This attribute is a read-only **Number** (**long**).

## Remarks

The **itemCount** property will count the total number of expanded items. For example, if there are two playlists that contain three media items each, **itemCount** will return 2 if the playlists are not expanded. If only the first playlist is expanded, **itemCount** will return 4. If both playlists are expanded, **itemCount** will return 6.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





