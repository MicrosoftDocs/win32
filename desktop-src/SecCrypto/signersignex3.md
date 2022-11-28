---
description: Signs and time stamps the specified file to allow multiple nested signatures.
ms.assetid: b400f937-fbef-4350-b024-43bb3cc063de
title: SignerSignEx3 function
ms.topic: reference
ms.date: 11/15/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignerSignEx3
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# SignerSignEx3 function

The **SignerSignEx3** function signs and time stamps the specified file, allowing multiple nested signatures.

> [!NOTE]
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

## Syntax

```C++
HRESULT WINAPI SignerSignEx3(
  _In_       DWORD                  dwFlags,
  _In_       SIGNER_SUBJECT_INFO    *pSubjectInfo,
  _In_       SIGNER_CERT            *pSignerCert,
  _In_       SIGNER_SIGNATURE_INFO  *pSignatureInfo,
  _In_opt_   SIGNER_PROVIDER_INFO   *pProviderInfo,
  _In_opt_   DWORD                  dwTimestampFlags,
  _In_opt_   PCSTR                  pszTimestampAlgorithmOid,
  _In_opt_   PCWSTR                 pwszHttpTimeStamp,
  _In_opt_   PCRYPT_ATTRIBUTES      psRequest,
  _In_opt_   PVOID                  pSipData,
  _Out_      SIGNER_CONTEXT         **ppSignerContext,
  _In_opt_   PCERT_STRONG_SIGN_PARA pCryptoPolicy,
  _In_opt_   SIGNER_DIGEST_SIGN_INFO  *pDigestSignInfo,
  _Reserved_ PVOID                  pReserved
);
```

## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Modifies the behavior of this function.

If the file to be signed is a portable executable (PE) file, this can be zero or a combination of one or more of the following values.

| Value                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SPC_EXC_PE_PAGE_HASHES_FLAG"></span><span id="spc_exc_pe_page_hashes_flag"></span><dl> <dt>**SPC\_EXC\_PE\_PAGE\_HASHES\_FLAG**</dt> <dt>0x10</dt> </dl>                    | Exclude page hashes when creating SIP indirect data for the PE file. This flag takes precedence over the **SPC\_INC\_PE\_PAGE\_HASHES\_FLAG** flag.<br/> If neither the **SPC\_EXC\_PE\_PAGE\_HASHES\_FLAG** or the **SPC\_INC\_PE\_PAGE\_HASHES\_FLAG** flag is specified, the value set with the [**WintrustSetDefaultIncludePEPageHashes**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustsetdefaultincludepepagehashes) function is used for this setting. The default for this setting is to exclude page hashes when creating SIP indirect data for PE files.<br/> This value is defined in the Mssip.h header file.<br/> **Windows Server 2003 and Windows XP:** This value is not supported.<br/> |
| <span id="SPC_INC_PE_IMPORT_ADDR_TABLE_FLAG"></span><span id="spc_inc_pe_import_addr_table_flag"></span><dl> <dt>**SPC\_INC\_PE\_IMPORT\_ADDR\_TABLE\_FLAG**</dt> <dt>0x20</dt> </dl> | This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="SPC_INC_PE_DEBUG_INFO_FLAG"></span><span id="spc_inc_pe_debug_info_flag"></span><dl> <dt>**SPC\_INC\_PE\_DEBUG\_INFO\_FLAG**</dt> <dt>0x40</dt> </dl>                       | This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="SPC_INC_PE_RESOURCES_FLAG"></span><span id="spc_inc_pe_resources_flag"></span><dl> <dt>**SPC\_INC\_PE\_RESOURCES\_FLAG**</dt> <dt>0x80</dt> </dl>                           | This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="SPC_INC_PE_PAGE_HASHES_FLAG"></span><span id="spc_inc_pe_page_hashes_flag"></span><dl> <dt>**SPC\_INC\_PE\_PAGE\_HASHES\_FLAG**</dt> <dt>0x100</dt> </dl>                   | Include page hashes when creating SIP indirect data for the PE file.<br/> **Windows Server 2003 and Windows XP:** This value is not supported.<br/> This value is defined in the Mssip.h header file.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="SPC_DIGEST_SIGN_FLAG"></span><span id="spc_digest_sign_flag"></span><dl> <dt>**SPC\_DIGEST\_SIGN\_FLAG**</dt> <dt>0x800</dt> </dl>                                          | Digest signing will be done.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="SIG_APPEND"></span><span id="sig_append"></span><dl> <dt>**SIG\_APPEND**</dt> <dt>0x1000</dt> </dl>                                                                         | The signature will be nested. If you set this flag before any signature has been added, the generated signature will be added as the outer signature. If you do not set this flag, the generated signature replaces the outer signature, deleting all inner signatures.<br/>                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="SPC_DIGEST_SIGN_EX_FLAG"></span><span id="spc_digest_sign_ex_flag"></span><dl> <dt>**SPC\_DIGEST\_SIGN\_EX\_FLAG**</dt> <dt>0x4000</dt> </dl>                                 | Digest signing will be done. The caller’s digest signing function will select and return the code signing certificate which performed the signing operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

