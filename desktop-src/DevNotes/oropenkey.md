---
description: Opens the specified registry key in an offline registry hive.
ms.assetid: 4a4afbef-5107-4006-bd67-aecb5d3b5112
title: OROpenKey function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OROpenKey
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# OROpenKey function

Opens the specified registry key in an offline registry hive.

## Syntax


```C++
DWORD OROpenKey(
  _In_     ORHKEY  Handle,
  _In_opt_ PCWSTR  lpSubKeyName,
  _Out_    PORHKEY phkResult
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive.

</dd> <dt>

*lpSubKeyName* \[in, optional\]
</dt> <dd>

A pointer to a UNICODE string that contains the name of the registry key to be opened. This key must be a subkey of the key identified by the *Handle* parameter.

Key names are not case sensitive.

If this parameter is **NULL** or a pointer to an empty string, the function returns the same handle that was passed in. If the key specified by the *Handle* parameter is the root key of the hive, the function returns ERROR\_INVALID\_PARAMETER.

For more information, see [Registry Element Size Limits](../sysinfo/registry-element-size-limits.md).

</dd> <dt>

*phkResult* \[out\]
</dt> <dd>

A pointer to a variable that receives a handle to the opened key. Use the [**ORCloseKey**](orclosekey.md) function to close the key after you have finished using the handle.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error.

If the handle to be returned would be a handle to the root key of the hive, the function returns ERROR\_INVALID\_PARAMETER.

If the specified key has been marked as deleted, this function returns ERROR\_KEY\_DELETED.

## Remarks

The **OROpenKey** function cannot be used to open the root key in an offline registry hive. To obtain a handle to the root key of a hive, use the [**OROpenHive**](oropenhive.md) function to load the hive into memory.

## Requirements



| Requirement | Value |
|----------------------------|---------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Offline Registry library version 1.0 or later<br/>                      |
| Header<br/>          | <dl> <dt>Offreg.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Offreg.dll</dt> </dl> |



## See also

<dl> <dt>

[**ORCloseKey**](orclosekey.md)
</dt> <dt>

[**ORCreateKey**](orcreatekey.md)
</dt> <dt>

[**ORDeleteKey**](ordeletekey.md)
</dt> <dt>

[**OROpenHive**](oropenhive.md)
</dt> </dl>

 

 
