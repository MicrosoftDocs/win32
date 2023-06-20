---
title: Rating
description: The Rating attribute contains the rating of the content.
ms.assetid: 3de28d65-9c81-4290-8b57-ceac5ab52f8d
keywords:
- Rating windows Media Format
topic_type:
- apiref
api_name:
- Rating
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Rating

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Rating attribute contains the rating of the content.

## Global Constant

g\_wszWMRating

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This is a file-level attribute.

Individual implementations in existing files use different scales and notations. Because of this, you should avoid using this attribute; there is no standardization from which to develop consistent user interfaces.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




