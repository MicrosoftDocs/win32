---
description: Deletes a subkey and its values from an offline registry hive.
ms.assetid: 651795d3-4328-4281-9a7f-ba75b4ec4da1
title: ORDeleteKey function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORDeleteKey
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORDeleteKey function

Deletes a subkey and its values from an offline registry hive.

## Syntax


```C++
DWORD ORDeleteKey(
  _In_     ORHKEY Handle,
  _In_opt_ PCWSTR lpSubKey
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive. This handle is returned by the [**ORCreateKey**](orcreatekey.md) or [**OROpenKey**](oropenkey.md) function.

</dd> <dt>

*lpSubKey* \[in, optional\]
</dt> <dd>

The name of the key to be deleted. It must be a subkey of the key that *Handle* identifies, but it cannot have subkeys.

If the subkey does not exist, the function returns ERROR\_NOT\_FOUND.

If this parameter is **NULL**, the function deletes the key specified by the *Handle* parameter. If the key specified by the *Handle* parameter is the root key of the hive, the function returns ERROR\_INVALID\_PARAMETER.

Key names are not case sensitive.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error. Possible error codes include the following:

-   If the specified subkey does not exist, the function returns ERROR\_FILE\_NOT\_FOUND.
-   If the specified subkey is the root key of the registry hive, the function returns ERROR\_INVALID\_PARAMETER.
-   If the specified subkey has subkeys, the function returns ERROR\_KEY\_HAS\_CHILDREN.

## Remarks

If the specified registry key exists, it is marked as deleted. A deleted key is not removed until the last handle to it is closed.

The key to be deleted must not have subkeys. To delete a key and all its subkeys, use the [**OREnumKey**](orenumkey.md) function to enumerate the subkeys and delete them individually.

Only the [**ORCloseKey**](orclosekey.md) function may be called on a deleted key; all other offline registry operations fail. If the deleted key was explicitly created by calling [**ORCreateKey**](orcreatekey.md), resources associated with the key are released when the last handle to the deleted key is closed.

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

[**OREnumKey**](orenumkey.md)
</dt> <dt>

[**OROpenKey**](oropenkey.md)
</dt> </dl>

 

 
