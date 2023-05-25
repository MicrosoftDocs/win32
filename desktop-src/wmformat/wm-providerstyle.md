---
title: WM/ProviderStyle
description: The WM/ProviderStyle attribute contains the style of the file as assigned by the metadata content provider.
ms.assetid: 3bf6811e-a527-4ec7-b330-6e0eabab485a
keywords:
- WM/ProviderStyle windows Media Format
topic_type:
- apiref
api_name:
- WM/ProviderStyle
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/ProviderStyle

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/ProviderStyle** attribute contains the style of the file as assigned by the metadata content provider.

## Global Constant

g\_wszWMProviderStyle

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This attribute is essentially a second genre designation. Because different classifiers have different notions of the genres associated with content, the provider style may be different than the genre assigned by the content creator.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> <dt>

[**WM/Genre**](wm-genre.md)
</dt> <dt>

[**WM/GenreID**](wm-genreid.md)
</dt> </dl>

 

 




