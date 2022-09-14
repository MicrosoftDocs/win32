---
title: WM/AlbumCoverURL Attribute
description: The WM/AlbumCoverURL attribute is the uniform resource locator (URL) for album art or a thumbnail image.
ms.assetid: 0134867a-7c11-4d50-9ab5-b48c1ca6c473
keywords:
- WM/AlbumCoverURL Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/AlbumCoverURL Attribute
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/AlbumCoverURL Attribute

The **WM/AlbumCoverURL** attribute is the uniform resource locator (URL) for album art or a thumbnail image.

## Applies To

-   [**Audio Items**](audio-item-attributes.md)
-   [**Photo Items**](photo-item-attributes.md)
-   [**Video Items**](video-item-attributes.md)

## Remarks

For an audio item, this attribute is the URL of the album art. For a photo or video item, this attribute is the URL of a thumbnail image.

This attribute is not available for media items in the current user's local library. It is available only for media items that belong to a remote library; that is, a library that has been made available by another user on the home network. To determine whether a media library is remote, call [**IWMPLibrary::get\_type**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibrary-get_type).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 12 or later.<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





