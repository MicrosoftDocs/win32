---
title: IResultProperty UID property (WdsSharedIDL.h)
description: Unique identifier for the property.
ms.assetid: b5cee5b3-78b4-4d2a-b442-f6624497ef71
keywords:
- UID property Legacy Windows Environment Features
- UID property Legacy Windows Environment Features , IResultProperty interface
- IResultProperty interface Legacy Windows Environment Features , UID property
topic_type:
- apiref
api_name:
- IResultProperty.UID
- IResultProperty.get_UID
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultProperty::UID property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Unique identifier for the property.

This property is read-only.

## Syntax


```C++
HRESULT get_UID(
  [out, retval] long *uid
);
```



## Property value

returns a pointer to the unique property identifier.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





