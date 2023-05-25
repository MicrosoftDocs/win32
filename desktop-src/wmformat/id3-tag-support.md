---
title: ID3 Tag Support
description: ID3 Tag Support
ms.assetid: 57119b88-5901-4bea-abf6-a67fe71afd1b
keywords:
- Windows Media Format SDK,attributes
- Advanced Systems Format (ASF),attributes
- ASF (Advanced Systems Format),attributes
- attributes,ID3 tags
- ID3 tags
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ID3 Tag Support

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table lists all of the attributes that correspond to ID3 tags. If you want to use the ID3 tags as attributes rather than using the standard attribute names, add the prefix "ID3/" to the tag name. For example, "ID3/TPE2" is equivalent to **Author**.



| Attribute                      | ID3v1.x | ID3v2.2 | ID3v2.3/v2.4 |
|--------------------------------|---------|---------|--------------|
| **Author**                     | Artist  | TP1     | TPE1         |
| **Copyright**                  |         | TCR     | TCOP         |
| **CopyrightURL**               |         | WCP     | WCOP         |
| **Description**                | Comment | COM     | COMM         |
| **Duration**                   |         | TLE     | TLEN         |
| **FileSize**                   |         |         | TSIZ         |
| **Title**                      | Title   | TT2     | TIT2         |
| **WM/AlbumArtist**             |         | TP2     | TPE2         |
| **WM/AlbumSortOrder**          |         |         | TSOA         |
| **WM/AlbumTitle**              | Album   | TAL     | TALB         |
| **WM/ArtistSortOrder**         |         |         | TSOP         |
| **WM/AudioFileURL**            |         | WAF     | WOAF         |
| **WM/AudioSourceURL**          |         | WAS     | WOAS         |
| **WM/AuthorURL**               |         | WAR     | WOAR         |
| **WM/BeatsPerMinute**          |         |         | TBPM         |
| **WM/Binary**                  |         | GEO     | GEOB         |
| **WM/Comments**                |         | COM     | COMM         |
| **WM/Composer**                |         | TCM     | TCOM         |
| **WM/Conductor**               |         | TP3     | TPE3         |
| **WM/ContentGroupDescription** |         | TT1     | TIT1         |
| **WM/EncodedBy**               |         | TEN     | TENC         |
| **WM/EncodingSettings**        |         | TSS     | TSSE         |
| **WM/EncodingTime**            |         |         | TDEN         |
| **WM/GenreID**                 | GenreID | TCO     | TCON         |
| **WM/InitialKey**              |         |         | TKEY         |
| **WM/ISRC**                    |         |         | TSRC         |
| **WM/Language**                |         | TLA     | TLAN         |
| **WM/Lyrics\_Synchronised**    |         | SLT     | SYLT         |
| **WM/MCDI**                    |         |         | MCDI         |
| **WM/ModifiedBy**              |         |         | TPE4         |
| **WM/Mood**                    |         |         | TMOO         |
| **WM/OriginalAlbumTitle**      |         | TOT     | TOAL         |
| **WM/OriginalArtist**          |         | TOA     | TOPE         |
| **WM/OriginalFilename**        |         | TOF     | TOFN         |
| **WM/OriginalLyricist**        |         | TOL     | TOLY         |
| **WM/OriginalReleaseYear**     |         | TOR     | TORY         |
| **WM/PartOfSet**               |         | TPA     | TPOS         |
| **WM/Picture**                 |         | PIC     | APIC         |
| **WM/PlaylistDelay**           |         |         | TDLY         |
| **WM/Publisher**               |         | TPB     | TPUB         |
| **WM/RadioStationName**        |         | TRN     | TRSN         |
| **WM/RadioStationOwner**       |         | TRO     | TRSO         |
| **WM/SetSubTitle**             |         |         | TSST         |
| **WM/SubTitle**                |         | TT3     | TIT3         |
| **WM/Text**                    |         | TXX     | TXXX         |
| **WM/TitleSortOrder**          |         |         | TSOT         |
| **WM/TrackNumber**             | Track   | TRK     | TRCK         |
| **WM/UniqueFileIdentifier**    |         | UFI     | UFID         |
| **WM/UserWebURL**              |         | WXX     | WXXX         |
| **WM/Writer**                  |         | TXT     | TEXT         |
| **WM/Year**                    | Year    | TYE     | TYER         |



 

## Related topics

<dl> <dt>

[**Attributes**](attributes.md)
</dt> </dl>

 

 




