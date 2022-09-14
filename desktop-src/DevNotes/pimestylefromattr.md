---
description: Retrieves styles for a given attribute.
ms.assetid: 206c69b9-981b-49ef-9f71-1c65e08637bb
title: PIMEStyleFromAttr function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PIMEStyleFromAttr
api_type: 
- DllExport
api_location: 
- Imeshare.dll
---

# PIMEStyleFromAttr function

Retrieves styles for a given attribute.

## Syntax


```C++
const IMESTYLE* __cdecl PIMEStyleFromAttr(
  _In_ const  UINT attr
);
```



## Parameters

<dl> <dt>

*attr* \[in\]
</dt> <dd>

This parameter can be one of the following values.

<dl> <dt>

<span id="IMESATTR_FIXEDCONVERTED"></span><span id="imesattr_fixedconverted"></span>**IMESATTR\_FIXEDCONVERTED** (5)
</dt> <dt>

<span id="IMESATTR_INPUT"></span><span id="imesattr_input"></span>**IMESATTR\_INPUT** (0)
</dt> <dt>

<span id="IMESATTR_INPUT_ERROR"></span><span id="imesattr_input_error"></span>**IMESATTR\_INPUT\_ERROR** (4)
</dt> <dt>

<span id="IMESATTR_MAX"></span><span id="imesattr_max"></span>**IMESATTR\_MAX** (5)
</dt> <dt>

<span id="IMESATTR_MIN"></span><span id="imesattr_min"></span>**IMESATTR\_MIN** (0)
</dt> <dt>

<span id="IMESATTR_TARGET_CONVERTED"></span><span id="imesattr_target_converted"></span>**IMESATTR\_TARGET\_CONVERTED** (1)
</dt> <dt>

<span id="IMESATTR_TARGET_NOTCONVERTED"></span><span id="imesattr_target_notconverted"></span>**IMESATTR\_TARGET\_NOTCONVERTED** (4)
</dt> </dl> </dd> </dl>

## Return value

Returns a pointer to an **IMESTYLE** structure representing the color and non-color settings.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

The **IMESTYLE** structure is defined as follows:

``` syntax
typedef struct {
    union {
        GRFSTY  grfsty;
        struct {
            UINT    fBold:1;
            UINT    fItalic:1;
            UINT    fUl:1;
            UINT    idUl:(sizeof(UINT) * 8 - 3);
        };
    };

    union {
        IMECOLORSTY colorstyText;
        struct {
            UINT    colorIdText;
            union {
                COLORREF    rgbText;
                UINT        colorWinText;
                UINT        colorSpecText;
                UINT        colorFundText;
            };
        };
    };

    union {
        IMECOLORSTY colorstyBack;
        struct {
            UINT    colorIdBack;
            union {
                COLORREF    rgbBack;
                UINT        colorWinBack;
                UINT        colorSpecBack;
                UINT        colorFundBack;
            };
        };
    };

    union {
        IMECOLORSTY colorstyUl;
        struct {
            UINT    colorIdUl;
            union {
                COLORREF    rgbUl;
                UINT        colorWinUl;
                UINT        colorSpecUl;
                UINT        colorFundUl;
            };
        };
    };
} IMESTYLE;
```

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



 

 
