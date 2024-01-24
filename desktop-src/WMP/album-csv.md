---
title: album.csv
description: album.csv
ms.assetid: 7308e849-7227-480e-937a-8e9091bdec98
keywords:
- Windows Media Player online stores,album.csv
- online stores,album.csv
- type 1 online stores,album.csv
- album.csv
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# album.csv

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This file contains an entry for each album included in the catalog. Each entry is a row composed of the tab-delimited fields described in the table below. Fields must appear in the order listed.

All fields in album.csv are required.

The Format column in the table below describes the way each Unicode text field is formatted. It does not refer to the data type of the contents. For example, if Integer is indicated in the Format column, it means that the field contains a Unicode string representing an integral value, rather than an actual integer.



| Field             | Format                                                                   | Description                                                                                                                                                                                                                                          |
|-------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AlbumID           | Non-negative integer.Example: 789456<br/>                          | Identifier for the album, unique within album.csv. Must be less than 2^32.                                                                                                                                                                           |
| AlbumName         | Unicode string.Example: Greatest Hits<br/>                         | Album title                                                                                                                                                                                                                                          |
| AlbumArtist       | Non-negative integer.Example: 34331<br/>                           | ArtistID of the artist. Only one value is allowed. Can be the ID of "Various Artists" or similar.                                                                                                                                                    |
| AlbumLabel        | Unicode string. Should be empty.                                         | Not used in this release. Should be empty.                                                                                                                                                                                                           |
| ReleaseDate       | Unicode string, in format YYYY-MM-DD.Example: 2005-0-0<br/>        | Release date. The value 0 is allowed for day or month.                                                                                                                                                                                               |
| AlbumPrice        | Unicode stringExample: $12.49<br/>                                 | Album price. The currency symbol should be included. The empty string, 0, and - have special meaning. An empty string indicates an unknown price. '0' indicates that the track is free. A hyphen ('-') indicates that the album cannot be purchased. |
| LinkedGenreID     | Non-negative integer.Example: 12<br/>                              | ID of primary genre for the album. Only one value is allowed.                                                                                                                                                                                        |
| LinkedSubGenreIDs | Format: n;n;n;Example: 32;44;663;<br/>                             | List of associated subgenre IDs. A trailing semicolon is allowed at the end of the list.                                                                                                                                                             |
| Popularity        | Can be non-negative integer or decimal value.Example: 1256.24<br/> | Popularity rating determined by the service. Can be the ranking of this album in the list of albums sorted by popularity. 0 is allowed.                                                                                                              |
| IsRecentlyAdded   | Boolean. Can be 0 or 1.                                                  | Flag to indicate that the album was recently added, as determined by the service.                                                                                                                                                                    |
| IsFeatured        | Boolean. Can be 0 or 1.                                                  | Flag to indicate that this is a featured album.                                                                                                                                                                                                      |
| EditorialGlyph    | Non-negative integer. Should be 0.                                       | Not used is release. Should be 0.                                                                                                                                                                                                                    |
| FeedsAreAvailable | Boolean. Can be 0 or 1.                                                  | Not used in this release. Should be 0.                                                                                                                                                                                                               |



 

 

 





