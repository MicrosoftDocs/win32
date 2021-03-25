---
description: Loads the specified registry hive file into memory and validates the hive.
ms.assetid: 5d8498b0-e1bb-4c3d-bf3d-7bfc3002eb1a
title: OROpenHive function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OROpenHive
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# OROpenHive function

Loads the specified registry hive file into memory and validates the hive.

## Syntax


```C++
DWORD OROpenHive(
  _In_  PCWSTR  lpHivePath,
  _Out_ PORHKEY phkResult
);
```



## Parameters

<dl> <dt>

*lpHivePath* \[in\]
</dt> <dd>

A pointer to a Unicode string that specifies the name of the registry hive file to be loaded into memory. This can be a hive file that was saved with the [**ORSaveHive**](orsavehive.md) function or created with the [RegSaveKey](/windows/win32/api/winreg/nf-winreg-regsavekeya) or [RegSaveKeyEx](/windows/win32/api/winreg/nf-winreg-regsavekeyexa) function. The file must be less than 4 GB in size, and the caller must have FILE\_READ\_DATA access to the file. For more information, see [File Security and Access Rights](../fileio/file-security-and-access-rights.md).

</dd> <dt>

*phkResult* \[out\]
</dt> <dd>

A pointer to a variable that receives a handle to the root key of the loaded offline registry hive. If the registry hive file cannot be opened or validation fails, the function sets this parameter to **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error. Possible error codes include the following:

-   If the file is empty or larger than 4 GB in size, the function returns ERROR\_BADDB.
-   If the caller does not have the necessary access rights to open the file, the function returns ERROR\_ACCESS\_DENIED.
-   If the registry hive fails validation, the function returns ERROR\_NOT\_REGISTRY\_FILE.

## Remarks

The **OROpenHive** function is the only offline registry function that validates a registry hive. If the validation fails, no attempt is made to repair the hive.

## Requirements



| Requirement | Value |
|----------------------------|---------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Offline Registry library version 1.0 or later<br/>                      |
| Header<br/>          | <dl> <dt>Offreg.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Offreg.dll</dt> </dl> |



## See also

<dl> <dt>

[**ORCloseHive**](orclosehive.md)
</dt> <dt>

[**ORCreateHive**](orcreatehive.md)
</dt> <dt>

[**ORSaveHive**](orsavehive.md)
</dt> <dt>

[RegSaveKey](/windows/win32/api/winreg/nf-winreg-regsavekeya)
</dt> <dt>

[RegSaveKeyEx](/windows/win32/api/winreg/nf-winreg-regsavekeyexa)
</dt> </dl>

 

 
