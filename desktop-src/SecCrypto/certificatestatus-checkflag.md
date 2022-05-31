---
description: Sets or retrieves the validity check flags for a certificate.
ms.assetid: c80c95a0-8a9b-441d-b243-7ee0552731e4
title: CertificateStatus.CheckFlag property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CertificateStatus.CheckFlag
api_type:
- COM
api_location:
- Capicom.dll
---

# CertificateStatus.CheckFlag property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ChainStatus Structure**](/dotnet/api/system.security.cryptography.x509certificates.x509chainstatus?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **CheckFlag** property sets or retrieves the validity check flags for a certificate.

## Syntax


```VB
CertificateStatus.CheckFlag As CAPICOM_CHECK_FLAG
```



## Property value

A value of the [**CAPICOM\_CHECK\_FLAG**](capicom-check-flag.md) enumeration that describes the validity checks for the certificate. The default value is **CAPICOM\_CHECK\_ONLINE\_ALL**.

**CAPICOM 2.0.0.3/2.0.0.2/2.0.0.1:** The default value is [**CAPICOM\_CHECK\_SIGNATURE\_VALIDITY**](capicom-check-flag.md), [**CAPICOM\_CHECK\_TIME\_VALIDITY**](capicom-check-flag.md), [**CAPICOM\_CHECK\_TRUSTED\_ROOT**](capicom-check-flag.md), and [**CAPICOM\_CHECK\_COMPLETE\_CHAIN**](capicom-check-flag.md).

**CAPICOM 2.0 and earlier:** The default value is [**CAPICOM\_CHECK\_SIGNATURE\_VALIDITY**](capicom-check-flag.md), [**CAPICOM\_CHECK\_TIME\_VALIDITY**](capicom-check-flag.md), and [**CAPICOM\_CHECK\_TRUSTED\_ROOT**](capicom-check-flag.md).

The following table shows the possible values.



| Value                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_CHECK_BASIC_CONSTRAINTS"></span><span id="capicom_check_basic_constraints"></span><dl> <dt>**CAPICOM\_CHECK\_BASIC\_CONSTRAINTS**</dt> </dl>                          | Checks basic constraints. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                    |
| <span id="CAPICOM_CHECK_COMPLETE_CHAIN"></span><span id="capicom_check_complete_chain"></span><dl> <dt>**CAPICOM\_CHECK\_COMPLETE\_CHAIN**</dt> </dl>                                   | Checks the complete chain. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                   |
| <span id="CAPICOM_CHECK_NAME_CONSTRAINTS"></span><span id="capicom_check_name_constraints"></span><dl> <dt>**CAPICOM\_CHECK\_NAME\_CONSTRAINTS**</dt> </dl>                             | Checks name constraints. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                     |
| <span id="CAPICOM_CHECK_NESTED_VALIDITY_PERIOD"></span><span id="capicom_check_nested_validity_period"></span><dl> <dt>**CAPICOM\_CHECK\_NESTED\_VALIDITY\_PERIOD**</dt> </dl>          | Checks nested validity. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                      |
| <span id="CAPICOM_CHECK_NONE"></span><span id="capicom_check_none"></span><dl> <dt>**CAPICOM\_CHECK\_NONE**</dt> </dl>                                                                  | No validity checking is done.<br/>                                                                                                                                                                                                                                                                                                                                                           |
| <span id="CAPICOM_CHECK_OFFLINE_ALL"></span><span id="capicom_check_offline_all"></span><dl> <dt>**CAPICOM\_CHECK\_OFFLINE\_ALL**</dt> </dl>                                            | Checks offline all. Revocation checks are performed on all certificates in the chain except for the root certificate. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                        |
| <span id="CAPICOM_CHECK_ONLINE_ALL"></span><span id="capicom_check_online_all"></span><dl> <dt>**CAPICOM\_CHECK\_ONLINE\_ALL**</dt> </dl>                                               | Checks online all. Revocation checks are performed on all certificates in the chain except for the root certificate. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                         |
| <span id="CAPICOM_CHECK_OFFLINE_REVOCATION_STATUS"></span><span id="capicom_check_offline_revocation_status"></span><dl> <dt>**CAPICOM\_CHECK\_OFFLINE\_REVOCATION\_STATUS**</dt> </dl> | Checks the revocation status of all certificates in the chain using only offline CRLs.<br/>                                                                                                                                                                                                                                                                                                  |
| <span id="CAPICOM_CHECK_ONLINE_REVOCATION_STATUS"></span><span id="capicom_check_online_revocation_status"></span><dl> <dt>**CAPICOM\_CHECK\_ONLINE\_REVOCATION\_STATUS**</dt> </dl>    | Checks the revocation status of all certificates in the chain using CRLs available online. CRLs are downloaded by using the CDP extension in the certificate.<br/> If the CRL has been downloaded and has not expired, CAPICOM uses it and does not go online.<br/> If a CRL has not been downloaded or is out of date, CAPICOM goes online to attempt to download the CRL.<br/> |
| <span id="CAPICOM_CHECK_SIGNATURE_VALIDITY"></span><span id="capicom_check_signature_validity"></span><dl> <dt>**CAPICOM\_CHECK\_SIGNATURE\_VALIDITY**</dt> </dl>                       | Checks for valid signatures on all certificates in the chain.<br/>                                                                                                                                                                                                                                                                                                                           |
| <span id="CAPICOM_CHECK_TIME_VALIDITY"></span><span id="capicom_check_time_validity"></span><dl> <dt>**CAPICOM\_CHECK\_TIME\_VALIDITY**</dt> </dl>                                      | Checks the time validity of all certificates in the chain.<br/>                                                                                                                                                                                                                                                                                                                              |
| <span id="CAPICOM_CHECK_TRUSTED_ROOT"></span><span id="capicom_check_trusted_root"></span><dl> <dt>**CAPICOM\_CHECK\_TRUSTED\_ROOT**</dt> </dl>                                         | Checks for a trusted root of the certificate chain.<br/>                                                                                                                                                                                                                                                                                                                                     |



 

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
