---
description: Releases resources used by the SdbGetMatchingExe function.
ms.assetid: 4a784f72-2108-4d5e-86e1-1960ac921c8f
title: SdbReleaseMatchingExe function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbReleaseMatchingExe
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbReleaseMatchingExe function

Releases resources used by the [**SdbGetMatchingExe**](sdbgetmatchingexe.md) function.

## Syntax


```C++
void WINAPI SdbReleaseMatchingExe(
  _In_ HSDB   hSDB,
  _In_ TAGREF trExe
);
```



## Parameters

<dl> <dt>

*hSDB* \[in\]
</dt> <dd>

A handle to the shim database returned by the [**SdbInitDatabase**](sdbinitdatabase.md) function.

</dd> <dt>

*trExe* \[in\]
</dt> <dd>

The [**TAGREF**](tagref.md) returned by [**SdbGetMatchingExe**](sdbgetmatchingexe.md).

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

[**SdbGetMatchingExe**](sdbgetmatchingexe.md)
</dt> <dt>

[**SdbInitDatabase**](sdbinitdatabase.md)
</dt> </dl>

 

 




