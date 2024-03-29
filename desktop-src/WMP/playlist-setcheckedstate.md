---
title: PLAYLIST.setCheckedState
description: The setCheckedState method specifies that the indexed item in the playlist is checked.
ms.assetid: ce5de21b-6354-485e-b6f7-f4d090c149f7
keywords:
- PLAYLIST.setCheckedState Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.setCheckedState
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.setCheckedState

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setCheckedState** method specifies that the indexed item in the playlist is checked.

``` syntax
        elementID.setCheckedState(item)
```

## Parameters

<dl> <dt>

<span id="item"></span><span id="ITEM"></span>*item*
</dt> <dd>

**Number** (**long**) indicating the index of the playlist item to be checked.

</dd> </dl>

## Return Value

This method returns a **Boolean**.

## Remarks

You can set all items to the checked state by specifying  1 in the *item* parameter.

This method has been replaced by **setCheckedState2**, which supports nested playlists.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.setCheckedState2**](playlist-setcheckedstate2.md)
</dt> </dl>

 

 





