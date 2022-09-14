---
title: AlternateSourceURL Attribute
description: The AlternateSourceURL attribute is a uniform resource locator for the media item that serves as an alternative to the DLNASourceURI and SourceURL attributes.
ms.assetid: 2be88d9b-4fd8-4e70-9a4d-114a2bf8b23c
keywords:
- AlternateSourceURL Attribute Windows Media Player
topic_type:
- apiref
api_name:
- AlternateSourceURL Attribute
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AlternateSourceURL Attribute

The **AlternateSourceURL** attribute is a uniform resource locator for the media item that serves as an alternative to the [**DLNASourceURI**](dlnasourceuri-attribute.md) and [**SourceURL**](sourceurl-attribute.md) attributes.

## Applies To

-   [**Audio Items**](audio-item-attributes.md)
-   [**Photo Items**](photo-item-attributes.md)
-   [**Playlist Items**](playlist-attributes-ref.md)
-   [**Video Items**](video-item-attributes.md)

## Remarks

This attribute is not available for media items in the current user's local library. It is available only for media items that belong to a remote library; that is, a library that has been made available by another user on the home network. To determine whether a media library is remote, call [**IWMPLibrary::get\_type**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibrary-get_type).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 12<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





