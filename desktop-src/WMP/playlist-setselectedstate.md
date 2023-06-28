---
title: PLAYLIST.setSelectedState
description: The setSelectedState method specifies that the indexed item in the playlist is selected.
ms.assetid: 61770053-733f-40b5-8b1f-92b6975d3ad3
keywords:
- PLAYLIST.setSelectedState Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.setSelectedState
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.setSelectedState

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setSelectedState** method specifies that the indexed item in the playlist is selected.

``` syntax
        elementID.setSelectedState(item)
```

## Parameters

<dl> <dt>

<span id="item"></span><span id="ITEM"></span>*item*
</dt> <dd>

**Number** (**long**) indicating the index of an item in the playlist.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

You can set all items to the selected state by specifying  1 in the *item* parameter.

This method has been replaced by **setSelectedState2**, which supports nested playlists.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.setSelectedState2**](playlist-setselectedstate2.md)
</dt> </dl>

 

 





