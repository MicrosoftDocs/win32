---
description: Frees the specified file attribute data.
ms.assetid: c1a4dcf8-614f-49a5-a923-8d7d610e6406
title: SdbFreeFileAttributes function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbFreeFileAttributes
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbFreeFileAttributes function

Frees the specified file attribute data.

## Syntax


```C++
BOOL WINAPI SdbFreeFileAttributes(
  _In_ PATTRINFO pFileAttributes
);
```



## Parameters

<dl> <dt>

*pFileAttributes* \[in\]
</dt> <dd>

An [**ATTRINFO**](attrinfo.md) structure returned by the [**SdbGetFileAttributes**](sdbgetfileattributes.md) function.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbGetFileAttributes**](sdbgetfileattributes.md)
</dt> </dl>

 

 




