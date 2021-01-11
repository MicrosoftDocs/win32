---
description: Sets DDE share information. This is usually done after editing.
ms.assetid: 002c73ce-7b35-4e8e-bb7e-0e1393b97ccc
title: NDdeShareSetInfo function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeShareSetInfo
- NDdeShareSetInfoA
- NDdeShareSetInfoW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeShareSetInfo function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Sets DDE share information. This is usually done after editing.

## Syntax


```C++
UINT NDdeShareSetInfo(
  _In_ LPTSTR lpszServer,
  _In_ LPTSTR lpszShareName,
  _In_ UINT   nLevel,
  _In_ LPBYTE lpBuffer,
  _In_ DWORD  cBufSize,
  _In_ WORD   sParmNum
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

The name of the share name whose information is to be modified. This parameter cannot be **NULL**.

</dd> <dt>

*nLevel* \[in\]
</dt> <dd>

The information level. This parameter must be 2.

</dd> <dt>

*lpBuffer* \[in\]
</dt> <dd>

A pointer to the [**NDDESHAREINFO**](nddeshareinfo-str.md) structure that specifies the DDE share information to be stored in the DSDM. Currently the DDE share information is modified as a whole, that is, no partial edits are made. This parameter cannot be **NULL**.

</dd> <dt>

*cBufSize* \[in\]
</dt> <dd>

The size of the *lpBuffer* buffer, in bytes.

</dd> <dt>

*sParmNum* \[in\]
</dt> <dd>

The parameter index to be modified. The current implementation does not support partial modification; therefore, this parameter must be zero.

</dd> </dl>

## Return value

If the function succeeds, the return value is NDDE\_NO\_ERROR.

If the function fails, the return value is an error code, which can be translated into a text error message by calling [**NDdeGetErrorString**](nddegeterrorstring.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeShareSetInfoW** (Unicode) and **NDdeShareSetInfoA** (ANSI)<br/>            |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**NDDESHAREINFO**](nddeshareinfo-str.md)
</dt> <dt>

[**NDdeShareGetInfo**](nddesharegetinfo.md)
</dt> </dl>

 

 




