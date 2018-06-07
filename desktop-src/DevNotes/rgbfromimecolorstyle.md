---
Description: Converts an IMECOLORSTY structure to a COLORREF structure.
ms.assetid: f7a3eab0-16ca-4c4e-9eda-bead8d1a91b8
title: RGBFromIMEColorStyle function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RGBFromIMEColorStyle function

Converts an **IMECOLORSTY** structure to a [**COLORREF**](https://msdn.microsoft.com/b87d3de2-7a13-44ef-8253-c6851a75fa54) structure.

## Syntax


```C++
COLORREF RGBFromIMEColorStyle(
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

Returns a [**COLORREF**](https://msdn.microsoft.com/b87d3de2-7a13-44ef-8253-c6851a75fa54) structure.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**COLORREF**](https://msdn.microsoft.com/b87d3de2-7a13-44ef-8253-c6851a75fa54)
</dt> <dt>

[**PColorStyleBackFromIMEStyle**](pcolorstylebackfromimestyle.md)
</dt> <dt>

[**PColorStyleTextFromIMEStyle**](pcolorstyletextfromimestyle.md)
</dt> </dl>

 

 




