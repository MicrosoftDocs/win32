---
title: IPropertyFilterCollection AddItem property
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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPropertyFilterCollection::AddItem property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

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



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





