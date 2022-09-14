---
title: WM/Publisher Attribute
description: The WM/Publisher attribute is the name of the company that published the content.
ms.assetid: 5f3aa5de-237e-449c-918e-8750481adc6f
keywords:
- WM/Publisher Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/Publisher
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/Publisher Attribute

The **WM/Publisher** attribute is the name of the company that published the content.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [DVDs](dvd-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**Label**, **ReleasedBy**, and **Studio** are aliases for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMPublisher.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





