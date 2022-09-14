---
title: WM/WMCollectionGroupID
description: The WM/WMCollectionGroupID attribute contains a GUID identifying the collection group.
ms.assetid: 5cfa1747-ce3b-4e8d-bcce-84fb719123e8
keywords:
- WM/WMCollectionGroupID windows Media Format
topic_type:
- apiref
api_name:
- WM/WMCollectionGroupID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/WMCollectionGroupID

The **WM/WMCollectionGroupID** attribute contains a GUID identifying the collection group.

## Global Constant

g\_wszWMWMCollectionGroupID

## Data Type

**WMT\_TYPE\_GUID**

## Remarks

Content is identified by Windows Media technologies by using three values: **WM/WMCollectionGroupID**, **WM/WMCollectionID**, and **WM/WMContentID**. These values identify the content, the collection to which it belongs, and the group to which the collection belongs. All three of these values are populated by Windows Media Player when metadata for the content is retrieved. You can have your application record these values and use them to identify content, but you should not change them if they are present.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




