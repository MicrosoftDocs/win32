---
Description: Specifies whether the specified color is a special window color.
ms.assetid: 41f7d4fb-9718-42a8-89df-c29bd8c0665b
title: FSpecialWindowIMEColorStyle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FSpecialWindowIMEColorStyle function

Specifies whether the specified color is a special window color.

## Syntax


```C++
BOOL __cdecl FSpecialWindowIMEColorStyle(
  _In_ const IMECOLORSTY *pcolorstyle
);
```



## Parameters

<dl> <dt>

*pcolorstyle* \[in\]
</dt> <dd>

An **IMECOLORSTY** structure returned from a [**PColorStyleBackFromIMEStyle**](pcolorstylebackfromimestyle.md) or [**PColorStyleTextFromIMEStyle**](pcolorstyletextfromimestyle.md) function.

</dd> </dl>

## Return value

Returns **TRUE** when the color is a special window color (one of special color).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**PColorStyleBackFromIMEStyle**](pcolorstylebackfromimestyle.md)
</dt> <dt>

[**PColorStyleTextFromIMEStyle**](pcolorstyletextfromimestyle.md)
</dt> </dl>

 

 




