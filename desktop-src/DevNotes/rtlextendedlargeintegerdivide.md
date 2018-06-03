---
Description: Divides extended integers.
ms.assetid: d46f65f0-6c41-4cb2-9882-5b11f7aae3ca
title: RtlExtendedLargeIntegerDivide function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 




