---
title: PLAYLIST.rightStatus
description: The rightStatus attribute specifies or retrieves the status text that is displayed on the right side and bottom of the PLAYLIST element.
ms.assetid: 82861572-ee8d-4780-a890-f018662499ff
keywords:
- PLAYLIST.rightStatus Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.rightStatus
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.rightStatus

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **rightStatus** attribute specifies or retrieves the status text that is displayed on the right side and bottom of the **PLAYLIST** element.

``` syntax
        elementID.rightStatus
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

 

 





