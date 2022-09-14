---
description: Retrieves the type and data for the specified registry value in an offline registry hive.
ms.assetid: 83604743-cb59-42a1-9951-620ad5bd8de7
title: ORGetValue function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORGetValue
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORGetValue function

Retrieves the type and data for the specified registry value in an offline registry hive.

## Syntax


```C++
DWORD ORGetValue(
  _In_        ORHKEY Handle,
  _In_opt_    PCWSTR lpSubKey,
  _In_opt_    PCWSTR lpValue,
  _Out_opt_   PDWORD pdwType,
  _Out_opt_   PVOID  pvData,
  _Inout_opt_ PDWORD pcbData
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive.

</dd> <dt>

*lpSubKey* \[in, optional\]
</dt> <dd>

The name of the registry key. This key must be a subkey of the key specified by the *Handle* parameter. This parameter can be **NULL**.

Key names are not case sensitive.

</dd> <dt>

*lpValue* \[in, optional\]
</dt> <dd>

The name of the registry value. If this parameter is **NULL** or an empty string, "", the function retrieves the type and data for the key's unnamed or default value, if any. For more information, see [Registry Element Size Limits](../sysinfo/registry-element-size-limits.md).

Keys do not automatically have an unnamed or default value. Unnamed values can be of any type.

Value names are not case sensitive.

</dd> <dt>

*pdwType* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives a code indicating the type of data stored in the specified value. For a list of the possible type codes, see [Registry Value Types](../sysinfo/registry-value-types.md). This parameter can be **NULL** if the type is not required.

</dd> <dt>

*pvData* \[out, optional\]
</dt> <dd>

A pointer to a buffer that receives the value's data. This parameter can be **NULL** if the data is not required.

If the data is a string, the function checks for a terminating null character. If one is not found, the string is stored with a null terminator if the buffer is large enough to accommodate the extra character. Otherwise, the function fails and returns ERROR\_MORE\_DATA.

</dd> <dt>

*pcbData* \[in, out, optional\]
</dt> <dd>

A pointer to a variable that specifies the size of the buffer pointed to by the *pvData* parameter, in bytes. When the function returns, this variable contains the size of the data copied to *pvData*.

The *pcbData* parameter can be **NULL** only if *pvData* is **NULL**.

If the data has the REG\_SZ, REG\_MULTI\_SZ or REG\_EXPAND\_SZ type, this size includes any terminating null character or characters. For more information, see Remarks.

If the buffer specified by *pvData* parameter is not large enough to hold the data, the function returns ERROR\_MORE\_DATA and stores the required buffer size in the variable pointed to by *pcbData*. In this case, the contents of the *pvData* buffer are undefined.

If *pvData* is **NULL**, and *pcbData* is non-**NULL**, the function returns ERROR\_SUCCESS and stores the size of the data, in bytes, in the variable pointed to by *pcbData*. This enables an application to determine the best way to allocate a buffer for the value's data.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error.

## Remarks

An application typically calls the [**OREnumValue**](orenumvalue.md) function to determine the value names and then calls the **ORGetValue** function to retrieve the data for the names.

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

[**OREnumKey**](orenumkey.md)
</dt> <dt>

[**OREnumValue**](orenumvalue.md)
</dt> <dt>

[**OROpenKey**](oropenkey.md)
</dt> <dt>

[**ORQueryInfoKey**](orqueryinfokey.md)
</dt> </dl>

 

 
