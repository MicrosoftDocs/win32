---
description: Closes a handle to the specified registry key in an offline registry hive.
ms.assetid: 01bb21b1-217b-4716-ae1e-466cf8383155
title: ORCloseKey function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORCloseKey
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORCloseKey function

Closes a handle to the specified registry key in an offline registry hive.

## Syntax


```C++
DWORD ORCloseKey(
  _In_ ORHKEY Handle
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error.

If the specified key is the root key of the registry hive, the function fails with ERROR\_INVALID\_PARAMETER.

## Remarks

The handle for a specified key should not be used after it has been closed, because it will no longer be valid. Key handles should not be left open any longer than necessary.

Use the [**ORCloseHive**](orclosehive.md) function to close an offline registry hive.

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

[**ORCreateKey**](orcreatekey.md)
</dt> <dt>

[**ORDeleteKey**](ordeletekey.md)
</dt> <dt>

[**OROpenKey**](oropenkey.md)
</dt> </dl>

 

 
