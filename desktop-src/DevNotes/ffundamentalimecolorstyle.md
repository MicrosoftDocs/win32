---
Description: Specifies whether the specified color is a fundamental color.
ms.assetid: 9a06fadc-9b97-4f7d-9488-688b72d14bc5
title: FFundamentalIMEColorStyle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FFundamentalIMEColorStyle function

Specifies whether the specified color is a fundamental color.

## Syntax


```C++
BOOL __cdecl FFundamentalIMEColorStyle(
  _In_ const IMECOLORSTY *pcolorstyle
);
```



## Parameters

<dl> <dt>

*pcolorstyle* \[in\]
</dt> <dd>

An **IMECOLORSTY** structure returned from the [**PColorStyleBackFromIMEStyle**](pcolorstylebackfromimestyle.md) or [**PColorStyleTextFromIMEStyle**](pcolorstyletextfromimestyle.md) function.

</dd> </dl>

## Return value

Returns **TRUE** when the color is a fundamental color.

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

 

 




