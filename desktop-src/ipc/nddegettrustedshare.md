---
description: Retrieves the options associated with a DDE share that is in the server users list of trusted shares.
ms.assetid: e5f2b4f8-f922-4734-9fe3-8a74a7f5f619
title: NDdeGetTrustedShare function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeGetTrustedShare
- NDdeGetTrustedShareA
- NDdeGetTrustedShareW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeGetTrustedShare function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Retrieves the options associated with a DDE share that is in the server user's list of trusted shares.

## Syntax


```C++
UINT NDdeGetTrustedShare(
  _In_  LPTSTR  lpszServer,
  _In_  LPTSTR  lpszShareName,
  _Out_ LPDWORD lpdwTrustOptions,
  _Out_ LPDWORD lpdwShareModId0,
  _Out_ LPDWORD lpdwShareModId1
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

The share name whose trusted status is being queried. This parameter cannot be **NULL**.

</dd> <dt>

*lpdwTrustOptions* \[out\]
</dt> <dd>

A pointer to a variable that receives the trust options. This parameter cannot be **NULL**. The following trust options are available.



| Value                                                                                                                                                                                                                                                       | Meaning                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <span id="NDDE_CMD_SHOW_MASK"></span><span id="ndde_cmd_show_mask"></span><dl> <dt>**NDDE\_CMD\_SHOW\_MASK**</dt> <dt>0x0000FFFFL</dt> </dl>             | Mask used to obtain the value used to override the DDE share show state, if NDDE\_TRUST\_CMD\_SHOW is set.<br/> |
| <span id="NDDE_TRUST_CMD_SHOW"></span><span id="ndde_trust_cmd_show"></span><dl> <dt>**NDDE\_TRUST\_CMD\_SHOW**</dt> <dt>0x10000000L</dt> </dl>          | Override the show state specified in the DDE share DSDM.<br/>                                                   |
| <span id="NDDE_TRUST_SHARE_DEL"></span><span id="ndde_trust_share_del"></span><dl> <dt>**NDDE\_TRUST\_SHARE\_DEL**</dt> <dt>0x20000000L</dt> </dl>       | Remove the share's trusted status.<br/>                                                                         |
| <span id="NDDE_TRUST_SHARE_INIT"></span><span id="ndde_trust_share_init"></span><dl> <dt>**NDDE\_TRUST\_SHARE\_INIT**</dt> <dt>0x40000000L</dt> </dl>    | Allow a client to initiate to the application if it is already running in the user's context.<br/>              |
| <span id="NDDE_TRUST_SHARE_START"></span><span id="ndde_trust_share_start"></span><dl> <dt>**NDDE\_TRUST\_SHARE\_START**</dt> <dt>0x80000000L</dt> </dl> | Allow the application to be started in the user's context.<br/>                                                 |



 

</dd> <dt>

*lpdwShareModId0* \[out\]
</dt> <dd>

A pointer to a variable that receives the first part of the trusted share modify identifier. This parameter cannot be **NULL**.

</dd> <dt>

*lpdwShareModId1* \[out\]
</dt> <dd>

A pointer to a variable that receives the second part of the trusted share modify identifier. This parameter cannot be **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return value is NDDE\_NO\_ERROR.

If the function fails, the return value is an error code, which can be translated into a text error message by calling [**NDdeGetErrorString**](nddegeterrorstring.md).

## Remarks

The trusted share modify identifier reflects the version of the DDE share in the DSDM at the time the DDE share was initially granted trusted status. The trusted share modify identifier is primarily used to remove obsolete trusted shares. However, the user does not need to remove obsolete trusted shares. The network DDE agent removes obsolete shares on the user's behalf.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeGetTrustedShareW** (Unicode) and **NDdeGetTrustedShareA** (ANSI)<br/>      |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**NDdeSetTrustedShare**](nddesettrustedshare.md)
</dt> </dl>

 

 




