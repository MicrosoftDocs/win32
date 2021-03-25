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
ms.date: 05/31/2018
---

# Temporary Attribute

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

 

 





