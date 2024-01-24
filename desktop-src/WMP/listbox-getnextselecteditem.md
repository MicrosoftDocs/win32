---
title: LISTBOX.getNextSelectedItem
description: The getNextSelectedItem method retrieves the next selected item in the list box control starting at the item after the one with the specified index.
ms.assetid: 060d196d-2b14-4386-ba01-34256c137db5
keywords:
- LISTBOX.getNextSelectedItem Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.getNextSelectedItem
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# LISTBOX.getNextSelectedItem

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getNextSelectedItem** method retrieves the next selected item in the list box control starting at the item after the one with the specified index.

``` syntax
        elementID.getNextSelectedItem(startIndex)
```

## Parameters

<dl> <dt>

<span id="startIndex"></span><span id="startindex"></span><span id="STARTINDEX"></span>*startIndex*
</dt> <dd>

**Number** (**long**) containing the index of the item that precedes the item being retrieved.

</dd> </dl>

## Return Value

This method returns a **Number** (**long**) containing the index of the next selected item.

## Remarks

To start search from the beginning, use  1 for the start index.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> </dl>

 

 





