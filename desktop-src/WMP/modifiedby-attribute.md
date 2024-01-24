---
title: ModifiedBy Attribute
description: A string that indicates whether the attributes of the item have been modified by the user.
ms.assetid: 6967e82e-a2db-4c2a-8572-35a4f52bc451
keywords:
- ModifiedBy Attribute Windows Media Player
topic_type:
- apiref
api_name:
- ModifiedBy
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ModifiedBy Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This attribute is no longer supported. The value is always empty or "user". \]

The **ModifiedBy** attribute is a string that indicates whether the attributes of the item have been modified by the user.

## Applies To

-   [DVDs](dvd-attributes.md)

## Remarks

This attribute is stored only in the digital media file.

To determine whether you can change the value of this attribute, use the [**Media.isReadOnlyItem**](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





