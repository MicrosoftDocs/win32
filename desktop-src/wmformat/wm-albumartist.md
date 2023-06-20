---
title: WM/AlbumArtist
description: The WM/AlbumArtist attribute contains the name of the primary artist for the album.
ms.assetid: 53675c06-313b-41f8-971b-ccd18f37e987
keywords:
- WM/AlbumArtist windows Media Format
topic_type:
- apiref
api_name:
- WM/AlbumArtist
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/AlbumArtist

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/AlbumArtist** attribute contains the name of the primary artist for the album.

## Global Constant

g\_wszWMAlbumArtist

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

For albums where the tracks may have different artists, such as tribute albums or collaborative albums, this attribute can be used to specify the primary artist of the album. It is preferable to use this attribute rather than using an author value of "various artists".

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




