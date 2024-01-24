---
description: Retrieves the names of all network DDE shares that are trusted in the context of the calling process.
ms.assetid: 8e2323a4-0c27-44e6-9598-08a3c1a88bd3
title: NDdeTrustedShareEnum function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeTrustedShareEnum
- NDdeTrustedShareEnumA
- NDdeTrustedShareEnumW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeTrustedShareEnum function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Retrieves the names of all network DDE shares that are trusted in the context of the calling process.

## Syntax


```C++
UINT NDdeTrustedShareEnum(
  _In_  LPTSTR  lpszServer,
  _In_  UINT    nLevel,
  _Out_ LPBYTE  lpBuffer,
  _In_  DWORD   cBufSize,
  _Out_ LPDWORD lpnEntriesRead,
  _Out_ LPDWORD lpcbTotalAvailable
);
```



## Parameters

<dl> <dt>

*lpszServer* \[in\]
</dt> <dd>

The name of the server on which the DSDM resides.

</dd> <dt>

*nLevel* \[in\]
</dt> <dd>

Reserved. This parameter must be zero.

</dd> <dt>

*lpBuffer* \[out\]
</dt> <dd>

A pointer to a buffer that receives the list of trusted DDE shares. The list of trusted DDE shares is returned as a sequence of null-separated strings terminating with a double null character at the end. This parameter can be **NULL**. If the *lpBuffer* is **NULL**, the DSDM returns the size of buffer required to hold the list of shares in the *lpcbTotalAvailable* field.

</dd> <dt>

*cBufSize* \[in\]
</dt> <dd>

The size of the *lpBuffer* buffer, in bytes. This parameter must be zero if *lpBuffer* is **NULL**.

</dd> <dt>

*lpnEntriesRead* \[out\]
</dt> <dd>

A pointer to a variable that receives the total number of trusted shares being enumerated. This parameter cannot be **NULL**.

</dd> <dt>

*lpcbTotalAvailable* \[out\]
</dt> <dd>

A pointer to a variable that receives the total number of bytes needed to store the list of trusted DDE shares. This parameter cannot be **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return value is NDDE\_NO\_ERROR.

If the function fails, the return value is an error code, which can be translated into a text error message by calling [**NDdeGetErrorString**](nddegeterrorstring.md). If the *lpBuffer* parameter is **NULL**, it returns NDDE\_BUF\_TOO\_SMALL.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeTrustedShareEnumW** (Unicode) and **NDdeTrustedShareEnumA** (ANSI)<br/>    |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> </dl>

 

 




