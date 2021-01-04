---
title: IResultType DisplayName property (WdsSharedIDL.h)
description: Localized display name of the type
ms.assetid: 21695ba3-aa6d-419b-961a-0643caa5ea1f
keywords:
- DisplayName property Legacy Windows Environment Features
- DisplayName property Legacy Windows Environment Features , IResultType interface
- IResultType interface Legacy Windows Environment Features , DisplayName property
topic_type:
- apiref
api_name:
- IResultType.DisplayName
- IResultType.get_DisplayName
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultType::DisplayName property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Localized display name of the type:

This property is read-only.

## Syntax


```C++
HRESULT get_DisplayName(
  [out, retval] BSTR *name
);
```



## Property value

returns the address of the localized display name for the type.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





