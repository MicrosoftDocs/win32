---
description: Creates an offline registry hive that contains a single empty root key.
ms.assetid: 985cfea4-6f15-4d63-8e41-df2a490296a3
title: ORCreateHive function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORCreateHive
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORCreateHive function

Creates an offline registry hive that contains a single empty root key.

## Syntax


```C++
DWORD ORCreateHive(
  _Out_ PORHKEY phkResult
);
```



## Parameters

<dl> <dt>

*phkResult* \[out\]
</dt> <dd>

Points to a variable to receive a handle to the root key of the newly created offline registry hive. If the hive cannot be created, the function sets this parameter to **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error.

If there is insufficient memory to create the registry hive, the function returns ERROR\_NOT\_ENOUGH\_MEMORY.

## Remarks

The **ORCreateHive** function creates an empty offline registry hive in memory. Use the [**ORCreateKey**](orcreatekey.md) and [**ORSetValue**](orsetvalue.md) functions to add keys and set their values.

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

[**OROpenHive**](oropenhive.md)
</dt> <dt>

[**ORSaveHive**](orsavehive.md)
</dt> <dt>

[**ORSetValue**](orsetvalue.md)
</dt> </dl>

 

 
