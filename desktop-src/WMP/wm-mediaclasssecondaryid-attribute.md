---
title: WM/MediaClassSecondaryID Attribute
description: The WM/MediaClassSecondaryID attribute is a GUID specifying the secondary media class, which is a subclass of the primary media class.
ms.assetid: 8112513a-b73a-497a-9c24-24ccef31cffc
keywords:
- WM/MediaClassSecondaryID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/MediaClassSecondaryID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/MediaClassSecondaryID Attribute

The **WM/MediaClassSecondaryID** attribute is a GUID specifying the secondary media class, which is a subclass of the primary media class.

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

The following table lists the supported GUIDs and their descriptions.



| GUID                                 | Description                                    |
|--------------------------------------|------------------------------------------------|
| D0E20D5C-CAD6-4F66-9FA1-6018830F1DCC | The media object represents a static playlist. |
| EB0BAFB6-3C4F-4C31-AA39-95C7B8D7831D | The media object represents an auto playlist.  |



 

**MediaClassSecondaryID** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMMediaClassSecondaryID.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | The photo item is supported only in Windows Media Player 10 or later The radio item is supported only in Windows Media Player 9 Series All other items are supported in Windows Media Player 9 Series and later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





