---
description: Returns a Certificates object that contains all certificates that match the specified search criteria.
ms.assetid: a2b8f4d4-dce3-467b-aaa0-a125056a1dd3
title: ICertificates2::Find method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificates.Find
- ICertificates2.Find
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificates2::Find method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2collection) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **Find** method returns a [**Certificates**](certificates.md) object that contains all certificates that match the specified search criteria. This method was introduced in CAPICOM 2.0.

## Syntax


```VB
Certificates.Find( _
  ByVal FindType, _
  [ ByVal varCriteria ], _
  [ ByVal bFindValidOnly ] _
)
```



## Parameters

<dl> <dt>

*FindType* \[in\]
</dt> <dd>

A value of the [**CAPICOM\_CERTIFICATE\_FIND\_TYPE**](capicom-certificate-find-type.md) enumeration that specifies the type of matching criteria supplied in the *varCriteria* parameter. The following table shows the possible values.



| Value                                                                                                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_CERTIFICATE_FIND_SHA1_HASH"></span><span id="capicom_certificate_find_sha1_hash"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_SHA1\_HASH**</dt> </dl>                              | Returns certificates with a SHA1 hash that matches the SHA1 hash specified in the *varCriteria* parameter.<br/>                                                                                                                              |
| <span id="CAPICOM_CERTIFICATE_FIND_SUBJECT_NAME"></span><span id="capicom_certificate_find_subject_name"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_SUBJECT\_NAME**</dt> </dl>                     | Returns certificates whose subject name exactly or partially matches the subject name specified in the *varCriteria* parameter. This call searches the subject name field only.<br/>                                                         |
| <span id="CAPICOM_CERTIFICATE_FIND_ISSUER_NAME"></span><span id="capicom_certificate_find_issuer_name"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_ISSUER\_NAME**</dt> </dl>                        | Returns certificates whose issuer name exactly or partially matches the issuer name specified in the *varCriteria* parameter. This call searches the issuer name field only.<br/>                                                            |
| <span id="CAPICOM_CERTIFICATE_FIND_ROOT_NAME"></span><span id="capicom_certificate_find_root_name"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_ROOT\_NAME**</dt> </dl>                              | Returns certificates whose root subject name exactly or partially matches the root subject name specified in the *varCriteria* parameter. This call creates a chain. This call searches the subject name field of the root certificate.<br/> |
| <span id="CAPICOM_CERTIFICATE_FIND_TEMPLATE_NAME"></span><span id="capicom_certificate_find_template_name"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_TEMPLATE\_NAME**</dt> </dl>                  | Returns certificates whose template name matches the template name specified in the *varCriteria* parameter.<br/>                                                                                                                            |
| <span id="CAPICOM_CERTIFICATE_FIND_EXTENSION"></span><span id="capicom_certificate_find_extension"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_EXTENSION**</dt> </dl>                               | Returns certificates that have an extension that matches the extension specified in the *varCriteria* parameter.<br/>                                                                                                                        |
| <span id="CAPICOM_CERTIFICATE_FIND_EXTENDED_PROPERTY"></span><span id="capicom_certificate_find_extended_property"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_EXTENDED\_PROPERTY**</dt> </dl>      | Returns certificates in the store that explicitly contain an extended property with the value specified in the *varCriteria* parameter.<br/>                                                                                                 |
| <span id="CAPICOM_CERTIFICATE_FIND_APPLICATION_POLICY"></span><span id="capicom_certificate_find_application_policy"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_APPLICATION\_POLICY**</dt> </dl>   | Returns certificates in the store that have either an enhanced key usage extension, application policy extension, or extended property specified in the *varCriteria* parameter.<br/>                                                        |
| <span id="CAPICOM_CERTIFICATE_FIND_CERTIFICATE_POLICY"></span><span id="capicom_certificate_find_certificate_policy"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_CERTIFICATE\_POLICY**</dt> </dl>   | Returns certificates that contain the policy OID in the Certificate Policy extension specified in the *varCriteria* parameter.<br/>                                                                                                          |
| <span id="CAPICOM_CERTIFICATE_FIND_TIME_VALID"></span><span id="capicom_certificate_find_time_valid"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_TIME\_VALID**</dt> </dl>                           | Returns certificates whose time is valid.<br/>                                                                                                                                                                                               |
| <span id="CAPICOM_CERTIFICATE_FIND_TIME_NOT_YET_VALID"></span><span id="capicom_certificate_find_time_not_yet_valid"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_TIME\_NOT\_YET\_VALID**</dt> </dl> | Returns certificates whose time is not yet valid.<br/>                                                                                                                                                                                       |
| <span id="CAPICOM_CERTIFICATE_FIND_TIME_EXPIRED"></span><span id="capicom_certificate_find_time_expired"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_TIME\_EXPIRED**</dt> </dl>                     | Returns certificates whose time has expired.<br/>                                                                                                                                                                                            |
| <span id="CAPICOM_CERTIFICATE_FIND_KEY_USAGE"></span><span id="capicom_certificate_find_key_usage"></span><dl> <dt>**CAPICOM\_CERTIFICATE\_FIND\_KEY\_USAGE**</dt> </dl>                              | Returns certificates containing key usages in the KeyUsage extension specified in the *varCriteria* parameter. If the KeyUsage extension is not present, all of the key usages are assumed to be unavailable.<br/>                           |



 

