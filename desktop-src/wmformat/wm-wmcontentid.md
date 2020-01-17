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
ms.date: 05/31/2018
---

# WM/WMContentID

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

 

 




