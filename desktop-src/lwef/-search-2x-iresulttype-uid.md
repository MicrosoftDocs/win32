---
title: IResultType UID property (WdsSharedIDL.h)
description: This property contains the unique identifier for the type.
ms.assetid: 31c2ef7d-f5a7-441e-80ea-fd7e46fded07
keywords:
- UID property Legacy Windows Environment Features
- UID property Legacy Windows Environment Features , IResultType interface
- IResultType interface Legacy Windows Environment Features , UID property
topic_type:
- apiref
api_name:
- IResultType.UID
- IResultType.get_UID
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultType::UID property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

This property contains the unique identifier for the type.

This property is read-only.

## Syntax


```C++
HRESULT get_UID(
  [out, retval] long *uid
);
```



## Property value

the address of the location containing the uid.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





