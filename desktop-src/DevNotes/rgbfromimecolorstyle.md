---
Description: 'Converts an IMECOLORSTY structure to a COLORREF structure.'
ms.assetid: 'f7a3eab0-16ca-4c4e-9eda-bead8d1a91b8'
title: RGBFromIMEColorStyle function
---

# RGBFromIMEColorStyle function

Converts an **IMECOLORSTY** structure to a [**COLORREF**](gdi.colorref) structure.

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

Returns a [**COLORREF**](gdi.colorref) structure.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**COLORREF**](gdi.colorref)
</dt> <dt>

[**PColorStyleBackFromIMEStyle**](pcolorstylebackfromimestyle.md)
</dt> <dt>

[**PColorStyleTextFromIMEStyle**](pcolorstyletextfromimestyle.md)
</dt> </dl>

 

 




