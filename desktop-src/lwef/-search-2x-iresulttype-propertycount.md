---
title: IResultType PropertyCount property (WdsSharedIDL.h)
description: This property contains the number of properties exposed by the type.
ms.assetid: 4ca4b18c-d228-4275-b00d-06c6f227e0ae
keywords:
- PropertyCount property Legacy Windows Environment Features
- PropertyCount property Legacy Windows Environment Features , IResultType interface
- IResultType interface Legacy Windows Environment Features , PropertyCount property
topic_type:
- apiref
api_name:
- IResultType.PropertyCount
- IResultType.get_PropertyCount
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultType::PropertyCount property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

This property contains the number of properties exposed by the type.

This property is read-only.

## Syntax


```C++
HRESULT get_PropertyCount(
  [out, retval] long *count
);
```



## Property value

returns the address of the number of properties exposed.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





