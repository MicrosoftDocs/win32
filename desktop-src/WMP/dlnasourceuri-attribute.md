---
title: DLNASourceURI Attribute
description: The DLNASourceURI attribute is the universal resource identifier (URI) of the item.
ms.assetid: 323c897b-9b76-44f7-9313-c51595589583
keywords:
- DLNASourceURI Attribute Windows Media Player
topic_type:
- apiref
api_name:
- DLNASourceURI
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# DLNASourceURI Attribute

The **DLNASourceURI** attribute is the universal resource identifier (URI) of the item.

## Applies To

-   [**Audio Items**](audio-item-attributes.md)
-   [**Other Items**](other-item-attributes.md)
-   [**Photo Items**](photo-item-attributes.md)
-   [**Playlist Items**](playlist-attributes-ref.md)
-   [**Video Items**](video-item-attributes.md)

## Remarks

If the item is in the current user's local library, this attribute, the [**SourceURL**](sourceurl-attribute.md) attribute, and the value returned by [**IWMPMedia::get\_sourceURL**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmedia-get_sourceurl) are all the same.

If the item is not in the current user's local library, but belongs to a remote library, this attribute is an identifier of the form dlna-playsingle://*xxx*.

You can pass a dlna-playsingle URI to the [**IWMPCore3::newMedia**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcore3-newmedia) method to obtain an [**IWMPMedia**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia) interface that enables you to view the media item's metadata and potentially edit the media item's star rating. Note, however, that the dlna-playsingle URI must be for a content directory service (CDS) that Windows Media Player has already discovered. The **newMedia** method will not initiate UPnP discovery and search for the CDS.

You can edit the star rating of a media item in a remote library only if the remote library supports the edit operation. Remote libraries hosted on a computer running Windows 7 support the edit operation. Remote libraries hosted on a computer running a Windows operating system earlier than Windows 7 do not support the edit operation.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 12<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





