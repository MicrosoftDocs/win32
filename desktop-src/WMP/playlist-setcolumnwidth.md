---
title: PLAYLIST.setColumnWidth
description: The setColumnWidth method specifies the column width and changes the resize mode of the column to \ 0034;Fixed \ 0034;.
ms.assetid: 6eebea0a-48f2-4300-b535-78744db6fea4
keywords:
- PLAYLIST.setColumnWidth Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.setColumnWidth
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.setColumnWidth

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setColumnWidth** method specifies the column width and changes the resize mode of the column to "Fixed".

``` syntax
        elementID.setColumnWidth(column, width)
```

## Parameters

<dl> <dt>

<span id="column"></span><span id="COLUMN"></span>*column*
</dt> <dd>

**Number** (**long**) indicating the index of the column being changed.

</dd> <dt>

<span id="width"></span><span id="WIDTH"></span>*width*
</dt> <dd>

**Number** (**long**) indicating the new width in pixels.

</dd> </dl>

## Return Value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.setColumnResizeMode**](playlist-setcolumnresizemode.md)
</dt> </dl>

 

 





