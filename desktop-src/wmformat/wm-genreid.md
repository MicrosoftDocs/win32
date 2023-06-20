---
title: WM/GenreID
description: The WM/GenreID attribute contains a genre identifier compliant with the contents of the TCON tag in ID3v2.
ms.assetid: 2f2a87f7-ba2d-465a-a36b-a8f58b5dd2d0
keywords:
- WM/GenreID windows Media Format
topic_type:
- apiref
api_name:
- WM/GenreID
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/GenreID

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/GenreID** attribute contains a genre identifier compliant with the contents of the TCON tag in ID3v2. This should contain the genre ID in parentheses, optionally followed by a refinement further describing the genre. For more information, refer to the ID3v2 specification.

## Global Constant

g\_wszWMGenreID

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

The preferred attribute for specifying a genre is [**WM/Genre**](wm-genre.md). Use it in preference to this attribute.

If you change either **WM/Genre** or **WM/GenreID** in an MP3 file, the other attribute will be changed to match.

### Example



| File type | Example value   |
|-----------|-----------------|
| Audio     | "(4) Eurodisco" |



 

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




