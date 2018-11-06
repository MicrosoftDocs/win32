---
Description: Divides extended integers.
ms.assetid: d46f65f0-6c41-4cb2-9882-5b11f7aae3ca
title: RtlExtendedLargeIntegerDivide function
ms.topic: article
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 




