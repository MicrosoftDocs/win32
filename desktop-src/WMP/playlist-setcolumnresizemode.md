---
title: PLAYLIST.setColumnResizeMode
description: The setColumnResizeMode method specifies how the indexed column sizes itself.
ms.assetid: 84ca0e60-ca24-4058-ae08-5b9cf3d7c38f
keywords:
- PLAYLIST.setColumnResizeMode Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.setColumnResizeMode
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.setColumnResizeMode

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setColumnResizeMode** method specifies how the indexed column sizes itself.

``` syntax
        elementID.setColumnResizeMode(column, mode)
```

## Parameters

<dl> <dt>

<span id="column"></span><span id="COLUMN"></span>*column*
</dt> <dd>

**Number** (**long**) indicating the index of the column to be changed.

</dd> <dt>

<span id="mode"></span><span id="MODE"></span>*mode*
</dt> <dd>

**String** indicating the sizing mode. Contains one of the following values.



| Value          | Description                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------|
| AutosizeHeader | The column resizes to accommodate all data in both the column and the header.                                  |
| AutosizeData   | The column resizes to accommodate all data in the column only.                                                 |
| Fixed          | The column is a fixed size.                                                                                    |
| Stretches      | The column resizes to use the remaining space in the **PLAYLIST** element after all other columns are resized. |



 

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
</dt> </dl>

 

 





