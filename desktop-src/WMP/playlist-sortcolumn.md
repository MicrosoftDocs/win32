---
title: PLAYLIST.sortColumn
description: The sortColumn method sorts the data in the specified column.
ms.assetid: 1563fee8-044a-4cb4-a9c2-11d4533536da
keywords:
- PLAYLIST.sortColumn Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.sortColumn
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.sortColumn

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **sortColumn** method sorts the data in the specified column.

``` syntax
        elementID.sortColumn(column)
```

## Parameters

<dl> <dt>

<span id="column"></span><span id="COLUMN"></span>*column*
</dt> <dd>

**Number** (**long**) indicating the index of the column to sort.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

This method sorts the specified column in the same way as the column header buttons in the **PLAYLIST** element. If the column has not yet been sorted, it is sorted in alphanumeric order. If it has been sorted, its order is reversed.

For this method to work, the **allowColumnSorting** attribute must be set to true.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.allowColumnSorting**](playlist-allowcolumnsorting.md)
</dt> </dl>

 

 





