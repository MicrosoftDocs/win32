---
Description: Retrieves the background color style of the specified style.
ms.assetid: 1b0acac1-c36d-49b6-8154-f69bda008e9a
title: PColorStyleBackFromIMEStyle function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PColorStyleBackFromIMEStyle
api_type: 
- DllExport
api_location: 
- Imeshare.dll
---

# PColorStyleBackFromIMEStyle function

Retrieves the background color style of the specified style.

## Syntax


```C++
const IMECOLORSTY* __cdecl PColorStyleBackFromIMEStyle(
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

Pointer to an **IMECOLORSTY** structure representing the background color style.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

The **IMECOLORSTY** structure is defined as follows:

``` syntax
typedef struct {
    UINT colorId;
    union {
        COLORREF    rgb;
        UINT        colorWin;
        UINT        colorSpec;
        UINT        colorFund;
    };
} IMECOLORSTY;
```

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**PIMEStyleFromAttr**](pimestylefromattr.md)
</dt> </dl>

 

 




