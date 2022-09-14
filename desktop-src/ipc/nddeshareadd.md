---
description: Creates and adds a new DDE share to the DDE share database manager (DSDM).
ms.assetid: c9814919-412e-4f13-98cc-373b69545734
title: NDdeShareAdd function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- NDdeShareAdd
- NDdeShareAddA
- NDdeShareAddW
api_type:
- DllExport
api_location:
- Nddeapi.dll
---

# NDdeShareAdd function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Creates and adds a new DDE share to the DDE share database manager (DSDM).

## Syntax


```C++
UINT NDdeShareAdd(
  _In_ LPTSTR               lpszServer,
  _In_ UINT                 nLevel,
  _In_ PSECURITY_DESCRIPTOR pSD,
  _In_ LPBYTE               lpBuffer,
  _In_ DWORD                cBufSize
);
```



## Parameters

<dl> <dt>

*lpszServer* \[in\]
</dt> <dd>

The name of the server whose DSDM is to be modified.

</dd> <dt>

*nLevel* \[in\]
</dt> <dd>

The information level. This parameter must be 2.

</dd> <dt>

*pSD* \[in\]
</dt> <dd>

A pointer to a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure to be associated with this share and against which access checks will be performed on subsequent initiates to this share. This parameter can be **NULL**, in which case the DSDM creates a default security descriptor that grants "Full Control" to the owner and "Read and Link" to everyone.

</dd> <dt>

*lpBuffer* \[in\]
</dt> <dd>

A pointer to the [**NDDESHAREINFO**](nddeshareinfo-str.md) structure that defines the ApplicationTopic list associated with the DDE share being created as well as other parameters. This parameter cannot be **NULL**.

</dd> <dt>

*cBufSize* \[in\]
</dt> <dd>

The size of the *lpBuffer* structure, in bytes. This parameter cannot be zero.

</dd> </dl>

## Return value

If the function succeeds, the return value is NDDE\_NO\_ERROR.

If the function fails, the return value is an error code, which can be translated into a text error message by calling [**NDdeGetErrorString**](nddegeterrorstring.md).

## Remarks

Before a client can connect to the DDE share, it must be trusted with [**NDdeSetTrustedShare**](nddesettrustedshare.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeShareAddW** (Unicode) and **NDdeShareAddA** (ANSI)<br/>                    |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**NDDESHAREINFO**](nddeshareinfo-str.md)
</dt> <dt>

[**NDdeSetTrustedShare**](nddesettrustedshare.md)
</dt> </dl>

 

