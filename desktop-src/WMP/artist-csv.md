---
title: artist.csv
description: artist.csv
ms.assetid: 50cf2fbc-28cc-4b13-988e-4c02eb821cfd
keywords:
- Windows Media Player online stores,artist.csv
- online stores,artist.csv
- type 1 online stores,artist.csv
- artist.csv
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# artist.csv

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This file contains an entry for each artist in the catalog. Each entry is a row composed of the tab-delimited fields described in the table below. Fields must appear in the order listed.

All fields in artist.csv are required.

The Format column in the table below describes the way each Unicode text field is formatted. It does not refer to the data type of the contents. For example, if Integer is indicated in the Format column, it means that the field contains a Unicode string representing an integral value, rather than an actual integer.



| Field                  | Format                                            | Description                                                                                                |
|------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ArtistID               | Non-negative integer. Example: 65832              | Unique identifier for the artist, unique within artist.csv. Must be less than 2^32.                        |
| ArtistName             | Unicode string.Example: Don Funk<br/>       | Display name for the artist.                                                                               |
| LinkedGenreID          | Non-negative integer.Example: 313<br/>      | GenreID of the artist's primary genre. Must be a main genre and not a subgenre. Only one value is allowed. |
| LinkedSimilarArtistIDs | N/A                                               | Not used in this release. Should be empty.                                                                 |
| Popularity             | Can be integer or decimal value. Example: 1252.25 | Popularity ranking. Can be the position in the list when sorted by popularity.                             |
| FeedsAvailable         | Boolean. Format: \[0\|1\]Example: 0<br/>    | Not used in this release. Should be empty.                                                                 |



 

 

 





