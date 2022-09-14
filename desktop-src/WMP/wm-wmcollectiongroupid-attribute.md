---
title: WM/WMCollectionGroupID Attribute
description: The WM/WMCollectionGroupID attribute is a GUID identifying the group containing the collection to which the item belongs.
ms.assetid: 5383fb12-fc16-474e-b9a0-c1e69b86a057
keywords:
- WM/WMCollectionGroupID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/WMCollectionGroupID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/WMCollectionGroupID Attribute

The **WM/WMCollectionGroupID** attribute is a GUID identifying the group containing the collection to which the item belongs.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**WMCollectionGroupID** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMCollectionGroupID.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