</dd> <dt>

*pSubjectInfo* \[in\]
</dt> <dd>

Pointer to a [**SIGNER\_SUBJECT\_INFO**](signer-subject-info.md) structure that specifies the subject to sign.

</dd> <dt>

*pSignerCert* \[in\]
</dt> <dd>

Pointer to a [**SIGNER\_CERT**](signer-cert.md) structure that specifies the certificate to use to create the digital signature.

</dd> <dt>

*pSignatureInfo* \[in\]
</dt> <dd>

A pointer to a [**SIGNER\_SIGNATURE\_INFO**](signer-signature-info.md) structure that contains information about the digital signature.

</dd> <dt>

*pProviderInfo* \[in, optional\]
</dt> <dd>

Pointer to a [**SIGNER\_PROVIDER\_INFO**](signer-provider-info.md) structure that specifies the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) and private key information used to create the digital signature.

If the value of this parameter is **NULL**, the *pSignerCert* parameter must specify a certificate that is associated with a CSP.

</dd> <dt>

*dwTimestampFlags* \[in, optional\]
</dt> <dd>

Flags that will be passed to [**SignerTimeStampEx3**](signertimestampex3.md) if the *pwszHttpTimeStamp* parameter is not **NULL**. This can be one of the following values.

| Value                                                                                                                                                                                                          | Meaning                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="SIGNER_TIMESTAMP_AUTHENTICODE"></span><span id="signer_timestamp_authenticode"></span><dl> <dt>**SIGNER\_TIMESTAMP\_AUTHENTICODE**</dt> </dl> | Default value. Specifies an Authenticode timestamp.<br/> |
| <span id="SIGNER_TIMESTAMP_RFC3161"></span><span id="signer_timestamp_rfc3161"></span><dl> <dt>**SIGNER\_TIMESTAMP\_RFC3161**</dt> </dl>                | Specifies an RFC 3161 timestamp.<br/>                    |

This parameter is ignored if the *pwszHttpTimeStamp* parameter is **NULL**.

</dd> <dt>

*pszTimestampAlgorithmOid* \[in, optional\]
</dt> <dd>

Object identifier of the algorithm to be used for creating an RFC 3161 timestamp. This parameter is ignored for Authenticode time stamps.

</dd> <dt>

*pwszHttpTimeStamp* \[in, optional\]
</dt> <dd>

URL of the time stamp server.

</dd> <dt>

*psRequest* \[in, optional\]
</dt> <dd>

Pointer to an array of [**CRYPT\_ATTRIBUTE**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_attribute) structures that are added to a sign request. This parameter is ignored if the *pwszHttpTimeStamp* parameter does not contain a valid value or is **NULL**.

</dd> <dt>

*pSipData* \[in, optional\]
</dt> <dd>

A 32-bit value that is passed as additional data to SIP functions. The format and content of this is defined by the SIP provider.

</dd> <dt>

*ppSignerContext* \[out\]
</dt> <dd>

The address of a pointer to the [**SIGNER\_CONTEXT**](signer-context.md) structure that contains the signed [*BLOB*](../secgloss/b-gly.md). When you have finished using the **SIGNER\_CONTEXT** structure, free the **SIGNER\_CONTEXT** structure by calling the [**SignerFreeSignerContext**](signerfreesignercontext.md) function.

</dd> <dt>

*pCryptoPolicy* \[in, optional\]
</dt> <dd>

If present, a pointer to a [**CERT\_STRONG\_SIGN\_PARA**](/windows/win32/api/Wincrypt/ns-wincrypt-cert_strong_sign_para) structure that contains the parameters used to check for strong signatures. If either a certificate or its chain does not pass, the file is not altered in any way. If a URL is passed in to specify a Time Stamping Authority (TSA), this policy is also applied to the time stamp.

</dd> <dt>

*pDigestSignInfo* \[in, optional\]
 </dt> <dd>

 If present, a pointer to a [**SIGNER\_DIGEST\_SIGN\_INFO**](signer-digest-sign-info.md) structure that contains information regarding digest signing.

 </dd> <dt>

*pReserved*
</dt> <dd>

Reserved. This value must be **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the function returns S\_OK.

If the function fails, it returns an **HRESULT** value that indicates the error. Possible error codes returned by this function include, but are not limited to, the following. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

| Return code                                                                                  | Description                                                                                                                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | If you set the *dwTimestampFlags* parameter to **SIGNER\_TIMESTAMP\_AUTHENTICODE**, you cannot set the *dwFlags* parameter to **SIG\_APPEND**.<br/> |

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |

## See also

<dl> <dt>

[**SignerSign**](signersign.md)
</dt> <dt>

[**SignerSignEx**](signersignex.md)
</dt> <dt>

[**SignerFreeSignerContext**](signerfreesignercontext.md)
</dt> <dt>

[**SIGNER\_DIGEST\_SIGN\_INFO**](signer-digest-sign-info.md)
</dt> </dl>
