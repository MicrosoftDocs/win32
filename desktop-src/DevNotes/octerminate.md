---
Description: Closes the OC manager.
ms.assetid: feba9954-03b2-4b57-b7ba-933e171751ff
title: OcTerminate function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OcTerminate function

Closes the OC manager.

## Syntax


```C++
VOID OcTerminate(
  _Inout_ PVOID *OcManagerContext
);
```



## Parameters

<dl> <dt>

*OcManagerContext* \[in, out\]
</dt> <dd>

On input, contains the OC manager context pointer returned by [**OcInitialize**](ocinitialize.md). On output, receives **NULL**.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>OcManage.dll</dt> </dl> |



## See also

<dl> <dt>

[**OcInitialize**](ocinitialize.md)
</dt> </dl>

 

 