</dd> <dt>

*varCriteria* \[in, optional\]
</dt> <dd>

A variant that contains the search criteria. This data must match the type of data specified in the *FindType* parameter. If the value of the *FindType* parameter is CAPICOM\_CERTIFICATE\_FIND\_TIME\_VALID, CAPICOM\_CERTIFICATE\_FIND\_TIME\_NOT\_YET\_VALID, or CAPICOM\_CERTIFICATE\_FIND\_TIME\_EXPIRED and you do not pass a value into this parameter, the current time is assumed. For examples of each data type, see Remarks. The default value is 0.

</dd> <dt>

*bFindValidOnly* \[in, optional\]
</dt> <dd>

A Boolean value that indicates whether only valid certificates are returned. The default value is false; this indicates that all certificates that match the search criteria are returned.

If true, the search will not return the following types of certificates:

-   Certificates whose time has expired or is not yet valid.
-   Certificates not chained properly.
-   Certificates that have signature problems.
-   Certificates that are revoked.

</dd> </dl>

## Return value

[**Certificates**](certificates.md) object that contains the results of the search.

**CAPICOM 2.1:** The [**Certificates**](certificates.md) object that is returned contains references to the certificates in the collection in which the search was done. Any changes made to the certificates in the returned **Certificates** object are reflected in that collection.

**CAPICOM 2.0, CAPICOM 2.0.0.1, CAPICOM 2.0.0.2, and CAPICOM 2.0.0.3:** The [**Certificates**](certificates.md) object that is returned contains copies of the certificates in the collection in which the search was done. Any changes made to the certificates in the returned **Certificates** object are not reflected in that collection.

## Remarks

The following examples show possible search criteria for the different search criteria types.



| *FindType* parameter                              | *varCriteria* parameter                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| CAPICOM\_CERTIFICATE\_FIND\_SHA1\_HASH            | 33F362434B577F844BB7226BE36F7D72EF9D9393                                                                                           |
| CAPICOM\_CERTIFICATE\_FIND\_SUBJECT\_NAME         | "NameOfPerson"                                                                                                                     |
| CAPICOM\_CERTIFICATE\_FIND\_ISSUER\_NAME          | "VeriSign"                                                                                                                         |
| CAPICOM\_CERTIFICATE\_FIND\_ROOT\_NAME            | "Microsoft Root Authority"                                                                                                         |
| CAPICOM\_CERTIFICATE\_FIND\_TEMPLATE\_NAME        | "AutoEnrollEFS"<br/> 1.3.6.1.4.1.311.21.8.3692315854.1256661383.1690418588.4201632533.1741915387.2177932052<br/>       |
| CAPICOM\_CERTIFICATE\_FIND\_EXTENSION             | "2.5.29.31"<br/> CAPICOM\_OID\_KEY\_USAGE\_EXTENSION<br/> "CRL Distribution List"<br/>                           |
| CAPICOM\_CERTIFICATE\_FIND\_EXTENDED\_PROPERTY    | CAPICOM\_PROPID\_KEY\_PROV\_INFO                                                                                                   |
| CAPICOM\_CERTIFICATE\_FIND\_APPLICATION\_POLICY   | "1.3.6.1.5.5.7.3.3"<br/> "1.3.6.1.5.5.7.3.4"<br/> CAPICOM\_OID\_SERVER\_AUTH\_EKU<br/> "Code Signing"<br/> |
| CAPICOM\_CERTIFICATE\_FIND\_CERTIFICATE\_POLICY   | "1.3.6.1.5.5.7.3.4.3.5"<br/> "Corporate High Assurance"<br/>                                                           |
| CAPICOM\_CERTIFICATE\_FIND\_TIME\_VALID           | \#04/15/2002, 6:00 PM\#                                                                                                            |
| CAPICOM\_CERTIFICATE\_FIND\_TIME\_NOT\_YET\_VALID | \#04/15/2002, 6:00 PM\#                                                                                                            |
| CAPICOM\_CERTIFICATE\_FIND\_TIME\_EXPIRED         | \#04/15/2002, 6:00 PM\#                                                                                                            |
| CAPICOM\_CERTIFICATE\_FIND\_KEY\_USAGE            | CAPICOM\_ENCIPHER\_ONLY\_KEY\_USAGE                                                                                                |



 

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Certificates**](certificates.md)
</dt> <dt>

[**CAPICOM\_OID**](capicom-oid.md)
</dt> </dl>

 

 
