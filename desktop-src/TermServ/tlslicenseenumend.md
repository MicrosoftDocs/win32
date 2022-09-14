---
title: TLSLicenseEnumEnd function
description: Continues from a previous call to the TLSLicenseEnumBegin function and terminates the enumeration.
ms.assetid: b9cba03c-0f5a-41e8-ae13-bcdd0ac6dd99
ms.tgt_platform: multiple
keywords:
- TLSLicenseEnumEnd function Remote Desktop Services
topic_type:
- apiref
api_name:
- TLSLicenseEnumEnd
api_location:
- Mstlsapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# TLSLicenseEnumEnd function

Continues from a previous call to the [**TLSLicenseEnumBegin**](tlslicenseenumbegin.md) function and terminates the enumeration.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mstlsapi.dll.

 

## Syntax


```C++
DWORD WINAPI TLSLicenseEnumEnd(
  _In_  TLS_HANDLE hHandle,
  _Out_ PDWORD     pdwErrCode
);
```



## Parameters

<dl> <dt>

*hHandle* \[in\]
</dt> <dd>

Handle to a Remote Desktop license server. Specify a handle that is opened by the [**TLSConnectToLsServer**](tlsconnecttolsserver.md) function.

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

<span id="LSERVER_E_INVALID_HANDLE"></span><span id="lserver_e_invalid_handle"></span>

<span id="LSERVER_E_INVALID_HANDLE"></span><span id="lserver_e_invalid_handle"></span>**LSERVER\_E\_INVALID\_HANDLE** (5005)


</dt> <dd>

The handle is not valid.

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

[**TLSLicenseEnumNext**](tlslicenseenumnext.md)
</dt> </dl>

 

