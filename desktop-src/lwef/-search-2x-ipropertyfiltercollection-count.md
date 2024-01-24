---
title: IPropertyFilterCollection Count property (WdsSharedIDL.h)
description: Number of filters in the collection.
ms.assetid: 9d656f06-eb1d-4cc6-9096-252f0fc65ae2
keywords:
- Count property Legacy Windows Environment Features
- Count property Legacy Windows Environment Features , IPropertyFilterCollection interface
- IPropertyFilterCollection interface Legacy Windows Environment Features , Count property
topic_type:
- apiref
api_name:
- IPropertyFilterCollection.Count
- IPropertyFilterCollection.get_Count
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IPropertyFilterCollection::Count property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Number of filters in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] long *count
);
```



## Property value

returns a pointer to the number of filters in the collection.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





