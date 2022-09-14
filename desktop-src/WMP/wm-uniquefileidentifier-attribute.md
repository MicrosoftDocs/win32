---
title: WM/UniqueFileIdentifier Attribute
description: The WM/UniqueFileIdentifier attribute is a string that uniquely identifies the item.
ms.assetid: 8196fc38-05dc-4c9e-98cb-1e160ce28a9a
keywords:
- WM/UniqueFileIdentifier Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/UniqueFileIdentifier
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/UniqueFileIdentifier Attribute

The **WM/UniqueFileIdentifier** attribute is a string that uniquely identifies the item.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**UniqueFileIdentifier** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMUniqueFileIdentifier.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





