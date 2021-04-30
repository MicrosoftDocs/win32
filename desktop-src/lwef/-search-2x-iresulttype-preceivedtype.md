---
title: IResultType PreceivedType property (WdsSharedIDL.h)
description: This property contains the string used to identify the type in the index.
ms.assetid: 26d5f14c-162a-4ded-ac72-875561b8c977
keywords:
- PreceivedType property Legacy Windows Environment Features
- PreceivedType property Legacy Windows Environment Features , IResultType interface
- IResultType interface Legacy Windows Environment Features , PreceivedType property
topic_type:
- apiref
api_name:
- IResultType.PreceivedType
- IResultType.get_PreceivedType
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultType::PreceivedType property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

This property contains the string used to identify the type in the index.

This property is read-only.

## Syntax


```C++
HRESULT get_PreceivedType(
  [out, retval] BSTR *name
);
```



## Property value

returns the address of the string identifyint the type in the index.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





