---
title: PLAYLIST.columns
description: The columns attribute defines the columns that appear in the PLAYLIST element.
ms.assetid: a805ee06-cf73-4eab-bcda-c374e55cd11a
keywords:
- PLAYLIST.columns Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.columns
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.columns

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **columns** attribute defines the columns that appear in the **PLAYLIST** element.

``` syntax
        elementID.columns
```

## Possible Values

This attribute is a read/write **String** in the following format:

DB\_NAME=FRIENDLY\_NAME;DB\_NAME=FRIENDLY\_NAME;

FRIENDLY\_NAME is the value shown in the column header of the PLAYLIST element, and DB\_NAME is a value from the following table. Note that a Playlist item might be a media item from the library or from a CD, or it might be another **Playlist** that is either user-created or taken from a CD. Some columns are valid only with certain Playlist items as indicated in the Description column.



| Value             | Description                                                                                                             |
|-------------------|-------------------------------------------------------------------------------------------------------------------------|
| Album             | The name of the album. Used with media items only.                                                                      |
| Artist            | The name of the artist. Not used with user-created playlists.                                                           |
| Author            | The name of the artist.                                                                                                 |
| Bitrate           | The bit rate of the content. Used only with media items from the library.                                               |
| CDTrackEnabled    | Indicates whether the CD track is enabled. Used only with CD media items.                                               |
| Checked           | Reserved for future use.                                                                                                |
| Copyright         | The copyright of the playlist. Not used with CD playlists or media items.                                               |
| CreationDate      | The date and time that the entry in the library was created. Used only with items from the library.                     |
| DigitallySecure   | Indicates whether the item is protected with Windows Media Rights Manager. Used only with media items from the library. |
| Duration          | The duration of the media item.                                                                                         |
| FileType          | Reserved for future use.                                                                                                |
| Genre             | The genre of the playlist. Not used with playlists from CDs.                                                            |
| MediaAttribute    | Reserved for future use.                                                                                                |
| MediaType         | The type of the media item (audio or video).                                                                            |
| MetadataSource    | The source of the metadata for this CD track (AMG, WindowsMedia.com, and so on). Used only with CD media items.         |
| ModifiedBy        | Reserved for future use.                                                                                                |
| Name              | The name of the playlist.                                                                                               |
| OriginalIndex     | If applicable, the corresponding CD track identifier. Used only with CD media items.                                    |
| PlayCount         | The number of times the content has been played through to the end. Used only with media items from the library.        |
| PlaylistAttribute | Reserved for future use.                                                                                                |
| Rating            | Reserved for future use.                                                                                                |
| SourceURL         | The path or URL to the content. Used only with media items from the library.                                            |
| Status            | The copying status of a CD track being copied. Used only with CD media items.                                           |
| Style             | Reserved for future use.                                                                                                |
| TOC               | If applicable, the corresponding CD Table of Contents Identifier. Not used with user-created playlists.                 |



 

## Remarks

If one of the columns does not exist in the library, it is left blank.

A maximum of 31 columns may be specified.

If you specify a duplicate column, the data in the first column will be left-aligned but all other duplicate columns will be right-aligned. For example, if you have two duration columns, the data will be left-aligned in the first and right-aligned in the second.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.columnsVisible**](playlist-columnsvisible.md)
</dt> </dl>

 

 





