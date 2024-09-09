---
title: WM/MCDI
description: The WM/MCDI attribute contains the music CD identifier. This is a binary dump of the table of contents from the CD that is used to uniquely identify the CD.
ms.assetid: cb16c62b-b9e0-4676-b1bb-ff26a2e09cb7
keywords:
- WM/MCDI windows Media Format
topic_type:
- apiref
api_name:
- WM/MCDI
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/MCDI

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/MCDI** attribute contains the music CD identifier. This is a binary dump of the table of contents from the CD that is used to uniquely identify the CD.

## Global Constant

g\_wszWMMCDI

## Data Type

**WMT\_TYPE\_BINARY**

## Remarks

This attribute is compatible with the ID3 frame, MCDI. The ID3 specification for the MCDI frame requires that only one such frame exist per file and that a valid TRCK frame exist. The metadata editor does not perform any validation for these rules. Also, the size of WM/MCDI is not limited to 804 bytes, as is the MCDI ID3 frame.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




