---
description: Closes the shim database initialized using the SdbInitDatabase function.
ms.assetid: 8452ab14-a1e9-41b3-a1ac-7ff3a7d3a7ed
title: SdbReleaseDatabase function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbReleaseDatabase
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbReleaseDatabase function

Closes the shim database initialized using the [**SdbInitDatabase**](sdbinitdatabase.md) function.

## Syntax


```C++
void WINAPI SdbReleaseDatabase(
  _In_ HSDB hSDB
);
```



## Parameters

<dl> <dt>

*hSDB* \[in\]
</dt> <dd>

A handle to the shim database returned by the [**SdbInitDatabase**](sdbinitdatabase.md) function.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbInitDatabase**](sdbinitdatabase.md)
</dt> </dl>

 

 




