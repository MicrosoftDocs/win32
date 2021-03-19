---
title: SyncOnly Attribute
description: The SyncOnly attribute is a string representation of a Boolean value that Windows Media Player uses to determine whether a playlist is available only for synchronization.
ms.assetid: 36149bb9-3a0b-4f6d-8be3-97d2a87faa83
keywords:
- SyncOnly Attribute Windows Media Player
topic_type:
- apiref
api_name:
- SyncOnly
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SyncOnly Attribute

The **SyncOnly** attribute is a string representation of a **Boolean** value that Windows Media Player uses to determine whether a playlist is available only for synchronization.

## Applies To

-   [Playlists](playlist-attributes-ref.md)

## Remarks

A value of 1 indicates that the playlist is available only for synchronization and cannot appear in the **Auto Playlist** node. A value of zero indicates that the playlist can appear in the **Auto Playlist** node.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





