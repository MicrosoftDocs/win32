---
Description: Closes the OC manager.
ms.assetid: feba9954-03b2-4b57-b7ba-933e171751ff
title: OcTerminate function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OcTerminate
api_type: 
- DllExport
api_location: 
- OcManage.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>OcManage.dll</dt> </dl> |



## See also

<dl> <dt>

[**OcInitialize**](ocinitialize.md)
</dt> </dl>

 

 




