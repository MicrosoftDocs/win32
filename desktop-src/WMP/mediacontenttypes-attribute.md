---
title: MediaContentTypes Attribute
description: The MediaContentTypes attribute specifies the type of content in the item.
ms.assetid: b91bab65-d6d2-4e05-9338-c24f28b7c71e
keywords:
- MediaContentTypes Attribute Windows Media Player
topic_type:
- apiref
api_name:
- MediaContentTypes
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# MediaContentTypes Attribute

The **MediaContentTypes** attribute specifies the type of content in the item.

## Applies To

-   [Playlists](playlist-attributes-ref.md)

## Remarks

This attribute can be one of the following values:



| Value | Meaning                                |
|-------|----------------------------------------|
| 1     | The playlist contains audio content.   |
| 2     | To be supplied.                        |
| 3     | The playlist contains audio content.   |
| 4     | The playlist contains video content.   |
| 5     | The playlist contains picture content. |
| 6     | The playlist contains TV content.      |



 

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





