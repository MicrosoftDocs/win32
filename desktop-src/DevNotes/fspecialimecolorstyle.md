---
Description: Specifies whether the specified color is a special color.
ms.assetid: fda856c4-37b9-444f-9c54-d9eb848a4b05
title: FSpecialIMEColorStyle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FSpecialIMEColorStyle function

Specifies whether the specified color is a special color.

## Syntax


```C++
BOOL __cdecl FSpecialIMEColorStyle(
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

Returns **TRUE** when the color is a special color.

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

 

 




