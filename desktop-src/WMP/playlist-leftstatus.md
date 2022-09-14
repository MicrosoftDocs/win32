---
title: PLAYLIST.leftStatus
description: The leftStatus attribute specifies or retrieves the status text that is displayed on the left side and bottom of the PLAYLIST element.
ms.assetid: c83f4fd1-d0e6-4822-9208-8e968c409a78
keywords:
- PLAYLIST.leftStatus Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.leftStatus
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PLAYLIST.leftStatus

The **leftStatus** attribute specifies or retrieves the status text that is displayed on the left side and bottom of the **PLAYLIST** element.

``` syntax
        elementID.leftStatus
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

This attribute can combine any text with specific keywords that will display the desired information, such as the total duration of the playlist. The keywords are surrounded by percentage symbols (%) to keep them distinct from the ordinary text.

The following keywords can be used.



| Keyword               | Description                                                                                                                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| count                 | Number of items in the playlist.                                                                                                                                                                             |
| size                  | Total size of the playlist.                                                                                                                                                                                  |
| duration              | Total duration of the playlist.                                                                                                                                                                              |
| *XXX*                 | Does a **getItemInfo** on the playlist with *XXX* being the item to receive.                                                                                                                                 |
| SelectedSize          | Total size of the selected entries in the playlist.                                                                                                                                                          |
| SelectedCount         | Total number of selected entries in the playlist.                                                                                                                                                            |
| SelectedDuration      | Total duration of the selected entries in the playlist.                                                                                                                                                      |
| CheckedCount          | Total number of checked tracks in the playlist.                                                                                                                                                              |
| CheckedDuration       | Total duration of the checked tracks in the playlist.                                                                                                                                                        |
| CheckedSize           | Total size of the checked tracks in the playlist.                                                                                                                                                            |
| DurationString        | Displays text that describes the duration as "Total Time" or "Estimated Time", depending on whether the total values are known. This text is followed by "%duration%".                                       |
| CheckedDurationString | Displays text that describes the duration for all checked items in the playlist as "Total Time" or "Estimated Time", depending on whether the total values are known. This text is followed by "%duration%". |



 

The value "Total Time: %duration%" for a playlist that contains a total duration of seven minutes will display "Total Time: 07:00".

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





