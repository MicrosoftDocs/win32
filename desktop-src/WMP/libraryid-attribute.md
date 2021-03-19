---
title: LibraryID Attribute
description: The LibraryID attribute is the identifier of the library that the item belongs to.
ms.assetid: 680d9374-8729-4258-8672-b4b93b65e20a
keywords:
- LibraryID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- LibraryID Attribute
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# LibraryID Attribute

The **LibraryID** attribute is the identifier of the library that the item belongs to.

## Applies To

-   [**Audio Items**](audio-item-attributes.md)
-   [**Photo Items**](photo-item-attributes.md)
-   [**Playlist Items**](playlist-attributes-ref.md)
-   [**Video Items**](video-item-attributes.md)

## Remarks

A media item might belong to the current user's local library or it might belong to a library that has been made available by another user on the home network or the Internet.

The value of this attribute is the same as the value returned by the [**IWMPLibrary2::getItemInfo**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibrary-get_name) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 12<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





