---
Description: Specifies whether the specified color is a special color.
ms.assetid: fda856c4-37b9-444f-9c54-d9eb848a4b05
title: FSpecialIMEColorStyle function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FSpecialIMEColorStyle
api_type: 
- DllExport
api_location: 
- Imeshare.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/library/ms683212(v=VS.85).aspx) functions.

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

 

 




