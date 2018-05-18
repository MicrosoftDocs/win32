---
title: IResultType PreceivedType property
description: This property contains the string used to identify the type in the index.
ms.assetid: '26d5f14c-162a-4ded-ac72-875561b8c977'
keywords: ["PreceivedType property Legacy Windows Environment Features", "PreceivedType property Legacy Windows Environment Features , IResultType interface", "IResultType interface Legacy Windows Environment Features , PreceivedType property"]
topic_type:
- apiref
api_name:
- IResultType.PreceivedType
- IResultType.get_PreceivedType
api_location:
- WdsSharedIDL.h
api_type:
- COM
---

# IResultType::PreceivedType property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

This property contains the string used to identify the type in the index.

This property is read-only.

## Syntax


```C++
HRESULT get_PreceivedType(
  [out, retval] BSTR *name
);
```



## Property value

returns the address of the string identifyint the type in the index.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





