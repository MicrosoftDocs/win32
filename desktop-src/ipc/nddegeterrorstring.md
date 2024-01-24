---
description: Converts an error code returned by a network DDE function into an error string that explains the returned error code.
ms.assetid: 7077e3bc-df6e-401b-9ac7-15144b79af96
title: NDdeGetErrorString function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeGetErrorString
- NDdeGetErrorStringA
- NDdeGetErrorStringW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeGetErrorString function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Converts an error code returned by a network DDE function into an error string that explains the returned error code.

## Syntax


```C++
UINT NDdeGetErrorString(
  _In_  UINT   uErrorCode,
  _Out_ LPTSTR lpszErrorString,
  _In_  DWORD  cBufSize
);
```



## Parameters

<dl> <dt>

*uErrorCode* \[in\]
</dt> <dd>

The error code to be converted into an error string.

</dd> <dt>

*lpszErrorString* \[out\]
</dt> <dd>

A pointer to a buffer that receives the translated error string. This parameter cannot be **NULL**. If the buffer is not large enough to store the complete error string, the string is truncated.

</dd> <dt>

*cBufSize* \[in\]
</dt> <dd>

The size of the buffer to receive the error string, in **TCHARs**.

</dd> </dl>

## Return value

If the function succeeds, the return value is zero.

If the function fails, the return value is a nonzero error code. If the *lpszErrorString* buffer is not large enough to accept the complete error string, and the string is truncated, the function returns the value NDDE\_INTERNAL\_ERROR.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeGetErrorStringW** (Unicode) and **NDdeGetErrorStringA** (ANSI)<br/>        |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> </dl>

 

 




