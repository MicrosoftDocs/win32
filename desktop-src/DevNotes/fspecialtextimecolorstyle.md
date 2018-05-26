---
Description: Specifies whether the specified color is a special text color.
ms.assetid: 527806f5-5046-48b0-a8db-86a5b8c0db08
title: FSpecialTextIMEColorStyle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FSpecialTextIMEColorStyle function

Specifies whether the specified color is a special text color.

## Syntax


```C++
BOOL __cdecl FSpecialTextIMEColorStyle(
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

Returns **TRUE** when the color is a special text color.

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

 

 




