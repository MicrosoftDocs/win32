---
description: Signs the specified file and returns a pointer to the signed data.
ms.assetid: 9921ffae-2299-4bf2-b76d-77f7f6afb663
title: SignerSignEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignerSignEx
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# SignerSignEx function

The **SignerSignEx** function signs the specified file and returns a pointer to the signed data.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
HRESULT WINAPI SignerSignEx(
  _In_     DWORD                 dwFlags,
  _In_     SIGNER_SUBJECT_INFO   *pSubjectInfo,
  _In_     SIGNER_CERT           *pSignerCert,
  _In_     SIGNER_SIGNATURE_INFO *pSignatureInfo,
  _In_opt_ SIGNER_PROVIDER_INFO  *pProviderInfo,
  _In_opt_ LPCWSTR               pwszHttpTimeStamp,
  _In_opt_ PCRYPT_ATTRIBUTES     psRequest,
  _In_opt_ LPVOID                pSipData,
  _Out_    SIGNER_CONTEXT        **ppSignerContext
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Modifies the behavior of this function.

If the file to be signed is a portable executable (PE) file, this can be zero or a combination of one or more of the following values. These identifiers are defined in Mssip.h.



| Value                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SPC_EXC_PE_PAGE_HASHES_FLAG"></span><span id="spc_exc_pe_page_hashes_flag"></span><dl> <dt>**SPC\_EXC\_PE\_PAGE\_HASHES\_FLAG**</dt> <dt>0x10</dt> </dl>                    | Exclude page hashes when creating SIP indirect data for the PE file. This flag takes precedence over the **SPC\_INC\_PE\_PAGE\_HASHES\_FLAG** flag.<br/> If neither the **SPC\_EXC\_PE\_PAGE\_HASHES\_FLAG** or the **SPC\_INC\_PE\_PAGE\_HASHES\_FLAG** flag is specified, the value set with the [**WintrustSetDefaultIncludePEPageHashes**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustsetdefaultincludepepagehashes) function is used for this setting. The default for this setting is to exclude page hashes when creating SIP indirect data for PE files.<br/> **Windows Server 2003 and Windows XP:** This value is not supported.<br/> |
| <span id="SPC_INC_PE_IMPORT_ADDR_TABLE_FLAG"></span><span id="spc_inc_pe_import_addr_table_flag"></span><dl> <dt>**SPC\_INC\_PE\_IMPORT\_ADDR\_TABLE\_FLAG**</dt> <dt>0x20</dt> </dl> | This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="SPC_INC_PE_DEBUG_INFO_FLAG"></span><span id="spc_inc_pe_debug_info_flag"></span><dl> <dt>**SPC\_INC\_PE\_DEBUG\_INFO\_FLAG**</dt> <dt>0x40</dt> </dl>                       | This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="SPC_INC_PE_RESOURCES_FLAG"></span><span id="spc_inc_pe_resources_flag"></span><dl> <dt>**SPC\_INC\_PE\_RESOURCES\_FLAG**</dt> <dt>0x80</dt> </dl>                           | This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="SPC_INC_PE_PAGE_HASHES_FLAG"></span><span id="spc_inc_pe_page_hashes_flag"></span><dl> <dt>**SPC\_INC\_PE\_PAGE\_HASHES\_FLAG**</dt> <dt>0x100</dt> </dl>                   | Include page hashes when creating SIP indirect data for the PE file.<br/> **Windows Server 2003 and Windows XP:** This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

</dd> <dt>

*pSubjectInfo* \[in\]
</dt> <dd>

A pointer to a [**SIGNER\_SUBJECT\_INFO**](signer-subject-info.md) structure that specifies the subject to sign.

</dd> <dt>

*pSignerCert* \[in\]
</dt> <dd>

A pointer to a [**SIGNER\_CERT**](signer-cert.md) structure that specifies the certificate to use to create the digital signature.

</dd> <dt>

*pSignatureInfo* \[in\]
</dt> <dd>

A pointer to a [**SIGNER\_SIGNATURE\_INFO**](signer-signature-info.md) structure that contains information about the digital signature.

</dd> <dt>

*pProviderInfo* \[in, optional\]
</dt> <dd>

A pointer to a [**SIGNER\_PROVIDER\_INFO**](signer-provider-info.md) structure that specifies the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) and private key information used to create the digital signature.

If the value of this parameter is **NULL**, the value of the *pSignerCert* parameter must specify a certificate that is associated with a CSP.

</dd> <dt>

*pwszHttpTimeStamp* \[in, optional\]
</dt> <dd>

The URL of a time stamp server.

</dd> <dt>

*psRequest* \[in, optional\]
</dt> <dd>

A pointer to an array of [**CRYPT\_ATTRIBUTE**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_attribute) structures that are added to a sign request. This parameter is ignored if the *pwszHttpTimeStamp* parameter does not contain a valid value that is not **NULL**.

</dd> <dt>

*pSipData* \[in, optional\]
</dt> <dd>

A 32-bit value that is passed as additional data to SIP functions. The format and content of this is defined by the SIP provider.

</dd> <dt>

*ppSignerContext* \[out\]
</dt> <dd>

The address of a pointer to the [**SIGNER\_CONTEXT**](signer-context.md) structure that contains the signed [*BLOB*](../secgloss/b-gly.md). When you have finished using the **SIGNER\_CONTEXT** structure, free the **SIGNER\_CONTEXT** structure by calling the [**SignerFreeSignerContext**](signerfreesignercontext.md) function.

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



## See also

<dl> <dt>

[**SignerSign**](signersign.md)
</dt> <dt>

[**SignerFreeSignerContext**](signerfreesignercontext.md)
</dt> </dl>

 

 
