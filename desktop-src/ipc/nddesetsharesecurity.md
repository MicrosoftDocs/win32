---
description: Sets the security descriptor associated with the DDE share.
ms.assetid: 8bb8c466-3dd7-49a6-8ba5-632001b8a47f
title: NDdeSetShareSecurity function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- NDdeSetShareSecurity
- NDdeSetShareSecurityA
- NDdeSetShareSecurityW
api_type:
- DllExport
api_location:
- Nddeapi.dll
---

# NDdeSetShareSecurity function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Sets the security descriptor associated with the DDE share. This is done usually after editing the DACL assigned to the DDE share.

## Syntax


```C++
UINT NDdeSetShareSecurity(
  _In_ LPTSTR               lpszServer,
  _In_ LPTSTR               lpszShareName,
  _In_ SECURITY_INFORMATION si,
  _In_ PSECURITY_DESCRIPTOR pSD
);
```



## Parameters

<dl> <dt>

*lpszServer* \[in\]
</dt> <dd>

The name of the server whose DSDM is to be modified.

</dd> <dt>

*lpszShareName* \[in\]
</dt> <dd>

The name of the share whose security descriptor is to be modified. This parameter cannot be **NULL**.

</dd> <dt>

*si* \[in\]
</dt> <dd>

A [**SECURITY\_INFORMATION**](/windows/desktop/SecAuthZ/security-information) value that identifies the security information to retrieve.

</dd> <dt>

*pSD* \[in\]
</dt> <dd>

A pointer to a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure that contains security information. This parameter cannot be **NULL** and should point to a valid security descriptor.

</dd> </dl>

## Return value

If the function succeeds, the return value is NDDE\_NO\_ERROR.

If the function fails, the return value is an error code, which can be translated into a text error message by calling [**NDdeGetErrorString**](nddegeterrorstring.md).

## Remarks

To modify the [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) associated with a DDE share in the DSDM, the user must have appropriate privilege; the share creator has this privilege.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeSetShareSecurityW** (Unicode) and **NDdeSetShareSecurityA** (ANSI)<br/>    |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**SECURITY\_INFORMATION**](/windows/desktop/SecAuthZ/security-information)
</dt> <dt>

[**NDdeGetShareSecurity**](nddegetsharesecurity.md)
</dt> </dl>

 

