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
ms.date: 05/31/2018
---

# WM/Genre

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

 

 




