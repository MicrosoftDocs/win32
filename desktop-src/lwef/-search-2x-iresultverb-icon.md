---
title: IResultVerb Icon property
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
ms.topic: article
ms.date: 05/31/2018
---

# IResultVerb::Icon property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

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



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





