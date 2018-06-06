---
Description: Multiplies extended integers.
ms.assetid: 6a59d211-4baf-4c7c-af2a-ffb0c5773445
title: RtlExtendedIntegerMultiply function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 




