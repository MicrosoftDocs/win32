---
Description: Specifies whether a non-color style has the bold style.
ms.assetid: fd34af7f-8847-43aa-9e69-264a08eba98b
title: FBoldIMEStyle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FBoldIMEStyle function

Specifies whether a non-color style has the bold style.

## Syntax


```C++
BOOL FBoldIMEStyle(
  _In_ const IMESTYLE *pimestyle
);
```



## Parameters

<dl> <dt>

*pimestyle* \[in\]
</dt> <dd>

An **IMESTYLE** structure returned from the [**PIMEStyleFromAttr**](pimestylefromattr.md) function.

</dd> </dl>

## Return value

**TRUE** if the style has the bold style.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**PIMEStyleFromAttr**](pimestylefromattr.md)
</dt> </dl>

 

 




