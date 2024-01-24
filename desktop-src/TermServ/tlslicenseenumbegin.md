---
title: TLSLicenseEnumBegin function
description: Begins enumeration of licenses that are issued by the Remote Desktop license server based on search criteria.
ms.assetid: ec575632-b828-49c0-b326-1ab420381875
ms.tgt_platform: multiple
keywords:
- TLSLicenseEnumBegin function Remote Desktop Services
topic_type:
- apiref
api_name:
- TLSLicenseEnumBegin
api_location:
- Mstlsapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# TLSLicenseEnumBegin function

Begins enumeration of licenses that are issued by the Remote Desktop license server based on search criteria.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mstlsapi.dll.

 

## Syntax


```C++
DWORD WINAPI TLSLicenseEnumBegin(
  _In_  TLS_HANDLE hHandle,
  _In_  DWORD      dwSearchParm,
  _In_  BOOL       bMatchAll,
  _In_  LSLicense  *lpSearchParm,
  _Out_ PDWORD     pdwErrCode
);
```



## Parameters

<dl> <dt>

*hHandle* \[in\]
</dt> <dd>

Handle to a Remote Desktop license server. Specify a handle that is opened by the [**TLSConnectToLsServer**](tlsconnecttolsserver.md) function.

</dd> <dt>

*dwSearchParm* \[in\]
</dt> <dd>

Specifies the search criteria. The parameter can be one or a combination of the values that are described in the following list. The parameter specifies the type of key pack and which key pack to search.

<dt>

<span id="LSLICENSE_SEARCH_LICENSEID"></span><span id="lslicense_search_licenseid"></span>

<span id="LSLICENSE_SEARCH_LICENSEID"></span><span id="lslicense_search_licenseid"></span>**LSLICENSE\_SEARCH\_LICENSEID** (0x00000001)


</dt> <dd>

Search by license ID.

</dd> <dt>

<span id="LSLICENSE_SEARCH_KEYPACKID"></span><span id="lslicense_search_keypackid"></span>

<span id="LSLICENSE_SEARCH_KEYPACKID"></span><span id="lslicense_search_keypackid"></span>**LSLICENSE\_SEARCH\_KEYPACKID** (0x00000002)


</dt> <dd>

Search by key pack ID.

</dd> <dt>

<span id="LSLICENSE_SEARCH_MACHINENAME"></span><span id="lslicense_search_machinename"></span>

<span id="LSLICENSE_SEARCH_MACHINENAME"></span><span id="lslicense_search_machinename"></span>**LSLICENSE\_SEARCH\_MACHINENAME** (0x00000008)


</dt> <dd>

Search by machine name.

</dd> <dt>

<span id="LSLICENSE_SEARCH_USERNAME"></span><span id="lslicense_search_username"></span>

<span id="LSLICENSE_SEARCH_USERNAME"></span><span id="lslicense_search_username"></span>**LSLICENSE\_SEARCH\_USERNAME** (0x00000010)


</dt> <dd>

Search by user name.

</dd> <dt>

<span id="LSLICENSE_SEARCH_ISSUEDATE"></span><span id="lslicense_search_issuedate"></span>

<span id="LSLICENSE_SEARCH_ISSUEDATE"></span><span id="lslicense_search_issuedate"></span>**LSLICENSE\_SEARCH\_ISSUEDATE** (0x00000080)


</dt> <dd>

Search by issue date.

</dd> <dt>

<span id="LSLICENSE_SEARCH_EXPIREDATE"></span><span id="lslicense_search_expiredate"></span>

<span id="LSLICENSE_SEARCH_EXPIREDATE"></span><span id="lslicense_search_expiredate"></span>**LSLICENSE\_SEARCH\_EXPIREDATE** (0x00000100)


</dt> <dd>

Search by expiration date.

</dd> <dt>

<span id="LSLICENSE_SEARCH__NUMLICENSES"></span><span id="lslicense_search__numlicenses"></span>

<span id="LSLICENSE_SEARCH__NUMLICENSES"></span><span id="lslicense_search__numlicenses"></span>**LSLICENSE\_SEARCH\_ NUMLICENSES** (0x00000200)


</dt> <dd>

Search by number of licenses.

</dd> <dt>

<span id="LSLICENSE_SEARCH___ENTRY_STATUS"></span><span id="lslicense_search___entry_status"></span>

<span id="LSLICENSE_SEARCH___ENTRY_STATUS"></span><span id="lslicense_search___entry_status"></span>**LSLICENSE\_SEARCH\_ ENTRY\_STATUS** (0x20000000)


</dt> <dd>

Search by entry status.

</dd> <dt>

<span id="LSLICENSE_EXSEARCH_LICENSESTATUS"></span><span id="lslicense_exsearch_licensestatus"></span>

<span id="LSLICENSE_EXSEARCH_LICENSESTATUS"></span><span id="lslicense_exsearch_licensestatus"></span>**LSLICENSE\_EXSEARCH\_LICENSESTATUS** (0x00100000)


</dt> <dd>

Search by license status.

</dd> <dt>

<span id="LSKEYPACK_SEARCH_ALL"></span><span id="lskeypack_search_all"></span>

<span id="LSKEYPACK_SEARCH_ALL"></span><span id="lskeypack_search_all"></span>**LSKEYPACK\_SEARCH\_ALL** (0xFFFFFFFF)


</dt> <dd>

Search all licenses.

</dd> </dl> </dd> <dt>

*bMatchAll* \[in\]
</dt> <dd>

Specifies whether to match all search values.

</dd> <dt>

*lpSearchParm* \[in\]
</dt> <dd>

Pointer to a [**LSLicense**](lslicense.md) structure that specifies the search parameters to look for.

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

<span id="LSERVER_E_INTERNAL_ERROR"></span><span id="lserver_e_internal_error"></span>

<span id="LSERVER_E_INTERNAL_ERROR"></span><span id="lserver_e_internal_error"></span>**LSERVER\_E\_INTERNAL\_ERROR** (5001)


</dt> <dd>

Internal error in license server.

</dd> <dt>

<span id="LSERVER_E_INVALID_SEQUENCE"></span><span id="lserver_e_invalid_sequence"></span>

<span id="LSERVER_E_INVALID_SEQUENCE"></span><span id="lserver_e_invalid_sequence"></span>**LSERVER\_E\_INVALID\_SEQUENCE** (5006)


</dt> <dd>

The calling sequence was not valid. Most likely, a previous enumeration has not ended.

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

</dd> <dt>

<span id="LSERVER_E_INVALID_DATA"></span><span id="lserver_e_invalid_data"></span>

<span id="LSERVER_E_INVALID_DATA"></span><span id="lserver_e_invalid_data"></span>**LSERVER\_E\_INVALID\_DATA** (5009)


</dt> <dd>

Data in the search parameter is not valid.

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

[**TLSLicenseEnumNext**](tlslicenseenumnext.md)
</dt> <dt>

[**TLSLicenseEnumEnd**](tlslicenseenumend.md)
</dt> </dl>

 

