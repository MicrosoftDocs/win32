---
description: Sets the data for the value of a specified registry key in an offline registry hive.
ms.assetid: 62fd3a3a-6ce3-4313-b0e7-37ceea0ce302
title: ORSetValue function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORSetValue
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORSetValue function

Sets the data for the value of a specified registry key in an offline registry hive.

## Syntax


```C++
DWORD ORSetValue(
  _In_     ORHKEY Handle,
  _In_opt_ PCWSTR lpValueName,
  _In_     DWORD  dwType,
  _In_opt_ const BYTE *lpData,
  _In_     DWORD  cbData
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive.

</dd> <dt>

*lpValueName* \[in, optional\]
</dt> <dd>

The name of the value to be set. If a value with this name is not already present in the key, the function adds it to the key.

If *lpValueName* is **NULL** or an empty string, "", the function sets the type and data for the key's unnamed or default value.

For more information, see [Registry Element Size Limits](../sysinfo/registry-element-size-limits.md).

Registry keys do not have default values, but they can have one unnamed value, which can be of any type.

</dd> <dt>

*dwType* \[in\]
</dt> <dd>

The type of data pointed to by the *lpData* parameter. For a list of the possible types, see [Registry Value Types](../sysinfo/registry-value-types.md).

</dd> <dt>

*lpData* \[in, optional\]
</dt> <dd>

The data to be stored.

For string-based types, such as REG\_SZ, the string must be null-terminated. For the REG\_MULTI\_SZ data type, the string must be terminated with two null characters.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

The size of the information pointed to by the *lpData* parameter, in bytes. If the data is of type REG\_SZ, REG\_EXPAND\_SZ, or REG\_MULTI\_SZ, *cbData* must include the size of the terminating null character or characters.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error.

## Remarks

Value sizes are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the file names stored in the registry. This helps the registry perform efficiently. Application elements such as icons, bitmaps, and executable files should be stored as files and not be placed in the registry.

## Requirements



| Requirement | Value |
|----------------------------|---------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Offline Registry library version 1.0 or later<br/>                      |
| Header<br/>          | <dl> <dt>Offreg.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Offreg.dll</dt> </dl> |



## See also

<dl> <dt>

[**ORCreateKey**](orcreatekey.md)
</dt> <dt>

[**OROpenKey**](oropenkey.md)
</dt> </dl>

 

 
