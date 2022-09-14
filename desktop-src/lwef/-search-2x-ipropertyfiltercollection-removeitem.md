---
title: IPropertyFilterCollection RemoveItem property (WdsSharedIDL.h)
description: Removes a specific filter to the collection.
ms.assetid: a8b8a1f7-d47a-45dc-81c9-f01ecf6c1560
keywords:
- RemoveItem property Legacy Windows Environment Features
- RemoveItem property Legacy Windows Environment Features , IPropertyFilterCollection interface
- IPropertyFilterCollection interface Legacy Windows Environment Features , RemoveItem property
topic_type:
- apiref
api_name:
- IPropertyFilterCollection.RemoveItem
- IPropertyFilterCollection.put_RemoveItem
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IPropertyFilterCollection::RemoveItem property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Removes a specific filter to the collection.

This property is write-only.

## Syntax


```C++
HRESULT put_RemoveItem(
  [in] long index
);
```



## Property value

Accepts a pointer to the index for the filter to be removed.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





