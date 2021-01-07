---
description: Time stamps the specified subject and supports setting time stamps on multiple signatures.
ms.assetid: A290ED4F-8803-4EAA-8CE1-68879F7F754A
title: SignerTimeStampEx3 function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignerTimeStampEx3
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# SignerTimeStampEx3 function

The **SignerTimeStampEx3** function time stamps the specified subject and supports setting time stamps on multiple signatures.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
HRESULT WINAPI SignerTimeStampEx3(
  _In_       DWORD                  dwFlags,
  _In_       DWORD                  dwIndex,
  _In_       SIGNER_SUBJECT_INFO    *pSubjectInfo,
  _In_       PCWSTR                 pwszHttpTimeStamp,
  _In_       PCWSTR                 pszAlgorithmOid,
  _In_opt_   PCRYPT_ATTRIBUTES      psRequest,
  _In_opt_   PVOID                  pSipData,
  _Out_      SIGNER_CONTEXT         **ppSignerContext,
  _In_opt_   PCERT_STRONG_SIGN_PARA pCryptoPolicy,
  _Reserved_ PVOID                  pReserved
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flag that specifies the type of time stamp to generate. This parameter can be one of the following values. The values are mutually exclusive.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="SIGNER_TIMESTAMP_AUTHENTICODE"></span><span id="signer_timestamp_authenticode"></span><dl> <dt><strong>SIGNER_TIMESTAMP_AUTHENTICODE</strong></dt> </dl></td>
<td>Specifies an Authenticode time stamp.<br/>
<blockquote>
[!Note]<br />
Authenticode is no longer the preferred type of time stamp. Support for Authenticode time stamps may be removed in the future. We recommend that you use RFC 3161 instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><span id="SIGNER_TIMESTAMP_RFC3161"></span><span id="signer_timestamp_rfc3161"></span><dl> <dt><strong>SIGNER_TIMESTAMP_RFC3161</strong></dt> </dl></td>
<td>Specifies an RFC 3161–compliant time stamp.<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

*dwIndex* \[in\]
</dt> <dd>

Specifies the sequence number of the signature to which the timestamp will be added. If this value is zero (0), the outer signature will be time stamped.

</dd> <dt>

*pSubjectInfo* \[in\]
</dt> <dd>

The address of a [**SIGNER\_SUBJECT\_INFO**](signer-subject-info.md) structure that represents the subject to be time stamped.

</dd> <dt>

*pwszHttpTimeStamp* \[in\]
</dt> <dd>

The address of a null-terminated Unicode string that contains the URL of a time stamp server.

</dd> <dt>

*pszAlgorithmOid* \[in\]
</dt> <dd>

A hash algorithm to be used for performing RFC 3161–compliant time stamps. This parameter is ignored for Authenticode time stamps.

</dd> <dt>

*psRequest* \[in, optional\]
</dt> <dd>

Optional. The address of a [**CRYPT\_ATTRIBUTES**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_attributes) structure that contains additional attributes that are added to the time stamp request.

This parameter is optional and can be **NULL** if it is not included.

</dd> <dt>

*pSipData* \[in, optional\]
</dt> <dd>

Optional. A 32-bit value that is passed as additional data to [*subject interface package*](../secgloss/s-gly.md) (SIP) functions. The format and content of this parameter is defined by the SIP provider.

This parameter is optional and can be **NULL** if it is not included.

</dd> <dt>

*ppSignerContext* \[out\]
</dt> <dd>

Optional. The address of a pointer to the [**SIGNER\_CONTEXT**](signer-context.md) structure that contains the signed BLOB. When you have finished using the **SIGNER\_CONTEXT** structure, free it by calling the [**SignerFreeSignerContext**](signerfreesignercontext.md) function.

</dd> <dt>

*pCryptoPolicy* \[in, optional\]
</dt> <dd>

If present, a pointer to a [**CERT\_STRONG\_SIGN\_PARA**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_strong_sign_para) structure that contains the parameters used to check for strong signatures. The time stamp must pass this cryptographic policy.

</dd> <dt>

*pReserved* 
</dt> <dd>

Reserved. This value must be **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the function returns S\_OK.

If the function fails, it returns an **HRESULT** value that indicates the error. Possible error codes returned by this function include, but are not limited to, the following. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>E_INVALIDARG</strong></dt> </dl></td>
<td>This error can be returned for the following conditions:<br/>
<ul>
<li>You must set either <strong>SIGNER_TIMESTAMP_AUTHENTICODE</strong> or <strong>SIGNER_TIMESTAMP_RFC3161</strong> for the <em>dwFlags</em> parameter.</li>
<li>The <em>pReserved</em> parameter must be <strong>NULL</strong>.</li>
<li>If you set the <strong>SIGNER_TIMESTAMP_AUTHENTICODE</strong> flag in the <em>dwFlags</em> parameter, you must set the <em>dwIndex</em> parameter to zero.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



## See also

<dl> <dt>

[**SignerTimeStamp**](signertimestamp.md)
</dt> <dt>

[**SignerTimeStampEx**](signertimestampex.md)
</dt> <dt>

[**SignerTimeStampEx2**](signertimestampex2.md)
</dt> </dl>

 

 
