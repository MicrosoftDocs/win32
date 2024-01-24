---
description: Time stamps the specified subject and optionally returns a pointer to a SIGNER\_CONTEXT structure that contains a pointer to a BLOB. This function can be used to perform X.509 Public Key Infrastructure, RFC 3161&\#8211;compliant, time stamps.
ms.assetid: fb82545b-c00f-44eb-96f4-aa27a125c8d9
title: SignerTimeStampEx2 function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignerTimeStampEx2
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# SignerTimeStampEx2 function

The **SignerTimeStampEx2** function time stamps the specified subject and optionally returns a pointer to a [**SIGNER\_CONTEXT**](signer-context.md) structure that contains a pointer to a [*BLOB*](../secgloss/b-gly.md). This function can be used to perform X.509 Public Key Infrastructure, RFC 3161–compliant, time stamps.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
HRESULT WINAPI SignerTimeStampEx2(
  _Reserved_ DWORD               dwFlags,
  _In_       SIGNER_SUBJECT_INFO *pSubjectInfo,
  _In_       LPCWSTR             pwszHttpTimeStamp,
  _In_       ALG_ID              dwAlgId,
  _In_       PCRYPT_ATTRIBUTES   psRequest,
  _In_       LPVOID              pSipData,
  _Out_      SIGNER_CONTEXT      **ppSignerContext 
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Value that specifies the type of time stamp to generate. This parameter can be one of the following values. The values are mutually exclusive.



| Value                                                                                                                                                                                                          | Meaning                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <span id="SIGNER_TIMESTAMP_AUTHENTICODE"></span><span id="signer_timestamp_authenticode"></span><dl> <dt>**SIGNER\_TIMESTAMP\_AUTHENTICODE**</dt> </dl> | Specifies an Authenticode time stamp.<br/>       |
| <span id="SIGNER_TIMESTAMP_RFC3161"></span><span id="signer_timestamp_rfc3161"></span><dl> <dt>**SIGNER\_TIMESTAMP\_RFC3161**</dt> </dl>                | Specifies an RFC 3161–compliant time stamp.<br/> |



 

</dd> <dt>

*pSubjectInfo* \[in\]
</dt> <dd>

The address of a [**SIGNER\_SUBJECT\_INFO**](signer-subject-info.md) structure that represents the subject to be time stamped.

</dd> <dt>

*pwszHttpTimeStamp* \[in\]
</dt> <dd>

The address of a null-terminated Unicode string that contains the URL of a time stamp server.

</dd> <dt>

*dwAlgId* \[in\]
</dt> <dd>

Specifies a hash algorithm to be used for performing RFC 3161–compliant time stamps. This parameter is ignored for Authenticode time stamps.

</dd> <dt>

*psRequest* \[in\]
</dt> <dd>

Optional. The address of a [**CRYPT\_ATTRIBUTES**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_attributes) structure that contains additional attributes that are added to the time stamp request.

This parameter is optional and can be **NULL** if it is not included.

</dd> <dt>

*pSipData* \[in\]
</dt> <dd>

Optional. A 32-bit value that is passed as additional data to [*subject interface package*](../secgloss/s-gly.md) (SIP) functions. The format and content of this parameter is defined by the SIP provider.

This parameter is optional and can be **NULL** if it is not included.

</dd> <dt>

*ppSignerContext* \[out\]
</dt> <dd>

Optional. The address of a pointer to the [**SIGNER\_CONTEXT**](signer-context.md) structure that contains the signed BLOB. When you have finished using the **SIGNER\_CONTEXT** structure, free it by calling the [**SignerFreeSignerContext**](signerfreesignercontext.md) function.

</dd> </dl>

## Return value

If the function succeeds, the function returns S\_OK.

If the function fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



## See also

<dl> <dt>

[**SignerTimeStamp**](signertimestamp.md)
</dt> <dt>

[**SignerTimeStampEx**](signertimestampex.md)
</dt> </dl>

 

 
