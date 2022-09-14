---
title: ExtTextOutWrap function
description: Draws text using the currently selected font, background color, and text color. You can optionally provide dimensions to be used for clipping, opacity, or both. This function wraps a call to ExtTextOut.
ms.assetid: 0804c231-53f9-4de6-b703-0077cdcebcb5
keywords:
- ExtTextOutWrap function Windows Controls
topic_type:
- apiref
api_name:
- ExtTextOutWrap
api_location:
- Comctl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ExtTextOutWrap function

\[**ExtTextOutWrap** is available through Windows XP with Service Pack 2 (SP2). It might be altered or unavailable in subsequent versions. It is recommended to use [**ExtTextOut**](/windows/desktop/api/wingdi/nf-wingdi-exttextouta) directly instead.\]

Draws text using the currently selected font, background color, and text color. You can optionally provide dimensions to be used for clipping, opacity, or both. This function wraps a call to [**ExtTextOut**](/windows/desktop/api/wingdi/nf-wingdi-exttextouta).

## Syntax


```C++
BOOL ExtTextOutWrap(
  _In_       HDC     hdc,
  _In_       int     X,
  _In_       int     Y,
  _In_       UINT    uOptions,
  _In_ const RECT    *lprc,
  _In_       LPCTSTR lpString,
  _In_       UINT    cbCount,
  _In_ const INT     *lpDx
);
```



## Parameters

<dl> <dt>

*hdc* \[in\]
</dt> <dd>

Type: **[**HDC**](/windows/desktop/WinProg/windows-data-types)**

A handle to the device context.

</dd> <dt>

*X* \[in\]
</dt> <dd>

Type: **int**

The x-coordinate, in logical coordinates, of the reference point used to position the string.

</dd> <dt>

*Y* \[in\]
</dt> <dd>

Type: **int**

The y-coordinate, in logical coordinates, of the reference point used to position the string.

</dd> <dt>

*uOptions* \[in\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

Values that specify how to use the application-defined rectangle. See [**ExtTextOut**](/windows/desktop/api/wingdi/nf-wingdi-exttextouta) for a complete list of options.

</dd> <dt>

*lprc* \[in\]
</dt> <dd>

Type: **const [**RECT**](/previous-versions//dd162897(v=vs.85))\***

A pointer to an optional [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that specifies the dimensions, in logical coordinates, of a rectangle that is used for clipping, opacity, or both.

</dd> <dt>

*lpString* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](/windows/desktop/WinProg/windows-data-types)**

A pointer to a buffer that contains the text to be drawn. The string does not need to be zero-terminated, since *cbCount* specifies the length of the string.

</dd> <dt>

*cbCount* \[in\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The length of the string, in bytes, pointed to by *lpString*.

</dd> <dt>

*lpDx* \[in\]
</dt> <dd>

Type: **const [**INT**](/windows/desktop/WinProg/windows-data-types)\***

A pointer to an optional array of values that indicate the distance between origins of adjacent character cells. For example, *lpDx*\[x\] logical units separate the origins of character cell x and character cell (x + 1).

</dd> </dl>

## Return value

Type: **[**BOOL**](/windows/desktop/WinProg/windows-data-types)**

Returns a nonzero value if the string is drawn successfully. However, if the ANSI version of [**ExtTextOut**](/windows/desktop/api/wingdi/nf-wingdi-exttextouta) is called with ETO\_GLYPH\_INDEX, the function returns **TRUE** even though the function does nothing.

If the function fails, the return value is zero.

To get extended error information, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

**ExtTextOutWrap** is not exported by name or declared in a public header file. To use it, you must use [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) and request ordinal 417 from ComCtl32.dll to obtain a function pointer.

For additional remarks, please see [**ExtTextOut**](/windows/desktop/api/wingdi/nf-wingdi-exttextouta).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 6.0 or later)</dt> </dl> |



 

