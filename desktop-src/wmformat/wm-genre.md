---
title: WM/Genre
description: The WM/Genre attribute contains the genre of the content.
ms.assetid: 50279c96-e8f2-40a3-9d5b-5827eb91b61e
keywords:
- WM/Genre windows Media Format
topic_type:
- apiref
api_name:
- WM/Genre
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/Genre

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/Genre** attribute contains the genre of the content.

## Global Constant

g\_wszWMGenre

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This is the preferred attribute for specifying the genre of content.

If you change either **WM/Genre** or **WM/GenreID** in an MP3 file, the other attribute will be changed to match.

### Example



| File type | Example value |
|-----------|---------------|
| Audio     | "Rock"        |
| Video     | "Drama"       |



 

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




