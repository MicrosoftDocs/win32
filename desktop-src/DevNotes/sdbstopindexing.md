---
description: Disables index creation and modification for the specified database.
ms.assetid: d079eae2-574e-4ac1-a0f9-11796e56a790
title: SdbStopIndexing function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbStopIndexing
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbStopIndexing function

Disables index creation and modification for the specified database.

## Syntax


```C++
BOOL WINAPI SdbStopIndexing(
  _In_ PDB     pdb,
  _In_ INDEXID iiWhich
);
```



## Parameters

<dl> <dt>

*pdb* \[in\]
</dt> <dd>

A handle to the shim database.

</dd> <dt>

*iiWhich* \[in\]
</dt> <dd>

The index identifier.

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

[**SdbCommitIndexes**](sdbcommitindexes.md)
</dt> <dt>

[**SdbDeclareIndex**](sdbdeclareindex.md)
</dt> <dt>

[**SdbStartIndexing**](sdbstartindexing.md)
</dt> </dl>

 

 




