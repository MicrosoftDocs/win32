---
title: WM/WMCollectionID
description: The WM/WMCollectionID attribute contains a GUID identifying the collection.
ms.assetid: 088fe2d7-e2d9-42a3-8deb-1d7948ff7df9
keywords:
- WM/WMCollectionID windows Media Format
topic_type:
- apiref
api_name:
- WM/WMCollectionID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/WMCollectionID

The **WM/WMCollectionID** attribute contains a GUID identifying the collection.

## Global Constant

g\_wszWMWMCollectionID

## Data Type

**WMT\_TYPE\_GUID**

## Remarks

Content is identified by Windows Media technologies by using three values: **WM/WMCollectionGroupID**, **WM/WMCollectionID**, and **WM/WMContentID**. These values identify the content, the collection to which it belongs, and the group to which the collection belongs. All three of these values are populated by Windows Media Player when metadata for the content is retrieved. You can have your application record these values and use them to identify content, but you should not change them if they are present.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




