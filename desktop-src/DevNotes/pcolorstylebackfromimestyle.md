---
Description: Retrieves the background color style of the specified style.
ms.assetid: 1b0acac1-c36d-49b6-8154-f69bda008e9a
title: PColorStyleBackFromIMEStyle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

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

 

 




