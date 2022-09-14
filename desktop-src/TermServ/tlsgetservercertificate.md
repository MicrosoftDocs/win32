---
title: TLSGetServerCertificate function
description: Returns the certificate of the Remote Desktop license server.
ms.assetid: 7a31e7f9-f6d6-4030-b7db-43be118bb158
ms.tgt_platform: multiple
keywords:
- TLSGetServerCertificate function Remote Desktop Services
topic_type:
- apiref
api_name:
- TLSGetServerCertificate
api_location:
- Mstlsapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# TLSGetServerCertificate function

Returns the certificate of the Remote Desktop license server.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mstlsapi.dll.

 

## Syntax


```C++
DWORD WINAPI TLSGetServerCertificate(
  _In_  TLS_HANDLE hHandle,
  _In_  BOOL       bSignCert,
  _Out_ LPBYTE     *ppbCertBlob,
  _Out_ LPDWORD    lpdwCertBlobLen,
  _Out_ PDWORD     pdwErrCode
);
```



## Parameters

<dl> <dt>

*hHandle* \[in\]
</dt> <dd>

Handle to a Remote Desktop license server that is opened by a call to the [**TLSConnectToLsServer**](tlsconnecttolsserver.md) function.

</dd> <dt>

*bSignCert* \[in\]
</dt> <dd>

**TRUE** if signature certificate, **FALSE** if exchange certificate.

</dd> <dt>

*ppbCertBlob* \[out\]
</dt> <dd>

Pointer to a variable that receives a pointer to a buffer that contains the certificate.

</dd> <dt>

*lpdwCertBlobLen* \[out\]
</dt> <dd>

Pointer to a variable that receives the size of the certificate that is returned.

</dd> <dt>

*pdwErrCode* \[out\]
</dt> <dd>

Pointer to a variable that receives the error code.

<dt>

<span id="LSERVER_S_SUCCESS"></span><span id="lserver_s_success"></span>

<span id="LSERVER_S_SUCCESS"></span><span id="lserver_s_success"></span>**LSERVER\_S\_SUCCESS** (0)


</dt> <dd>

Call is successful.

</dd> <dt>

<span id="TLS_W_SELFSIGN_CERTIFICATE"></span><span id="tls_w_selfsign_certificate"></span>

<span id="TLS_W_SELFSIGN_CERTIFICATE"></span><span id="tls_w_selfsign_certificate"></span>**TLS\_W\_SELFSIGN\_CERTIFICATE** (4007)


</dt> <dd>

Certificate returned is a self-signed certificate.

</dd> <dt>

<span id="TLS_W_TEMP_SELFSIGN_CERT"></span><span id="tls_w_temp_selfsign_cert"></span>

<span id="TLS_W_TEMP_SELFSIGN_CERT"></span><span id="tls_w_temp_selfsign_cert"></span>**TLS\_W\_TEMP\_SELFSIGN\_CERT** (4009)


</dt> <dd>

Certificate returned is temporary.

</dd> <dt>

<span id="TLS_E_ACCESS_DENIED"></span><span id="tls_e_access_denied"></span>

<span id="TLS_E_ACCESS_DENIED"></span><span id="tls_e_access_denied"></span>**TLS\_E\_ACCESS\_DENIED** (5003)


</dt> <dd>

Access denied.

</dd> <dt>

<span id="TLS_E_ALLOCATE_HANDLE"></span><span id="tls_e_allocate_handle"></span>

<span id="TLS_E_ALLOCATE_HANDLE"></span><span id="tls_e_allocate_handle"></span>**TLS\_E\_ALLOCATE\_HANDLE** (5007)


</dt> <dd>

Server is too busy to process the request.

</dd> <dt>

<span id="TLS_E_NO_CERTIFICATE"></span><span id="tls_e_no_certificate"></span>

<span id="TLS_E_NO_CERTIFICATE"></span><span id="tls_e_no_certificate"></span>**TLS\_E\_NO\_CERTIFICATE** (5022)


</dt> <dd>

Cannot retrieve a certificate.

</dd> </dl> </dd> </dl>

## Return value

This function returns the following possible return values.

<dl> <dt>

**RPC\_S\_OK**
</dt> <dd>

The call succeeded. Check the value of the *pdwErrCode* parameter to get the return code for the call.

</dd> <dt>

**RPC\_S\_INVALID\_ARG**
</dt> <dd>

The argument was invalid.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Mstlsapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**TLSConnectToLsServer**](tlsconnecttolsserver.md)
</dt> </dl>

 

