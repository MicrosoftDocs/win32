---
title: IResultVerb Icon property (WdsSharedIDL.h)
description: This property returns a pointer to handle of the optional icon associated with the verb.
ms.assetid: 19de0e36-b453-48a4-8ac0-f26432e088ae
keywords:
- Icon property Legacy Windows Environment Features
- Icon property Legacy Windows Environment Features , IResultVerb interface
- IResultVerb interface Legacy Windows Environment Features , Icon property
topic_type:
- apiref
api_name:
- IResultVerb.Icon
- IResultVerb.get_Icon
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultVerb::Icon property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

This property returns a pointer to handle of the optional icon associated with the verb.

This property is read-only.

## Syntax


```C++
HRESULT get_Icon(
  [out, retval] SHANDLE_PTR *hicon
);
```



## Property value

hicon is a pointer to the handle of the optional icon assocuated with the verb.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





