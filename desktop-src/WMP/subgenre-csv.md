---
title: subgenre.csv
description: subgenre.csv
ms.assetid: 3ba51cda-0c29-4ce9-9237-8444225349c8
keywords:
- Windows Media Player online stores,subgenre.csv
- online stores,subgenre.csv
- type 1 online stores,subgenre.csv
- subgenre.csv
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# subgenre.csv

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This file contains an entry for each subgenre represented in the catalog. Each entry is a row composed of the tab-delimited fields described in the table below. Fields must appear in the order listed.

The Format column in the table below describes the way each Unicode text field is formatted. It does not refer to the data type of the contents. For example, if Integer is indicated in the Format column, it means that the field contains a Unicode string representing an integral value, rather than an actual integer.



| Field             | Required | Format                                                                                            | Description                                                                                                                                               |
|-------------------|----------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| SubGenreID        | Yes      | Non-negative integer.                                                                             | Subgenre identifier (ID), unique within subgenre.csv. Up to 1024 subgenres are allowed.                                                                   |
| SubGenreTitle     | Yes      | Unicode string.Example: Intelligent Dance Music (IDM)<br/>                                  | Subgenre display name.                                                                                                                                    |
| SubGenreSubtitle  | No       | Unicode string.Example: New, percussive electronic music that's not quite pure techno.<br/> | Describe the meaning of the subgenre display name. Should be less than 64 characters.                                                                     |
| FeedsAreAvailable | Yes      | Boolean.Format: \[0\|1\]<br/> Example: 0<br/>                                         | Indicates whether "radio play" is possible by jumping to a feed.                                                                                          |
| Linked\_GenreID   | Yes      | Non-negative integer (GenreID).Example: 12<br/>                                             | The GenreID of the parent genre. Only one parent is allowed.                                                                                              |
| SortOrderRank     | Yes      | Non-negative integer.Example: 23<br/>                                                       | A ranking, ideally unique, used for sorting subgenres in the user interface. If the parent genre has 10 subgenres, this might be an integer from 1 to 10. |



 

 

 





