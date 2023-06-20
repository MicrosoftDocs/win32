---
title: WM/UniqueFileIdentifier
description: The WM/UniqueFileIdentifier attribute contains a unique file identifier for the content.
ms.assetid: 3f90dd5c-0f3d-451a-a454-f8d7f25b6201
keywords:
- WM/UniqueFileIdentifier windows Media Format
topic_type:
- apiref
api_name:
- WM/UniqueFileIdentifier
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/UniqueFileIdentifier

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/UniqueFileIdentifier** attribute contains a unique file identifier for the content.

## Global Constant

g\_wszWMUniqueFileIdentifier

## Data Type

**WM\_TYPE\_STRING**

## Remarks

The unique file identifier is a generic string that can be used by applications and services to uniquely identify the file. The string contains semicolon-delimited arbitrary values. You should never clear this attribute. You can append values and remove your own values, but all others should be left unaltered.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




