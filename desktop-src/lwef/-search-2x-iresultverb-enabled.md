---
title: IResultVerb Enabled property
description: This property returns TRUE if the verb is enabled.
ms.assetid: 27e3dbb8-678e-46c7-82e5-40b86cb157a7
keywords:
- Enabled property Legacy Windows Environment Features
- Enabled property Legacy Windows Environment Features , IResultVerb interface
- IResultVerb interface Legacy Windows Environment Features , Enabled property
topic_type:
- apiref
api_name:
- IResultVerb.Enabled
- IResultVerb.get_Enabled
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# IResultVerb::Enabled property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

This property returns TRUE if the verb is enabled.

This property is read-only.

## Syntax


```C++
HRESULT get_Enabled(
  [out, retval] VARIANT_BOOL *flag
);
```



## Property value

This property returns True if the verb is enabled or False if not.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





