---
Description: Specifies whether a non-color style has the italic style.
ms.assetid: 4295c0b1-6e37-4fa9-9015-68bcc4784cda
title: FItalicIMEStyle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FItalicIMEStyle function

Specifies whether a non-color style has the italic style.

## Syntax


```C++
BOOL __cdecl FItalicIMEStyle(
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

**TRUE** if the style has the italic style.

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

 

 




