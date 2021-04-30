---
description: Removes an extended property from the collection.
ms.assetid: 0329a158-758d-4e73-95a5-bab7307e7d70
title: ExtendedProperties.Remove method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExtendedProperties.Remove
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ExtendedProperties.Remove method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API function [**CertGetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty) and obtain the properties. For information about PInvoke, see [Platform Invoke Tutorial](https://msdn.microsoft.com/library/aa288468.aspx). The [.NET and CryptoAPI via P/Invoke: Part 1](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic5) and [.NET and CryptoAPI via P/Invoke: Part 2](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic6) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](/previous-versions/ms867087(v=msdn.10)) may also be helpful.\]

The **Remove** method removes an extended property from the collection.

## Syntax


```VB
ExtendedProperties.Remove( _
  ByVal propID _
)
```



## Parameters

<dl> <dt>

*propID* \[in\]
</dt> <dd>

A value of the [**CAPICOM\_PROPID**](capicom-propid.md) enumeration that defines the CAPICOM property identifiers of the extended property to remove. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_PROPID_UNKNOWN"></span><span id="capicom_propid_unknown"></span><dl> <dt>**CAPICOM\_PROPID\_UNKNOWN**</dt> </dl>                                                                       | The type of the property is not known.<br/>                                                                                                                                                                                                                                          |
| <span id="CAPICOM_PROPID_KEY_PROV_HANDLE"></span><span id="capicom_propid_key_prov_handle"></span><dl> <dt>**CAPICOM\_PROPID\_KEY\_PROV\_HANDLE**</dt> </dl>                                             | A handle to a key container within a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).<br/>                                                                                        |
| <span id="CAPICOM_PROPID_KEY_PROV_INFO"></span><span id="capicom_propid_key_prov_info"></span><dl> <dt>**CAPICOM\_PROPID\_KEY\_PROV\_INFO**</dt> </dl>                                                   | Information about a key container within a CSP.<br/>                                                                                                                                                                                                                                 |
| <span id="CAPICOM_PROPID_SHA1_HASH"></span><span id="capicom_propid_sha1_hash"></span><dl> <dt>**CAPICOM\_PROPID\_SHA1\_HASH**</dt> </dl>                                                                | A SHA1 hash object.<br/>                                                                                                                                                                                                                                                             |
| <span id="CAPICOM_PROPID_HASH_PROP"></span><span id="capicom_propid_hash_prop"></span><dl> <dt>**CAPICOM\_PROPID\_HASH\_PROP**</dt> </dl>                                                                | The properties of a hash object.<br/>                                                                                                                                                                                                                                                |
| <span id="CAPICOM_PROPID_MD5_HASH"></span><span id="capicom_propid_md5_hash"></span><dl> <dt>**CAPICOM\_PROPID\_MD5\_HASH**</dt> </dl>                                                                   | An MD5 hash object.<br/>                                                                                                                                                                                                                                                             |
| <span id="CAPICOM_PROPID_KEY_CONTEXT"></span><span id="capicom_propid_key_context"></span><dl> <dt>**CAPICOM\_PROPID\_KEY\_CONTEXT**</dt> </dl>                                                          | The key [*context*](../secgloss/c-gly.md).<br/>                                                                                                                                                                                                |
| <span id="CAPICOM_PROPID_KEY_SPEC"></span><span id="capicom_propid_key_spec"></span><dl> <dt>**CAPICOM\_PROPID\_KEY\_SPEC**</dt> </dl>                                                                   | The specifications for a key.<br/>                                                                                                                                                                                                                                                   |
| <span id="CAPICOM_PROPID_IE30_RESERVED"></span><span id="capicom_propid_ie30_reserved"></span><dl> <dt>**CAPICOM\_PROPID\_IE30\_RESERVED**</dt> </dl>                                                    | Information about whether the object is reserved in Internet Explorer 3.0.<br/>                                                                                                                                                                                                      |
| <span id="CAPICOM_PROPID_PUBKEY_HASH_RESERVED"></span><span id="capicom_propid_pubkey_hash_reserved"></span><dl> <dt>**CAPICOM\_PROPID\_PUBKEY\_HASH\_RESERVED**</dt> </dl>                              | Information about whether the hash of the public key is reserved.<br/>                                                                                                                                                                                                               |
| <span id="CAPICOM_PROPID_ENHKEY_USAGE"></span><span id="capicom_propid_enhkey_usage"></span><dl> <dt>**CAPICOM\_PROPID\_ENHKEY\_USAGE**</dt> </dl>                                                       | An [*enhanced key usage*](../secgloss/e-gly.md) (EKU).<br/>                                                                                                                                                              |
| <span id="CAPICOM_PROPID_CTL_USAGE"></span><span id="capicom_propid_ctl_usage"></span><dl> <dt>**CAPICOM\_PROPID\_CTL\_USAGE**</dt> </dl>                                                                | A [*certificate trust list*](../secgloss/c-gly.md) (CTL) usage.<br/>                                                                                                                                             |
| <span id="CAPICOM_PROPID_NEXT_UPDATE_LOCATION"></span><span id="capicom_propid_next_update_location"></span><dl> <dt>**CAPICOM\_PROPID\_NEXT\_UPDATE\_LOCATION**</dt> </dl>                              | The location of the next update to the [*certificate revocation list*](../secgloss/c-gly.md) (CRL).<br/>                                                                                               |
| <span id="CAPICOM_PROPID_FRIENDLY_NAME"></span><span id="capicom_propid_friendly_name"></span><dl> <dt>**CAPICOM\_PROPID\_FRIENDLY\_NAME**</dt> </dl>                                                    | A human-readable name.<br/>                                                                                                                                                                                                                                                          |
| <span id="CAPICOM_PROPID_PVK_FILE"></span><span id="capicom_propid_pvk_file"></span><dl> <dt>**CAPICOM\_PROPID\_PVK\_FILE**</dt> </dl>                                                                   | A file that contains a private key.<br/>                                                                                                                                                                                                                                             |
| <span id="CAPICOM_PROPID_DESCRIPTION"></span><span id="capicom_propid_description"></span><dl> <dt>**CAPICOM\_PROPID\_DESCRIPTION**</dt> </dl>                                                           | A human-readable description.<br/>                                                                                                                                                                                                                                                   |
| <span id="CAPICOM_PROPID_ACCESS_STATE"></span><span id="capicom_propid_access_state"></span><dl> <dt>**CAPICOM\_PROPID\_ACCESS\_STATE**</dt> </dl>                                                       | The state of the access.<br/>                                                                                                                                                                                                                                                        |
| <span id="CAPICOM_PROPID_SIGNATURE_HASH"></span><span id="capicom_propid_signature_hash"></span><dl> <dt>**CAPICOM\_PROPID\_SIGNATURE\_HASH**</dt> </dl>                                                 | A hash of the signature.<br/>                                                                                                                                                                                                                                                        |
| <span id="CAPICOM_PROPID_SMART_CARD_DATA"></span><span id="capicom_propid_smart_card_data"></span><dl> <dt>**CAPICOM\_PROPID\_SMART\_CARD\_DATA**</dt> </dl>                                             | Smart card data.<br/>                                                                                                                                                                                                                                                                |
| <span id="CAPICOM_PROPID_EFS"></span><span id="capicom_propid_efs"></span><dl> <dt>**CAPICOM\_PROPID\_EFS**</dt> </dl>                                                                                   | An Encrypting File System (EFS).<br/>                                                                                                                                                                                                                                                |
| <span id="CAPICOM_PROPID_FORTEZZA_DATA"></span><span id="capicom_propid_fortezza_data"></span><dl> <dt>**CAPICOM\_PROPID\_FORTEZZA\_DATA**</dt> </dl>                                                    | Data created using the cryptographic protocols and algorithms owned by the [*National Institute of Standards and Technology*](../secgloss/n-gly.md) (NIST).<br/> |
| <span id="CAPICOM_PROPID_ARCHIVED"></span><span id="capicom_propid_archived"></span><dl> <dt>**CAPICOM\_PROPID\_ARCHIVED**</dt> </dl>                                                                    | Information about whether the object is archived.<br/>                                                                                                                                                                                                                               |
| <span id="CAPICOM_PROPID_KEY_IDENTIFIER"></span><span id="capicom_propid_key_identifier"></span><dl> <dt>**CAPICOM\_PROPID\_KEY\_IDENTIFIER**</dt> </dl>                                                 | A key identifier.<br/>                                                                                                                                                                                                                                                               |
| <span id="CAPICOM_PROPID_AUTO_ENROLL"></span><span id="capicom_propid_auto_enroll"></span><dl> <dt>**CAPICOM\_PROPID\_AUTO\_ENROLL**</dt> </dl>                                                          | Auto-enrollment information for a certificate.<br/>                                                                                                                                                                                                                                  |
| <span id="CAPICOM_PROPID_PUBKEY_ALG_PARA"></span><span id="capicom_propid_pubkey_alg_para"></span><dl> <dt>**CAPICOM\_PROPID\_PUBKEY\_ALG\_PARA**</dt> </dl>                                             | Parameters for a public key algorithm.<br/>                                                                                                                                                                                                                                          |
| <span id="CAPICOM_PROPID_CROSS_CERT_DIST_POINTS"></span><span id="capicom_propid_cross_cert_dist_points"></span><dl> <dt>**CAPICOM\_PROPID\_CROSS\_CERT\_DIST\_POINTS**</dt> </dl>                       | Information used to update dynamic cross certificates.<br/>                                                                                                                                                                                                                          |
| <span id="CAPICOM_PROPID_ISSUER_PUBLIC_KEY_MD5_HASH"></span><span id="capicom_propid_issuer_public_key_md5_hash"></span><dl> <dt>**CAPICOM\_PROPID\_ISSUER\_PUBLIC\_KEY\_MD5\_HASH**</dt> </dl>          | The MD5 hash of the issuer's public key.<br/>                                                                                                                                                                                                                                        |
| <span id="CAPICOM_PROPID_SUBJECT_PUBLIC_KEY_MD5_HASH"></span><span id="capicom_propid_subject_public_key_md5_hash"></span><dl> <dt>**CAPICOM\_PROPID\_SUBJECT\_PUBLIC\_KEY\_MD5\_HASH**</dt> </dl>       | The MD5 hash of the subject's public key.<br/>                                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROPID_ENROLLMENT"></span><span id="capicom_propid_enrollment"></span><dl> <dt>**CAPICOM\_PROPID\_ENROLLMENT**</dt> </dl>                                                              | Information about the certificate's enrollment.<br/>                                                                                                                                                                                                                                 |
| <span id="CAPICOM_PROPID_DATE_STAMP"></span><span id="capicom_propid_date_stamp"></span><dl> <dt>**CAPICOM\_PROPID\_DATE\_STAMP**</dt> </dl>                                                             | A date stamp.<br/>                                                                                                                                                                                                                                                                   |
| <span id="CAPICOM_PROPID_ISSUER_SERIAL_NUMBER_MD5_HASH"></span><span id="capicom_propid_issuer_serial_number_md5_hash"></span><dl> <dt>**CAPICOM\_PROPID\_ISSUER\_SERIAL\_NUMBER\_MD5\_HASH**</dt> </dl> | The MD5 hash of the issuer's serial number.<br/>                                                                                                                                                                                                                                     |
| <span id="CAPICOM_PROPID_SUBJECT_NAME_MD5_HASH"></span><span id="capicom_propid_subject_name_md5_hash"></span><dl> <dt>**CAPICOM\_PROPID\_SUBJECT\_NAME\_MD5\_HASH**</dt> </dl>                          | The MD5 hash of the subject's name.<br/>                                                                                                                                                                                                                                             |
| <span id="CAPICOM_PROPID_EXTENDED_ERROR_INFO"></span><span id="capicom_propid_extended_error_info"></span><dl> <dt>**CAPICOM\_PROPID\_EXTENDED\_ERROR\_INFO**</dt> </dl>                                 | Extended information about an error.<br/>                                                                                                                                                                                                                                            |
| <span id="CAPICOM_PROPID_RENEWAL"></span><span id="capicom_propid_renewal"></span><dl> <dt>**CAPICOM\_PROPID\_RENEWAL**</dt> </dl>                                                                       | Information about the renewal of a [*certification authority*](../secgloss/c-gly.md).<br/>                                                                                                                     |
| <span id="CAPICOM_PROPID_ARCHIVED_KEY_HASH"></span><span id="capicom_propid_archived_key_hash"></span><dl> <dt>**CAPICOM\_PROPID\_ARCHIVED\_KEY\_HASH**</dt> </dl>                                       | An archived hash of a key.<br/>                                                                                                                                                                                                                                                      |
| <span id="CAPICOM_PROPID_FIRST_RESERVED"></span><span id="capicom_propid_first_reserved"></span><dl> <dt>**CAPICOM\_PROPID\_FIRST\_RESERVED**</dt> </dl>                                                 | Information about the first reservation.<br/>                                                                                                                                                                                                                                        |
| <span id="CAPICOM_PROPID_LAST_RESERVED"></span><span id="capicom_propid_last_reserved"></span><dl> <dt>**CAPICOM\_PROPID\_LAST\_RESERVED**</dt> </dl>                                                    | Information about the most recent reservation.<br/>                                                                                                                                                                                                                                  |
| <span id="CAPICOM_PROPID_FIRST_USER"></span><span id="capicom_propid_first_user"></span><dl> <dt>**CAPICOM\_PROPID\_FIRST\_USER**</dt> </dl>                                                             | Information about the first user.<br/>                                                                                                                                                                                                                                               |
| <span id="CAPICOM_PROPID_LAST_USER"></span><span id="capicom_propid_last_user"></span><dl> <dt>**CAPICOM\_PROPID\_LAST\_USER**</dt> </dl>                                                                | Information about the most recent user.<br/>                                                                                                                                                                                                                                         |



 

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
