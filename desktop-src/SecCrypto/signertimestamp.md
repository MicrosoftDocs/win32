---
description: Time stamps the specified subject. This function supports Authenticode time stamping. To perform X.509 Public Key Infrastructure (RFC 3161) time stamping, use the SignerTimeStampEx2 function.
ms.assetid: fb2c149b-dba2-4879-be97-831037e1110b
title: SignerTimeStamp function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignerTimeStamp
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# SignerTimeStamp function

The **SignerTimeStamp** function time stamps the specified subject. This function supports Authenticode time stamping. To perform X.509 Public Key Infrastructure (RFC 3161) time stamping, use the [**SignerTimeStampEx2**](signertimestampex2.md) function.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
HRESULT WINAPI SignerTimeStamp(
  _In_     SIGNER_SUBJECT_INFO *pSubjectInfo,
  _In_     LPCWSTR             pwszHttpTimeStamp,
  _In_opt_ PCRYPT_ATTRIBUTES   psRequest,
  _In_opt_ LPVOID              pSipData
);
```



## Parameters

<dl> <dt>

*pSubjectInfo* \[in\]
</dt> <dd>

The address of a [**SIGNER\_SUBJECT\_INFO**](signer-subject-info.md) structure that represents the subject to be time stamped.

</dd> <dt>

*pwszHttpTimeStamp* \[in\]
</dt> <dd>

The address of a null-terminated Unicode string that contains the URL of a time stamp server.

</dd> <dt>

*psRequest* \[in, optional\]
</dt> <dd>

The address of a [**CRYPT\_ATTRIBUTES**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_attributes) structure that contains additional attributes that are added to the time stamp request.

This parameter is optional and can be **NULL** if it is not included.

</dd> <dt>

*pSipData* \[in, optional\]
</dt> <dd>

A 32-bit value that is passed as additional data to SIP functions. The format and content of this is defined by the SIP provider.

This parameter is optional and can be **NULL** if it is not included.

</dd> </dl>

## Return value

If the function succeeds, the function returns S\_OK.

If the function fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 
