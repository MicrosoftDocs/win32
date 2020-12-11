---
title: SisFreeBackupStructure function (Sisbkup.h)
description: Frees the specified SIS backup structure.
ms.assetid: 34d5e919-e4bf-4105-ac15-a2ff5adfbdee
keywords:
- SisFreeBackupStructure function Backup
topic_type:
- apiref
api_name:
- SisFreeBackupStructure
api_location:
- Sisbkup.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# SisFreeBackupStructure function

The **SisFreeBackupStructure** function frees the specified SIS backup structure.

## Syntax


```C++
BOOL SisFreeBackupStructure(
  _In_ PVOID sisBackupStructure
);
```



## Parameters

<dl> <dt>

*sisBackupStructure* \[in\]
</dt> <dd>

Pointer to the SIS backup structure returned from [**SisCreateBackupStructure**](siscreatebackupstructure.md).

</dd> </dl>

## Return value

This function returns **TRUE** if it completes successfully and **FALSE** otherwise. Call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) to get more information about the reason the call failed.

## Remarks

This function should be called after the backup operation is completed for the volume identified by the value of the *sisBackupStructure* parameter.

Note that it is not safe to assume that this only deallocates memory. For example, this function may also perform additional administrative operations for the SIS architecture. Therefore, call this function even if your backup operation will exit immediately afterward.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Sisbkup.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Sisbkup.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sisbkup.dll</dt> </dl> |



## See also

<dl> <dt>

[**SisCreateBackupStructure**](siscreatebackupstructure.md)
</dt> </dl>

 

