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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ExtTextOutWrap function

\[**ExtTextOutWrap** is available through Windows XP with Service Pack 2 (SP2). It might be altered or unavailable in subsequent versions. It is recommended to use [**ExtTextOut**](https://msdn.microsoft.com/library/windows/desktop/dd162713) directly instead.\]

Draws text using the currently selected font, background color, and text color. You can optionally provide dimensions to be used for clipping, opacity, or both. This function wraps a call to [**ExtTextOut**](https://msdn.microsoft.com/library/windows/desktop/dd162713).

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

Type: **[**HDC**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hdc)**

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

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#uint)**

Values that specify how to use the application-defined rectangle. See [**ExtTextOut**](https://msdn.microsoft.com/library/windows/desktop/dd162713) for a complete list of options.

</dd> <dt>

*lprc* \[in\]
</dt> <dd>

Type: **const [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897)\***

A pointer to an optional [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that specifies the dimensions, in logical coordinates, of a rectangle that is used for clipping, opacity, or both.

</dd> <dt>

*lpString* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751#lpctstr)**

A pointer to a buffer that contains the text to be drawn. The string does not need to be zero-terminated, since *cbCount* specifies the length of the string.

</dd> <dt>

*cbCount* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#uint)**

The length of the string, in bytes, pointed to by *lpString*.

</dd> <dt>

*lpDx* \[in\]
</dt> <dd>

Type: **const [**INT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#int)\***

A pointer to an optional array of values that indicate the distance between origins of adjacent character cells. For example, *lpDx*\[x\] logical units separate the origins of character cell x and character cell (x + 1).

</dd> </dl>

## Return value

Type: **[**BOOL**](https://msdn.microsoft.com/library/windows/desktop/aa383751#bool)**

Returns a nonzero value if the string is drawn successfully. However, if the ANSI version of [**ExtTextOut**](https://msdn.microsoft.com/library/windows/desktop/dd162713) is called with ETO\_GLYPH\_INDEX, the function returns **TRUE** even though the function does nothing.

If the function fails, the return value is zero.

To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

**ExtTextOutWrap** is not exported by name or declared in a public header file. To use it, you must use [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) and request ordinal 417 from ComCtl32.dll to obtain a function pointer.

For additional remarks, please see [**ExtTextOut**](https://msdn.microsoft.com/library/windows/desktop/dd162713).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 6.0 or later)</dt> </dl> |



 

 





