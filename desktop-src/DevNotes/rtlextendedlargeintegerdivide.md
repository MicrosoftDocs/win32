---
description: Divides extended integers.
ms.assetid: d46f65f0-6c41-4cb2-9882-5b11f7aae3ca
title: RtlExtendedLargeIntegerDivide function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlExtendedLargeIntegerDivide
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlExtendedLargeIntegerDivide function

\[The **RtlExtendedLargeIntegerDivide** function is exported to support existing driver binaries and is obsolete. For better performance, use the compiler support for 64-bit integer operations.\]

Divides extended integers.

## Syntax


```C++
LARGE_INTEGER RtlExtendedLargeIntegerDivide(
  _In_    LARGE_INTEGER Dividend,
  _In_    ULONG         Divisor,
  _Inout_ PULONG        Remainder
);
```



## Parameters

<dl> <dt>

*Dividend* \[in\]
</dt> <dd>

Dividend.

</dd> <dt>

*Divisor* \[in\]
</dt> <dd>

Divisor.

</dd> <dt>

*Remainder* \[in, out\]
</dt> <dd>

Pointer to division remainder.

</dd> </dl>

## Return value

Returns the result of the division operation.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 
