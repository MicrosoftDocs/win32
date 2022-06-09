---
description: Retrieves information from the certificate.
ms.assetid: 57f1c6f9-f06d-4ac7-9070-2a2e6afe93d2
title: ICertificate2::GetInfo method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate.GetInfo
- ICertificate2.GetInfo
- ICertificate.GetInfo
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificate2::GetInfo method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](/previous-versions/windows/embedded/hh424017(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **GetInfo** method retrieves information from the [*certificate*](../secgloss/c-gly.md).

## Syntax


```VB
Certificate.GetInfo( _
  ByVal InfoType _
)
```



## Parameters

<dl> <dt>

*InfoType* \[in\]
</dt> <dd>

A value of the [**CAPICOM\_CERT\_INFO\_TYPE**](capicom-cert-info-type.md) enumeration that specifies what type of data is retrieved from the certificate. The following table shows the possible values.



| Value                                                                                                                                                                                                                                     | Meaning                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="CAPICOM_CERT_INFO_SUBJECT_SIMPLE_NAME"></span><span id="capicom_cert_info_subject_simple_name"></span><dl> <dt>**CAPICOM\_CERT\_INFO\_SUBJECT\_SIMPLE\_NAME**</dt> </dl> | Returns the display name from the certificate subject.<br/>                            |
| <span id="CAPICOM_CERT_INFO_ISSUER_SIMPLE_NAME"></span><span id="capicom_cert_info_issuer_simple_name"></span><dl> <dt>**CAPICOM\_CERT\_INFO\_ISSUER\_SIMPLE\_NAME**</dt> </dl>    | Returns the display name of the issuer of the certificate.<br/>                        |
| <span id="CAPICOM_CERT_INFO_SUBJECT_EMAIL_NAME"></span><span id="capicom_cert_info_subject_email_name"></span><dl> <dt>**CAPICOM\_CERT\_INFO\_SUBJECT\_EMAIL\_NAME**</dt> </dl>    | Returns the email address of the certificate subject.<br/>                             |
| <span id="CAPICOM_CERT_INFO_ISSUER_EMAIL_NAME"></span><span id="capicom_cert_info_issuer_email_name"></span><dl> <dt>**CAPICOM\_CERT\_INFO\_ISSUER\_EMAIL\_NAME**</dt> </dl>       | Returns the email address of the issuer of the certificate.<br/>                       |
| <span id="CAPICOM_CERT_INFO_SUBJECT_UPN"></span><span id="capicom_cert_info_subject_upn"></span><dl> <dt>**CAPICOM\_CERT\_INFO\_SUBJECT\_UPN**</dt> </dl>                          | Returns the UPN of the certificate subject. Introduced in CAPICOM 2.0.<br/>            |
| <span id="CAPICOM_CERT_INFO_ISSUER_UPN"></span><span id="capicom_cert_info_issuer_upn"></span><dl> <dt>**CAPICOM\_CERT\_INFO\_ISSUER\_UPN**</dt> </dl>                             | Returns the UPN of the issuer of the certificate. Introduced in CAPICOM 2.0.<br/>      |
| <span id="CAPICOM_CERT_INFO_SUBJECT_DNS_NAME"></span><span id="capicom_cert_info_subject_dns_name"></span><dl> <dt>**CAPICOM\_CERT\_INFO\_SUBJECT\_DNS\_NAME**</dt> </dl>          | Returns the DNS name of the certificate subject. Introduced in CAPICOM 2.0.<br/>       |
| <span id="CAPICOM_CERT_INFO_ISSUER_DNS_NAME"></span><span id="capicom_cert_info_issuer_dns_name"></span><dl> <dt>**CAPICOM\_CERT\_INFO\_ISSUER\_DNS\_NAME**</dt> </dl>             | Returns the DNS name of the issuer of the certificate. Introduced in CAPICOM 2.0.<br/> |



 

</dd> </dl>

## Return value

A string that contains the requested information.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[Cryptography Objects](cryptography-objects.md)
</dt> <dt>

[**Certificate**](certificate.md)
</dt> </dl>

 

 
