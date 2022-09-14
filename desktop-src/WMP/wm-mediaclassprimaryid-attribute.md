---
title: WM/MediaClassPrimaryID Attribute
description: The WM/MediaClassPrimaryID attribute is a GUID specifying one of the primary media classes music, non-music audio, video, or other.
ms.assetid: eb78f4a9-7c18-4cad-bb34-fd1ff15bad4f
keywords:
- WM/MediaClassPrimaryID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/MediaClassPrimaryID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/MediaClassPrimaryID Attribute

The **WM/MediaClassPrimaryID** attribute is a GUID specifying one of the primary media classes: music, non-music audio, video, or other.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Photo Items](photo-item-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Radio Items](radio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

**MediaClassPrimaryID** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMMediaClassPrimaryID.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later (The photo item is supported only in Windows Media Player 10 or later)<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





