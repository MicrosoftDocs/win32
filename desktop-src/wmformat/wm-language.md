---
title: WM/Language
description: The WM/Language attribute contains the language of the stream.
ms.assetid: 840f95b0-c8f2-4da6-9a76-3870b2325a42
keywords:
- WM/Language windows Media Format
topic_type:
- apiref
api_name:
- WM/Language
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/Language

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/Language** attribute contains the language of the stream.

## Global Constant

g\_wszWMLanguage

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

The language string used should be compliant with RFC 1766. For more information, see [Language Strings](language-strings.md).

### Example



| File type | Example value |
|-----------|---------------|
| All       | "en-us"       |



 

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




