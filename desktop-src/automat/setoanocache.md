---
title: SetOaNoCache function
description: Disables the BSTR caching in OleAut32.dll.
ms.assetid: '07bca76a-84af-4857-9739-f032a4790388'
keywords: ["SetOaNoCache function Automation"]
topic_type:
- apiref
api_name:
- SetOaNoCache
api_location:
- OleAut32.dll
api_type:
- DllExport
---

# SetOaNoCache function

Disables the **BSTR** caching in OleAut32.dll.

## Syntax


```C++
void __cdecl SetOaNoCache(void);
```



## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

OLE Automation caches the space allocated for **BSTR** strings. The **SetOaNoCache** function immediately disables the oleaut32.dll **BSTR** caching mechanism. All further allocations and deallocations are passed directly to the process allocator. Cached **BSTR** values are not released. This function should be called before any **BSTR** operations take place in the process. **BSTR** caching can also be disabled at the machine level by setting the environment variable OANOCACHE to 1.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>OleAut32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>OleAut32.dll</dt> </dl> |



 

 





