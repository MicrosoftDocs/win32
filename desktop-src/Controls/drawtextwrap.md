---
title: DrawTextWrap function
description: Draws formatted text in the specified rectangle. It formats the text according to the specified method (expanding tabs, justifying characters, breaking lines, and so on). This function wraps a call to DrawText.
ms.assetid: 28ab4c5e-3b8f-49e8-b072-500ba1916caf
keywords:
- DrawTextWrap function Windows Controls
topic_type:
- apiref
api_name:
- DrawTextWrap
api_location:
- Comctl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DrawTextWrap function

\[**DrawTextWrap** is available through Windows XP with Service Pack 2 (SP2). It might be altered or unavailable in subsequent versions. It is recommended to use [**DrawText**](/windows/desktop/api/winuser/nf-winuser-drawtext) directly instead.\]

Draws formatted text in the specified rectangle. It formats the text according to the specified method (expanding tabs, justifying characters, breaking lines, and so on). This function wraps a call to [**DrawText**](/windows/desktop/api/winuser/nf-winuser-drawtext).

## Syntax


```C++
int WINAPI DrawTextWrap(
  _In_    HDC              hdc,
  _Inout_ LPCTSTR          lpString,
  _In_    int              nCount,
  _Inout_ LPRECT           lpRect,
  _In_    UINT             uFormat,
  _In_    LPDRAWTEXTPARAMS lpDTParams
);
```



## Parameters

<dl> <dt>

*hdc* \[in\]
</dt> <dd>

Type: **[**HDC**](/windows/desktop/WinProg/windows-data-types)**

A handle to the device context.

</dd> <dt>

*lpString* \[in, out\]
</dt> <dd>

Type: **[**LPCTSTR**](/windows/desktop/WinProg/windows-data-types)**

A pointer to a buffer that contains the text to draw. If the *nCount* parameter is -1, the string must be null-terminated.

If *uFormat* includes DT\_MODIFYSTRING, the function might add up to four additional characters to this string. The buffer that contains the string should be large enough to accommodate these extra characters.

</dd> <dt>

*nCount* \[in\]
</dt> <dd>

Type: **int**

The length of the string pointed to by *lpString*. If *nCount* is -1, then the *lpString* parameter is assumed to be a pointer to a null-terminated string and [**DrawText**](/windows/desktop/api/winuser/nf-winuser-drawtext) computes the character count automatically.

</dd> <dt>

*lpRect* \[in, out\]
</dt> <dd>

Type: **LPRECT**

A pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that contains the rectangle, in logical coordinates, in which the text is to be formatted.

</dd> <dt>

*uFormat* \[in\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The formatting options. See the documentation for [**DrawText**](/windows/desktop/api/winuser/nf-winuser-drawtext) for a complete list of options.

</dd> <dt>

*lpDTParams* \[in\]
</dt> <dd>

Type: **LPDRAWTEXTPARAMS**

A pointer to a [**DRAWTEXTPARAMS**](/windows/win32/api/winuser/ns-winuser-drawtextparams) structure that specifies additional formatting options. This parameter can be **NULL**.

</dd> </dl>

## Return value

Type: **int**

If the function succeeds, the return value is the text height in logical units. If **DT\_VCENTER** or **DT\_BOTTOM** is specified, the return value is the offset from the **top** member of *lprc* to the bottom of the drawn text If the function fails, the return value is zero.

If the function fails, the return value is zero.

To get extended error information, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

**DrawTextWrap** is not exported by name or declared in a public header. To use it, you must use [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) and request ordinal 415 from ComCtl32.dll to obtain a function pointer.

For additional remarks, please see [**DrawText**](/windows/desktop/api/winuser/nf-winuser-drawtext).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 6.0 or later)</dt> </dl> |



 

