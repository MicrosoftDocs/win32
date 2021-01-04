---
title: TLSLicenseEnumNext function
description: Continues from a previous call to the TLSLicenseEnumBegin function and returns the next license that is installed on a Remote Desktop license server that matches the search criteria.
ms.assetid: 6932289b-b59c-493c-8dbc-03c0662e921e
ms.tgt_platform: multiple
keywords:
- TLSLicenseEnumNext function Remote Desktop Services
topic_type:
- apiref
api_name:
- TLSLicenseEnumNext
api_location:
- Mstlsapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# TLSLicenseEnumNext function

Continues from a previous call to the [**TLSLicenseEnumBegin**](tlslicenseenumbegin.md) function and returns the next license that is installed on a Remote Desktop license server that matches the search criteria.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mstlsapi.dll.

 

## Syntax


```C++
DWORD WINAPI TLSLicenseEnumNext(
  _In_  TLS_HANDLE hHandle,
  _In_  LSLicense  *lpLicense,
  _Out_ PDWORD     pdwErrCode
);
```



## Parameters

<dl> <dt>

*hHandle* \[in\]
</dt> <dd>

Handle to a Remote Desktop license server. Specify a handle that is opened by the [**TLSConnectToLsServer**](tlsconnecttolsserver.md) function.

</dd> <dt>

*lpLicense* \[in\]
</dt> <dd>

Pointer to a [**LSLicense**](lslicense.md) structure that receives the next license that matches the search criteria.

</dd> <dt>

*pdwErrCode* \[out\]
</dt> <dd>

Pointer to a variable that receives one of the following error codes on return.

<dt>

<span id="LSERVER_S_SUCCESS"></span><span id="lserver_s_success"></span>

<span id="LSERVER_S_SUCCESS"></span><span id="lserver_s_success"></span>**LSERVER\_S\_SUCCESS** (0)


</dt> <dd>

Call is successful.

</dd> <dt>

<span id="LSERVER_I_NO_MORE_DATA"></span><span id="lserver_i_no_more_data"></span>

<span id="LSERVER_I_NO_MORE_DATA"></span><span id="lserver_i_no_more_data"></span>**LSERVER\_I\_NO\_MORE\_DATA** (4001)


</dt> <dd>

No more licenses match the search criteria.

</dd> <dt>

<span id="LSERVER_E_INTERNAL_ERROR"></span><span id="lserver_e_internal_error"></span>

<span id="LSERVER_E_INTERNAL_ERROR"></span><span id="lserver_e_internal_error"></span>**LSERVER\_E\_INTERNAL\_ERROR** (5001)


</dt> <dd>

Internal error in license server.

</dd> <dt>

<span id="LSERVER_E_INVALID_SEQUENCE"></span><span id="lserver_e_invalid_sequence"></span>

<span id="LSERVER_E_INVALID_SEQUENCE"></span><span id="lserver_e_invalid_sequence"></span>**LSERVER\_E\_INVALID\_SEQUENCE** (5006)


</dt> <dd>

The calling sequence was not valid. Must call the [**TLSLicenseEnumBegin()**](tlslicenseenumbegin.md) function before this.

</dd> <dt>

<span id="LSERVER_E_SERVER_BUSY"></span><span id="lserver_e_server_busy"></span>

<span id="LSERVER_E_SERVER_BUSY"></span><span id="lserver_e_server_busy"></span>**LSERVER\_E\_SERVER\_BUSY** (5007)


</dt> <dd>

License server is too busy to process the request.

</dd> <dt>

<span id="LSERVER_E_OUTOFMEMORY"></span><span id="lserver_e_outofmemory"></span>

<span id="LSERVER_E_OUTOFMEMORY"></span><span id="lserver_e_outofmemory"></span>**LSERVER\_E\_OUTOFMEMORY** (5008)


</dt> <dd>

Cannot process the request because of insufficient memory.

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

The argument was not valid.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Mstlsapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**LSLicense**](lslicense.md)
</dt> <dt>

[**TLSConnectToLsServer**](tlsconnecttolsserver.md)
</dt> <dt>

[**TLSLicenseEnumBegin**](tlslicenseenumbegin.md)
</dt> <dt>

[**TLSLicenseEnumEnd**](tlslicenseenumend.md)
</dt> </dl>

 

