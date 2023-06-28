---
title: RadioBand Attribute
description: The RadioBand attribute is the frequency band of the radio station.
ms.assetid: 410dd263-93ff-41d3-9744-d38a4674dddf
keywords:
- RadioBand Attribute Windows Media Player
topic_type:
- apiref
api_name:
- RadioBand
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# RadioBand Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **RadioBand** attribute is the frequency band of the radio station.

## Applies To

-   [Radio Items](radio-item-attributes.md)

## Remarks

This attribute is stored only in the library.

This attribute has one of the following values: "FM", "AM", or "Net".

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------|
| Version<br/> | Windows Media Player 9 Series only<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





