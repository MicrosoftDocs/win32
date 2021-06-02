---
description: Deletes a DDE share from the DDE share database manager (DSDM).
ms.assetid: 3240f4b1-2625-46bc-9bbe-27737c59df81
title: NDdeShareDel function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeShareDel
- NDdeShareDelA
- NDdeShareDelW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeShareDel function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Deletes a DDE share from the DDE share database manager (DSDM).

## Syntax


```C++
UINT NDdeShareDel(
  _In_ LPTSTR lpszServer,
  _In_ LPTSTR lpszShareName,
  _In_ UINT   wReserved
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

The name of the share to be deleted from the DSDM. This parameter cannot be **NULL**.

</dd> <dt>

*wReserved* \[in\]
</dt> <dd>

Reserved. This parameter must be zero.

</dd> </dl>

## Return value

If the function succeeds, the return value is NDDE\_NO\_ERROR.

If the function fails, the return value is an error code which can be translated into a text error message by calling [**NDdeGetErrorString**](nddegeterrorstring.md).

## Remarks

To delete a DDE share from the DSDM, you must have the appropriate privilege. The share creator has delete privilege.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeShareDelW** (Unicode) and **NDdeShareDelA** (ANSI)<br/>                    |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> </dl>

 

 




