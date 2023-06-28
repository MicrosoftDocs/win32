---
title: LISTBOX.setSelectedState
description: The setSelectedState method selects or unselects the item with the specified index.
ms.assetid: a72aa461-f378-4612-b580-ecad735931cb
keywords:
- LISTBOX.setSelectedState Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.setSelectedState
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# LISTBOX.setSelectedState

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setSelectedState** method selects or unselects the item with the specified index.

``` syntax
        elementID.setSelectedState(index, selected)
```

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number** (**long**) containing the index of the item to select or unselect.

</dd> <dt>

<span id="selected"></span><span id="SELECTED"></span>*selected*
</dt> <dd>

**Boolean** value indicating whether the item is to be selected (true) or unselected (false).

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

This is used to select or unselect multiple lines.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> </dl>

 

 





