---
title: DRMKeyID Attribute
description: The DRMKeyID attribute identifies the media usage rights for content that is protected using digital rights management (DRM).
ms.assetid: 37d2ddf9-9b87-42fd-84c0-0bd2a256056a
keywords:
- DRMKeyID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- DRMKeyID
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRMKeyID Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRMKeyID** attribute identifies the media usage rights for content that is protected using digital rights management (DRM).

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

Typically this attribute is used for querying and displaying media usage rights.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





