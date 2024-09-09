---
title: Description (Windows Media Format 11 SDK)
description: The Description attribute contains a description of the content of the file.
ms.assetid: b9a1dcb1-9e8a-49a0-8dd5-388c929645c3
keywords:
- Description windows Media Format
topic_type:
- apiref
api_name:
- Description
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Description (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Description** attribute contains a description of the content of the file.

## Global Constant

g\_wszWMDescription

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This is a file-level attribute.

For ID3v1 MP3 files, this attribute is limited to 30 characters.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




