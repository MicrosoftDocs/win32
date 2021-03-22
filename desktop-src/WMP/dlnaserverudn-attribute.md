---
title: DLNAServerUDN Attribute
description: The DLNAServerUDN attribute is the unique device name of the server that hosts the media item.
ms.assetid: 1965731d-1b6e-4d76-a983-fd57c851fcfb
keywords:
- DLNAServerUDN Attribute Windows Media Player
topic_type:
- apiref
api_name:
- DLNAServerUDN Attribute
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DLNAServerUDN Attribute

The **DLNAServerUDN** attribute is the unique device name of the server that hosts the media item.

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

 

 





