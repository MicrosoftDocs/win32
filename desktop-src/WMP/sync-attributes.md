---
title: Sync Attributes
description: The Sync01 through Sync16 attributes are string representations of 32-bit values that Windows Media Player uses when it synchronizes playlists with one of up to 16 portable devices.
ms.assetid: b9ae3420-aa09-4969-8637-f16d438942f3
keywords:
- Sync Attributes Windows Media Player
topic_type:
- apiref
api_name:
- Sync
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Sync Attributes

The **Sync01** through **Sync16** attributes are string representations of 32-bit values that Windows Media Player uses when it synchronizes playlists with one of up to 16 portable devices.

## Applies To

-   [Playlists](playlist-attributes-ref.md)

## Remarks

These are read/write attributes. A value of zero indicates that Windows Media Player should not synchronize the playlist with the associated device. A value greater than zero indicates a synchronization priority for the given playlist.

Based on user input, Windows Media Player sets this attribute for each of the playlists in the library. When Windows Media Player attempts to synchronize a playlist with a portable device, it examines each playlist to compare the values for the **Sync***XX* attributes that represent the device partnership. Playlists that have lower **Sync***XX* values receive higher synchronization priority.

For example, the library might contain the following four playlists and respective **Sync***XX* values:



| Playlist Name | Sync01 Value |
|---------------|--------------|
| GymMusic.WPL  | 0x0000000D   |
| Relax.WPL     | 0x00000020   |
| DriveHome.WPL | 0x00000001   |
| NoGo.WPL      | 0x00000000   |



 

When Windows Media Player synchronizes the device associated with the attribute, it will synchronize the playlists in the following order:

1.  DriveHome.WPL
2.  GymMusic.WPL
3.  Relax.WPL

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> <dt>

[**Enumerating Synchronization Playlists**](enumerating-synchronization-playlists.md)
</dt> </dl>

 

 





