---
title: WM/WMContentID
description: The WM/WMContentID attribute contains a GUID identifying the content.
ms.assetid: b46d02f4-04f5-430a-b3f7-0f80e03bed2c
keywords:
- WM/WMContentID windows Media Format
topic_type:
- apiref
api_name:
- WM/WMContentID
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM/WMContentID

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WM/WMContentID** attribute contains a GUID identifying the content.

## Global Constant

g\_wszWMWMContentID

## Data Type

**WMT\_TYPE\_GUID**

## Remarks

Content is identified by Windows Media technologies by using three values: **WM/WMCollectionGroupID**, **WM/WMCollectionID**, and **WM/WMContentID**. These values identify the content, the collection to which it belongs, and the group to which the collection belongs. All three of these values are populated by Windows Media Player when metadata for the content is retrieved. You can have your application record these values and use them to identify content, but you should not change them if they are present.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




