---
description: Multiplies extended integers.
ms.assetid: 6a59d211-4baf-4c7c-af2a-ffb0c5773445
title: RtlExtendedIntegerMultiply function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlExtendedIntegerMultiply
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlExtendedIntegerMultiply function

\[The **RtlExtendedIntegerMultiply** function is exported to support existing driver binaries and is obsolete. For better performance, use the compiler support for 64-bit integer operations.\]

Multiplies extended integers.

## Syntax


```C++
LARGE_INTEGER RtlExtendedIntegerMultiply(
  _In_ LARGE_INTEGER Multiplicand,
  _In_ LONG          Multiplier
);
```



## Parameters

<dl> <dt>

*Multiplicand* \[in\]
</dt> <dd>

Multiplicand.

</dd> <dt>

*Multiplier* \[in\]
</dt> <dd>

Multiplier.

</dd> </dl>

## Return value

Returns multiplication result.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 
