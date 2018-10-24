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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrawTextWrap function

\[**DrawTextWrap** is available through Windows XP with Service Pack 2 (SP2). It might be altered or unavailable in subsequent versions. It is recommended to use [**DrawText**](https://msdn.microsoft.com/library/windows/desktop/dd162498) directly instead.\]

Draws formatted text in the specified rectangle. It formats the text according to the specified method (expanding tabs, justifying characters, breaking lines, and so on). This function wraps a call to [**DrawText**](https://msdn.microsoft.com/library/windows/desktop/dd162498).

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

Type: **[**HDC**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hdc)**

A handle to the device context.

</dd> <dt>

*lpString* \[in, out\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751#lpctstr)**

A pointer to a buffer that contains the text to draw. If the *nCount* parameter is -1, the string must be null-terminated.

If *uFormat* includes DT\_MODIFYSTRING, the function might add up to four additional characters to this string. The buffer that contains the string should be large enough to accommodate these extra characters.

</dd> <dt>

*nCount* \[in\]
</dt> <dd>

Type: **int**

The length of the string pointed to by *lpString*. If *nCount* is -1, then the *lpString* parameter is assumed to be a pointer to a null-terminated string and [**DrawText**](https://msdn.microsoft.com/library/windows/desktop/dd162498) computes the character count automatically.

</dd> <dt>

*lpRect* \[in, out\]
</dt> <dd>

Type: **LPRECT**

A pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that contains the rectangle, in logical coordinates, in which the text is to be formatted.

</dd> <dt>

*uFormat* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#uint)**

The formatting options. See the documentation for [**DrawText**](https://msdn.microsoft.com/library/windows/desktop/dd162498) for a complete list of options.

</dd> <dt>

*lpDTParams* \[in\]
</dt> <dd>

Type: **LPDRAWTEXTPARAMS**

A pointer to a [**DRAWTEXTPARAMS**](https://msdn.microsoft.com/library/windows/desktop/dd162500) structure that specifies additional formatting options. This parameter can be **NULL**.

</dd> </dl>

## Return value

Type: **int**

If the function succeeds, the return value is the text height in logical units. If **DT\_VCENTER** or **DT\_BOTTOM** is specified, the return value is the offset from the **top** member of *lprc* to the bottom of the drawn text If the function fails, the return value is zero.

If the function fails, the return value is zero.

To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

**DrawTextWrap** is not exported by name or declared in a public header. To use it, you must use [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) and request ordinal 415 from ComCtl32.dll to obtain a function pointer.

For additional remarks, please see [**DrawText**](https://msdn.microsoft.com/library/windows/desktop/dd162498).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 6.0 or later)</dt> </dl> |



 

 





