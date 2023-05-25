---
title: listitem.csv
description: listitem.csv
ms.assetid: d8f4bdb3-e7a5-4080-9ae7-555bf3695e9c
keywords:
- Windows Media Player online stores,listitem.csv
- online stores,listitem.csv
- type 1 online stores,listitem.csv
- listitem.csv
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# listitem.csv

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This file contains entries for each item that is included in a list. Each entry is a row composed of the tab-delimited fields described in the table below. Fields must appear in the order listed.

All fields are required.

The Format column in the table below describes the way each Unicode text field is formatted. It does not refer to the data type of the contents. For example, if Integer is indicated in the Format column, it means that the field contains a Unicode string representing an integral value, rather than an actual integer.



| Field              | Format                                          | Description                                                                                                            |
|--------------------|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Linked\_ListID     | Non-negative integer.Example: 465<br/>    | The ID of the list this item is part of.                                                                               |
| Linked\_ListItem   | Non-negative integer.Example: 684793<br/> | The ID of the item. Can be the ID of a track, an album, an artist, a genre, a subgenre, a radio feed, or another list. |
| ItemPositionInList | Non-negative integer.Example: 5<br/>      | The position of the item within its list. The first item in a list is at position 0.                                   |



 

 

 





