---
title: GetTextExtentPoint32Wrap function
description: Computes the width and height of the specified string of text. This function wraps a call to GetTextExtentPoint.
ms.assetid: 156f9344-6071-451c-94c7-63f369a5573a
keywords:
- GetTextExtentPoint32Wrap function Windows Controls
topic_type:
- apiref
api_name:
- GetTextExtentPoint32Wrap
api_location:
- Comctl32.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetTextExtentPoint32Wrap function

\[**GetTextExtentPoint32Wrap** is available through Windows XP with Service Pack 2 (SP2). It might be altered or unavailable in subsequent versions. It is recommended to use [**GetTextExtentPoint**](https://msdn.microsoft.com/library/windows/desktop/dd144937) directly instead.\]

Computes the width and height of the specified string of text. This function wraps a call to [**GetTextExtentPoint**](https://msdn.microsoft.com/library/windows/desktop/dd144937).

## Syntax


```C++
BOOL GetTextExtentPoint32Wrap(
  _In_  HDC     hdc,
  _In_  LPCTSTR lpString,
  _In_  UINT    cbCount,
  _Out_ LPSIZE  lpSize
);
```



## Parameters

<dl> <dt>

*hdc* \[in\]
</dt> <dd>

Type: **[**HDC**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hdc)**

A handle to the device context.

</dd> <dt>

*lpString* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751#lpctstr)**

A pointer to a buffer that contains the text to be drawn. The string does not need to be zero-terminated, since *cbCount* specifies the length of the string.

</dd> <dt>

*cbCount* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#uint)**

The length, in bytes, of the string pointed to by *lpString*.

</dd> <dt>

*lpSize* \[out\]
</dt> <dd>

Type: **LPSIZE**

When this method returns, contains a pointer to a [**SIZE**](https://msdn.microsoft.com/library/windows/desktop/dd145106) structure containing the dimensions of the string, in logical units.

</dd> </dl>

## Return value

Type: **[**BOOL**](https://msdn.microsoft.com/library/windows/desktop/aa383751#bool)**

Returns a nonzero value if successful; otherwise, 0.

To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

**GetTextExtentPoint32Wrap** is not exported by name or declared in a public header file. To use it, you must use [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) and request ordinal 420 from ComCtl32.dll to obtain a function pointer.

For additional remarks, please see [**GetTextExtentPoint**](https://msdn.microsoft.com/library/windows/desktop/dd144937).

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                            |
| DLL<br/>                      | <dl> <dt>Comctl32.dll (version 5.81 or later)</dt> </dl> |



 

 





