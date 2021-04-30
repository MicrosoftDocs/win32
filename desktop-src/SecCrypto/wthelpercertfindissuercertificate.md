---
description: Finds an issuer certificate from the specified certificate stores that matches the specified subject certificate.
ms.assetid: c724f602-fc73-4857-941f-0f22a9e472d1
title: WTHelperCertFindIssuerCertificate function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WTHelperCertFindIssuerCertificate
api_type: 
- DllExport
api_location: 
- Wintrust.dll
---

# WTHelperCertFindIssuerCertificate function

\[The **WTHelperCertFindIssuerCertificate** function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The **WTHelperCertFindIssuerCertificate** function finds an issuer certificate from the specified certificate stores that matches the specified subject certificate.

> [!Note]  
> This function has no associated import library. You must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Wintrust.dll.

 

## Syntax


```C++
PCCERT_CONTEXT WINAPI WTHelperCertFindIssuerCertificate(
  _In_      PCCERT_CONTEXT pChildContext,
  _In_      DWORD          chStores,
  _In_      HCERTSTORE     *pahStores,
  _In_      FILETIME       *psftVerifyAsOf,
  _In_      DWORD          dwEncoding,
  _Out_opt_ DWORD          *pdwConfidence,
  _Out_     DWORD          *dwError
);
```



## Parameters

<dl> <dt>

*pChildContext* \[in\]
</dt> <dd>

The subject certificate for which to find a matching issuer certificate.

</dd> <dt>

*chStores* \[in\]
</dt> <dd>

The number of elements in the *pahStores* array.

</dd> <dt>

*pahStores* \[in\]
</dt> <dd>

An array of certificate stores in which to search.

</dd> <dt>

*psftVerifyAsOf* \[in\]
</dt> <dd>

The time of verification.

</dd> <dt>

*dwEncoding* \[in\]
</dt> <dd>

A **DWORD** value that specifies the encoding types of the certificate to check. For information about possible encoding types, see [Certificate and Message Encoding Types](certificate-and-message-encoding-types.md).

</dd> <dt>

*pdwConfidence* \[out, optional\]
</dt> <dd>

This parameter can be a bitwise combination of zero or more of the following confidence values.



| Value                                                                                                                                                                                                                                                                 | Meaning                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <span id="CERT_CONFIDENCE_SIG"></span><span id="cert_confidence_sig"></span><dl> <dt>**CERT\_CONFIDENCE\_SIG**</dt> <dt> 0x10000000</dt> </dl>                     | The signature of the certificate is valid.<br/>                                           |
| <span id="CERT_CONFIDENCE_TIME"></span><span id="cert_confidence_time"></span><dl> <dt>**CERT\_CONFIDENCE\_TIME**</dt> <dt> 0x01000000</dt> </dl>                  | The time of the certificate issuer is valid.<br/>                                         |
| <span id="_CERT_CONFIDENCE_TIMENEST"></span><span id="_cert_confidence_timenest"></span><dl> <dt> **CERT\_CONFIDENCE\_TIMENEST**</dt> <dt>0x00100000</dt> </dl>    | The time of the certificate is valid.<br/>                                                |
| <span id="_CERT_CONFIDENCE_AUTHIDEXT"></span><span id="_cert_confidence_authidext"></span><dl> <dt> **CERT\_CONFIDENCE\_AUTHIDEXT**</dt> <dt>0x00010000</dt> </dl> | The authority ID extension is valid.<br/>                                                 |
| <span id="_CERT_CONFIDENCE_HYGIENE"></span><span id="_cert_confidence_hygiene"></span><dl> <dt> **CERT\_CONFIDENCE\_HYGIENE**</dt> <dt>0x00001000</dt> </dl>       | At a minimum, the signature of the certificate and authority ID extension are valid.<br/> |
| <span id="_CERT_CONFIDENCE_HIGHEST"></span><span id="_cert_confidence_highest"></span><dl> <dt> **CERT\_CONFIDENCE\_HIGHEST**</dt> <dt>0x11111000</dt> </dl>       | A combination of all of the other confidence values.<br/>                                 |



 

</dd> <dt>

*dwError* \[out\]
</dt> <dd>

A pointer to a **DWORD** variable that contains the error value for this certificate, if applicable.

</dd> </dl>

## Return value

An issuer certificate that matches the subject certificate specified by the *pChildContext* parameter.

## Remarks

To successfully find a matching issuer certificate, the following requirements must be met:

-   The signature of the subject certificate specified by the *pChildContext* parameter must be valid.
-   The **rgExtension** member of the **pCertInfo** member of the *pChildContext* parameter must contain a [**CERT\_AUTHORITY\_KEY\_ID\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_authority_key_id_info) structure. The **CertIssuer** and **CertSerialMember** members of this structure much match the corresponding members for the issuer certificate.
-   The value of the *psftVerifyAsOf* parameter must be within the period of validity of the subject certificate.
-   The period of validity of the subject certificate must be within the period of validity of the issuer certificate.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Wintrust.dll</dt> </dl> |



 

 
