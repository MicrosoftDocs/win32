---
title: LibraryName Attribute
description: The LibraryName attribute is the name of the library that the item belongs to.
ms.assetid: 70ce2de1-6c7b-427a-ba48-a9f69bacd015
keywords:
- LibraryName Attribute Windows Media Player
topic_type:
- apiref
api_name:
- LibraryName
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# LibraryName Attribute

The LibraryName attribute is the name of the library that the item belongs to.

## Applies To

-   [**Audio Items**](audio-item-attributes.md)
-   [**Photo Items**](photo-item-attributes.md)
-   [**Playlist Items**](playlist-attributes-ref.md)
-   [**Video Items**](video-item-attributes.md)

## Remarks

A media item might belong to the current user's local library or it might belong to a library that has been made available by another user on a home network.

The value of this attribute is the same as the value returned by the [**IWMPLibrary::get\_name**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibrary-get_name) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 12<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





