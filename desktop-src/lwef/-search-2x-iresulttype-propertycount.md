---
title: IResultType PropertyCount property
description: This property contains the number of properties exposed by the type.
ms.assetid: '4ca4b18c-d228-4275-b00d-06c6f227e0ae'
keywords: ["PropertyCount property Legacy Windows Environment Features", "PropertyCount property Legacy Windows Environment Features , IResultType interface", "IResultType interface Legacy Windows Environment Features , PropertyCount property"]
topic_type:
- apiref
api_name:
- IResultType.PropertyCount
- IResultType.get_PropertyCount
api_location:
- WdsSharedIDL.h
api_type:
- COM
---

# IResultType::PropertyCount property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

This property contains the number of properties exposed by the type.

This property is read-only.

## Syntax


```C++
HRESULT get_PropertyCount(
  [out, retval] long *count
);
```



## Property value

returns the address of the number of properties exposed.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





