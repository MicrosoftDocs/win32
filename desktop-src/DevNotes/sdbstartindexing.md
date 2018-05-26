---
Description: Enables index creation and modification for the specified database.
ms.assetid: f780034e-6963-423c-8ffa-9fbe98dca7e1
title: SdbStartIndexing function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SdbStartIndexing function

Enables index creation and modification for the specified database.

## Syntax


```C++
BOOL WINAPI SdbStartIndexing(
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



|                                     |                                                                                        |
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

[**SdbStopIndexing**](sdbstopindexing.md)
</dt> </dl>

 

 




