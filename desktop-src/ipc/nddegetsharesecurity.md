---
description: Retrieves the security descriptor associated with the DDE share. This is done usually for editing.
ms.assetid: 7d3cc965-45ee-40ce-a462-568200592345
title: NDdeGetShareSecurity function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- NDdeGetShareSecurity
- NDdeGetShareSecurityA
- NDdeGetShareSecurityW
api_type:
- DllExport
api_location:
- Nddeapi.dll
---

# NDdeGetShareSecurity function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Retrieves the security descriptor associated with the DDE share. This is done usually for editing.

## Syntax


```C++
UINT NDdeGetShareSecurity(
  _In_  LPTSTR               lpszServer,
  _In_  LPTSTR               lpszShareName,
  _In_  SECURITY_INFORMATION si,
  _Out_ PSECURITY_DESCRIPTOR pSD,
  _In_  DWORD                cbSD,
  _Out_ LPDWORD              lpcbsdRequired
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

The name of the share whose security descriptor is to be retrieved from the DSDM. This parameter cannot be **NULL**.

</dd> <dt>

*si* \[in\]
</dt> <dd>

A [**SECURITY\_INFORMATION**](/windows/desktop/SecAuthZ/security-information) value that specifies the security information to be retrieved from the security descriptor associated with the share.

</dd> <dt>

*pSD* \[out\]
</dt> <dd>

A pointer to a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure that receives the self-relative security descriptor. This parameter can be **NULL**. If this parameter is **NULL**, the DSDM determines the size of the requested security information and returns the number of bytes needed in the *lpcbsdRequired* parameter along with the NDDE\_BUF\_TOO\_SMALL error code.

</dd> <dt>

*cbSD* \[in\]
</dt> <dd>

The size of the *pSD* buffer. This parameter must be zero if *pSD* is **NULL**.

</dd> <dt>

*lpcbsdRequired* \[out\]
</dt> <dd>

A pointer to the variable that receives the actual size of the retrieved security descriptor. This parameter cannot be **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return value is NDDE\_NO\_ERROR.

If the function fails, the return value is an error code, which can be translated into a text error message by calling [**NDdeGetErrorString**](nddegeterrorstring.md). If the *pSD* parameter was **NULL**, it returns NDDE\_BUF\_TOO\_SMALL.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeGetShareSecurityW** (Unicode) and **NDdeGetShareSecurityA** (ANSI)<br/>    |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**SECURITY\_INFORMATION**](/windows/desktop/SecAuthZ/security-information)
</dt> <dt>

[**NDdeSetShareSecurity**](nddesetsharesecurity.md)
</dt> </dl>

 

