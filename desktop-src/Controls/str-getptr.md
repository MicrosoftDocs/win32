---
title: Str\_GetPtr function
description: Copies a string from one buffer to another.
ms.assetid: a3dd55a0-3f8b-4d6c-9956-666bebc3ab8d
keywords:
- Str_GetPtr function Windows Controls
topic_type:
- apiref
api_name:
- Str_GetPtr
- Str_GetPtrA
- Str_GetPtrW
api_location:
- ComCtl32.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Str\_GetPtr function

\[This function is available through Windows XP with Service Pack 2 (SP2) and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows.\]

Copies a string from one buffer to another.

## Syntax


```C++
int WINAPI Str_GetPtr(
  _In_    LPCTSTR pszSource,
  _Inout_ LPCSTR  pszDest,
  _In_    int     cchDest
);
```



## Parameters

<dl> <dt>

*pszSource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751#lpctstr)**

A pointer to a source string.

</dd> <dt>

*pszDest* \[in, out\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751#lpcstr)**

A pointer to the destination buffer. This value can be **NULL**.

</dd> <dt>

*cchDest* \[in\]
</dt> <dd>

Type: **int**

The size of *pszDest*, in characters.

</dd> </dl>

## Return value

Type: **int**

If *pszDest* is **NULL** or *cchDest* is zero, returns the size of the buffer, in characters, needed to contain a null-terminated copy of the string pointed to by *pszSource*.

If *pszDest* is non-**NULL**, returns the number of characters successfully copied, including the terminating null character.

If *pszDest* cannot hold the entire string pointed to by *pszSource*, then (*cchDest*-1) characters are copied, the string null-terminated, and *cchDest* returned.

## Remarks

**Str\_GetPtr** is available as ANSI (**Str\_GetPtrA**) and Unicode (**Str\_GetPtrW**) versions. These functions are not exported by name or declared in a public header file. To use them, you must use [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) and request ordinal 233 (**Str\_GetPtrA**) or 235 (**Str\_GetPtrW**) from ComCtl32.dll to obtain a function pointer.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>ComCtl32.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **Str\_GetPtrW** (Unicode) and **Str\_GetPtrA** (ANSI)<br/>                       |



 

 





