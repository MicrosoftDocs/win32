---
Description: Specifies whether the specified color is an RGB color.
ms.assetid: 16b48644-c2d5-4383-836a-122f44504638
title: FRGBIMEColorStyle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FRGBIMEColorStyle function

Specifies whether the specified color is an RGB color.

## Syntax


```C++
BOOL __cdecl FRGBIMEColorStyle(
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

Returns **TRUE** when the color is an RGB color.

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

 

 




