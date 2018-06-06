---
Description: Specifies whether a non-color style has an underline style.
ms.assetid: 452dda6e-b12b-457c-9a01-c5363359c9f5
title: FUlIMEStyle function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FUlIMEStyle function

Specifies whether a non-color style has an underline style.

## Syntax


```C++
BOOL __cdecl FUlIMEStyle(
  _In_ const IMESTYLE *pimestyle
);
```



## Parameters

<dl> <dt>

*pimestyle* \[in\]
</dt> <dd>

An **IMESTYLE** structure returned from [**PIMEStyleFromAttr**](pimestylefromattr.md) function.

</dd> </dl>

## Return value

TRUE if the style has an underline style.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**PIMEStyleFromAttr**](pimestylefromattr.md)
</dt> </dl>

 

 




