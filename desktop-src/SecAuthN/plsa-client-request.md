---
description: An opaque data type.
ms.assetid: 384dd6e0-726f-4100-a036-1cca6a332a64
title: PLSA_CLIENT_REQUEST (Ntsecpkg.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PLSA\_CLIENT\_REQUEST

The **PLSA\_CLIENT\_REQUEST** data type is an opaque data type.

The [*Local Security Authority*](../secgloss/l-gly.md) (LSA) uses it internally to maintain client information related to individual requests.


```C++
#include <windows.h>

typedef PVOID *PLSA_CLIENT_REQUEST;
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Ntsecpkg.h</dt> </dl> |



 

 
