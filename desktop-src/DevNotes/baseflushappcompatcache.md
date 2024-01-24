---
description: Flushes the application compatibility cache.
ms.assetid: 03f47813-87f6-4b71-b453-77a2facab019
title: BaseFlushAppcompatCache function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BaseFlushAppcompatCache
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-appcompat-l1-1-0.dll
- KernelBase.dll
- API-MS-Win-Core-appcompat-l1-1-1.dll
---

# BaseFlushAppcompatCache function

Flushes the application compatibility cache.

## Syntax


```C++
BOOL WINAPI BaseFlushAppcompatCache(void);
```



## Parameters

This function has no parameters.

## Return value

The function returns **TRUE** if it succeeds and **FALSE** otherwise.

## Remarks

The caller must be an administrator.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl> |



## See also

<dl> <dt>

[**ShimFlushCache**](shimflushcache.md)
</dt> </dl>

 

 




