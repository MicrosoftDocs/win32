---
title: PLAYLIST.copy
description: The copy method begins a copy operation from the CD.
ms.assetid: 7d919ae5-456b-4cb9-ad52-9396f5c867d6
keywords:
- PLAYLIST.copy Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.copy
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PLAYLIST.copy

The **copy** method begins a copy operation from the CD.

``` syntax
        elementID.copy()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Remarks

This method copies only the checked items in the playlist, and works the same way as in the **Copy from CD** pane in the full mode of Windows Media Player. For this method to work, a CD must be in the CD drive. Set the **checkboxesVisible** attribute to true to allow users to select individual items on a CD before copying.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.abortCopy**](playlist-abortcopy.md)
</dt> <dt>

[**PLAYLIST.copying**](playlist-copying.md)
</dt> </dl>

 

 





