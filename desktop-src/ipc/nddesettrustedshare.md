---
description: Grants the specified DDE share trusted status within the current users context.
ms.assetid: 508d3603-468c-4ecb-8e5c-0ab86c2ff3b4
title: NDdeSetTrustedShare function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeSetTrustedShare
- NDdeSetTrustedShareA
- NDdeSetTrustedShareW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeSetTrustedShare function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Grants the specified DDE share trusted status within the current user's context.

## Syntax


```C++
UINT NDdeSetTrustedShare(
  _In_ LPTSTR lpszServer,
  _In_ LPTSTR lpszShareName,
  _In_ DWORD  dwTrustOptions
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

The name of the share to be granted trusted status. This parameter cannot be **NULL**.

</dd> <dt>

*dwTrustOptions* \[in\]
</dt> <dd>

The options affecting the trusted status of the DDE share. This parameter can be one of the following values.



| Option                                                                                                                                                                                                                                                      | Meaning                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <span id="NDDE_CMD_SHOW_MASK"></span><span id="ndde_cmd_show_mask"></span><dl> <dt>**NDDE\_CMD\_SHOW\_MASK**</dt> <dt>0x0000FFFFL</dt> </dl>             | Mask used to obtain the value used to override the DDE share show state, if NDDE\_TRUST\_CMD\_SHOW is set.<br/> |
| <span id="NDDE_TRUST_CMD_SHOW"></span><span id="ndde_trust_cmd_show"></span><dl> <dt>**NDDE\_TRUST\_CMD\_SHOW**</dt> <dt>0x10000000L</dt> </dl>          | Override the show state specified in the DDE share DSDM.<br/>                                                   |
| <span id="NDDE_TRUST_SHARE_DEL"></span><span id="ndde_trust_share_del"></span><dl> <dt>**NDDE\_TRUST\_SHARE\_DEL**</dt> <dt>0x20000000L</dt> </dl>       | Remove the share's trusted status.<br/>                                                                         |
| <span id="NDDE_TRUST_SHARE_INIT"></span><span id="ndde_trust_share_init"></span><dl> <dt>**NDDE\_TRUST\_SHARE\_INIT**</dt> <dt>0x40000000L</dt> </dl>    | Allow a client to initiate to the application if it is already running in the user's context.<br/>              |
| <span id="NDDE_TRUST_SHARE_START"></span><span id="ndde_trust_share_start"></span><dl> <dt>**NDDE\_TRUST\_SHARE\_START**</dt> <dt>0x80000000L</dt> </dl> | Allow the application to be started in the user's context.<br/>                                                 |



 

</dd> </dl>

## Return value

If the function succeeds, the return value is NDDE\_NO\_ERROR.

If the function fails, the return value is an error code, which can be translated into a text error message by calling [**NDdeGetErrorString**](nddegeterrorstring.md).

## Remarks

The DDE share must first be created with [**NDdeShareAdd**](nddeshareadd.md).

If **NDdeSetTrustedShare** is called with *dwTrustOptions* set to zero, the trusted share loses its trusted status.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeSetTrustedShareW** (Unicode) and **NDdeSetTrustedShareA** (ANSI)<br/>      |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**NDdeShareAdd**](nddeshareadd.md)
</dt> </dl>

 

 




