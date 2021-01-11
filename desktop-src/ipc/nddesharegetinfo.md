---
description: Retrieves DDE share information. This is usually done for editing.
ms.assetid: a2e48a4d-2b72-40a3-b827-474da1db0910
title: NDdeShareGetInfo function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeShareGetInfo
- NDdeShareGetInfoA
- NDdeShareGetInfoW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeShareGetInfo function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Retrieves DDE share information. This is usually done for editing.

## Syntax


```C++
UINT NDdeShareGetInfo(
  _In_  LPTSTR  lpszServer,
  _In_  LPTSTR  lpszShareName,
  _In_  UINT    nLevel,
  _Out_ LPBYTE  lpBuffer,
  _In_  DWORD   cBufSize,
  _Out_ LPDWORD lpnTotalAvailable,
  _In_  LPWORD  lpnItems
);
```



## Parameters

<dl> <dt>

*lpszServer* \[in\]
</dt> <dd>

The name of the server on which the DSDM resides.

</dd> <dt>

*lpszShareName* \[in\]
</dt> <dd>

The share name whose information is to be retrieved from the DSDM. This parameter must not be **NULL**.

</dd> <dt>

*nLevel* \[in\]
</dt> <dd>

The information level. This parameter must be 2.

</dd> <dt>

*lpBuffer* \[out\]
</dt> <dd>

A pointer to a buffer that receives the [**NDDESHAREINFO**](nddeshareinfo-str.md) structure and associated data pointed to by its members. This parameter can be **NULL**. If *lpBuffer* is **NULL**, then the DSDM calculates the number of bytes required to store the requested share information and returns that value in the *lpnTotalAvailable* field along with the NDDE\_BUF\_TOO\_SMALL error.

</dd> <dt>

*cBufSize* \[in\]
</dt> <dd>

The size of the *lpBuffer* buffer, in bytes. If *lpBuffer* is **NULL**, then *cBufSize* should be zero.

</dd> <dt>

*lpnTotalAvailable* \[out\]
</dt> <dd>

A pointer to a variable that receives the total number of bytes needed to store the requested share information. This parameter cannot be **NULL**.

</dd> <dt>

*lpnItems* \[in\]
</dt> <dd>

A pointer to an item selection mask for partial share information retrieval.

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
| Unicode and ANSI names<br/>   | **NDdeShareGetInfoW** (Unicode) and **NDdeShareGetInfoA** (ANSI)<br/>            |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**NDDESHAREINFO**](nddeshareinfo-str.md)
</dt> <dt>

[**NDdeShareSetInfo**](nddesharesetinfo.md)
</dt> </dl>

 

 




