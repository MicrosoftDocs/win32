---
description: Enumerates the subkeys of the specified open registry key in an offline registry hive. The function retrieves information about one subkey each time it is called.
ms.assetid: 46d13c37-473a-4772-992c-a565ad702fb9
title: OREnumKey function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OREnumKey
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# OREnumKey function

Enumerates the subkeys of the specified open registry key in an offline registry hive. The function retrieves information about one subkey each time it is called.

## Syntax


```C++
DWORD OREnumKey(
  _In_        ORHKEY    Handle,
  _In_        DWORD     dwIndex,
  _Out_       PWSTR     lpName,
  _Inout_     PDWORD    lpcName,
  _Out_opt_   PWSTR     lpClass,
  _Inout_opt_ PDWORD    lpcClass,
  _Out_opt_   PFILETIME lpftLastWriteTime
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive.

</dd> <dt>

*dwIndex* \[in\]
</dt> <dd>

The index of the subkey to retrieve. This parameter should be zero for the first call to the function and then incremented for subsequent calls.

Because subkeys are not ordered, any new subkey will have an arbitrary index. This means that the function may return subkeys in any order.

</dd> <dt>

*lpName* \[out\]
</dt> <dd>

A pointer to a buffer that receives the name of the subkey, including the terminating null character. The function copies only the name of the subkey, not the full key hierarchy, to the buffer. If the function fails, no information is copied to this buffer.

For more information, see [Registry Element Size Limits](../sysinfo/registry-element-size-limits.md).

</dd> <dt>

*lpcName* \[in, out\]
</dt> <dd>

A pointer to a variable that specifies the size of the buffer specified by the *lpName* parameter, in **WCHARs**. This size should include the terminating null character. If the function succeeds, the variable pointed to by *lpcName* contains the number of characters stored in the buffer, not including the terminating null character.

</dd> <dt>

*lpClass* \[out, optional\]
</dt> <dd>

A pointer to a buffer that receives the null-terminated class string of the enumerated subkey. This parameter can be **NULL**.

</dd> <dt>

*lpcClass* \[in, out, optional\]
</dt> <dd>

A pointer to a variable that specifies the size of the buffer specified by the *lpClass* parameter, in **WCHARs**. The size should include the terminating null character. If the function succeeds, *lpcClass* contains the number of characters stored in the buffer, not including the terminating null character. This parameter can be **NULL** only if *lpClass* is **NULL**.

</dd> <dt>

*lpftLastWriteTime* \[out, optional\]
</dt> <dd>

A pointer to [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure that receives the time at which the enumerated subkey was last written. This parameter can be **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error. Possible error codes include the following:

-   If the *lpName* buffer is too small to receive the name of the key, the function returns ERROR\_MORE\_DATA.
-   If there are no more subkeys available, the function returns ERROR\_NO\_MORE\_ITEMS.

## Remarks

To enumerate subkeys, an application should initially call the **OREnumKey** function with the *dwIndex* parameter set to zero. The application should then increment the *dwIndex* parameter and call **OREnumKey** until there are no more subkeys (meaning the function returns ERROR\_NO\_MORE\_ITEMS).

The application can also set *dwIndex* to the index of the last subkey on the first call to the function and decrement the index until the subkey with the index 0 is enumerated. To retrieve the index of the last subkey, use the [**ORQueryInfoKey**](/windows/win32/api/winreg/nf-winreg-regqueryinfokeya) function.

While an application is using the **OREnumKey** function, it should not make calls to any offline registry functions that might change the key being enumerated.

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

[**ORDeleteKey**](ordeletekey.md)
</dt> <dt>

[**OROpenKey**](oropenkey.md)
</dt> <dt>

[**ORQueryInfoKey**](orqueryinfokey.md)
</dt> </dl>

 

 
