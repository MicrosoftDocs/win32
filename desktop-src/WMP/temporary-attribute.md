---
title: Temporary Attribute
description: The Temporary attribute specifies whether a playlist is temporary.
ms.assetid: 0d967a70-97d1-4918-8068-fe2868ab41d2
keywords:
- Temporary Attribute Windows Media Player
topic_type:
- apiref
api_name:
- Temporary
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Temporary Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Temporary** attribute specifies whether a playlist is temporary.

**Remarks**

If you retrieved a playlist from the library, changes you make to the playlist will be reflected in the user's library. To avoid this, call [IWMPPlaylist::setItemInfo](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplaylist-setiteminfo) passing the attribute name "Temporary" and the value "true". This converts your playlist instance to a temporary playlist, which is safe to edit without changing the original playlist.

**Applies To**

-   [Playlists](playlist-attributes-ref.md)

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





