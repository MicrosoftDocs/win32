---
title: WM/SubTitle Attribute
description: The WM/SubTitle attribute is the subtitle of the content.
ms.assetid: b1bd9a90-7ff5-4cc3-a141-839f4eaaa407
keywords:
- WM/SubTitle Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/SubTitle
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/SubTitle Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/SubTitle** attribute is the subtitle of the content.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

**SubTitle** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMSubTitle.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





