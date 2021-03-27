---
title: PLAYLIST.itemMedia
description: The itemMedia attribute retrieves the Media object corresponding to the given index in the PLAYLIST element.
ms.assetid: 38085798-7986-432f-8c88-de886bfc2ac5
keywords:
- PLAYLIST.itemMedia Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.itemMedia
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PLAYLIST.itemMedia

The **itemMedia** attribute retrieves the **Media** object corresponding to the given index in the **PLAYLIST** element.

``` syntax
        elementID.itemMedia(index)
```

## Possible Values

This attribute is a read-only **Media** object.

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number**(**long**) containing the index of a playlist item.

</dd> </dl>

## Remarks

The **itemMedia** property will return media objects that are expanded in the **PLAYLIST** element. For example, if there is a playlist that contains three media clips that is not expanded in the **PLAYLIST** element, **itemMedia**(0) will return the playlist as the media object. If the playlist is expanded, **itemMedia**(0) will return the first media clip in the playlist.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





