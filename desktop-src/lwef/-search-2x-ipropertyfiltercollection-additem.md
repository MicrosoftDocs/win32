---
title: IPropertyFilterCollection AddItem property (WdsSharedIDL.h)
description: Adds a new filter to the collection.
ms.assetid: 01078e7a-811a-4dfb-b122-4801f39413d8
keywords:
- AddItem property Legacy Windows Environment Features
- AddItem property Legacy Windows Environment Features , IPropertyFilterCollection interface
- IPropertyFilterCollection interface Legacy Windows Environment Features , AddItem property
topic_type:
- apiref
api_name:
- IPropertyFilterCollection.AddItem
- IPropertyFilterCollection.get_AddItem
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IPropertyFilterCollection::AddItem property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Adds a new filter to the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_AddItem(
  [out, retval] IPropertyFilter **filter
);
```



## Property value

returns a pointer to the address for the new filter.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





