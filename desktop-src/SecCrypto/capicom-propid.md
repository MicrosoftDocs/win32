---
description: Defines the CAPICOM property identifiers.
ms.assetid: faf10018-3ed8-4de6-9838-c553626f6dd7
title: CAPICOM_PROPID enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_PROPID
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_PROPID enumeration

The **CAPICOM\_PROPID** enumeration defines the CAPICOM property identifiers.

## Members



| Member                                                 | Description                                                                                                                                                                                                                                                                                | Value      |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **CAPICOM\_PROPID\_UNKNOWN**                           | The type of the property is not known.<br/>                                                                                                                                                                                                                                          | 0          |
| **CAPICOM\_PROPID\_KEY\_PROV\_HANDLE**                 | A handle to a key container within a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).<br/>                                                                                        | 1          |
| **CAPICOM\_PROPID\_KEY\_PROV\_INFO**                   | Information about a key container within a CSP.<br/>                                                                                                                                                                                                                                 | 2          |
| **CAPICOM\_PROPID\_SHA1\_HASH**                        | A SHA1 hash object.<br/>                                                                                                                                                                                                                                                             | 3          |
| **CAPICOM\_PROPID\_HASH\_PROP**                        | The properties of a hash object.<br/>                                                                                                                                                                                                                                                | 3          |
| **CAPICOM\_PROPID\_MD5\_HASH**                         | An MD5 hash object.<br/>                                                                                                                                                                                                                                                             | 4          |
| **CAPICOM\_PROPID\_KEY\_CONTEXT**                      | The key [*context*](../secgloss/c-gly.md).<br/>                                                                                                                                                                                                | 5          |
| **CAPICOM\_PROPID\_KEY\_SPEC**                         | The specifications for a key.<br/>                                                                                                                                                                                                                                                   | 6          |
| **CAPICOM\_PROPID\_IE30\_RESERVED**                    | Information about whether the object is reserved in Internet Explorer 3.0.<br/>                                                                                                                                                                                                      | 7          |
| **CAPICOM\_PROPID\_PUBKEY\_HASH\_RESERVED**            | Information about whether the hash of the public key is reserved.<br/>                                                                                                                                                                                                               | 8          |
| **CAPICOM\_PROPID\_ENHKEY\_USAGE**                     | An [*enhanced key usage*](../secgloss/e-gly.md) (EKU).<br/>                                                                                                                                                              | 9          |
| **CAPICOM\_PROPID\_CTL\_USAGE**                        | A [*certificate trust list*](../secgloss/c-gly.md) (CTL) usage.<br/>                                                                                                                                             | 9          |
| **CAPICOM\_PROPID\_NEXT\_UPDATE\_LOCATION**            | The location of the next update to the [*certificate revocation list*](../secgloss/c-gly.md) (CRL).<br/>                                                                                               | 10         |
| **CAPICOM\_PROPID\_FRIENDLY\_NAME**                    | A human-readable name.<br/>                                                                                                                                                                                                                                                          | 11         |
| **CAPICOM\_PROPID\_PVK\_FILE**                         | A file that contains a private key.<br/>                                                                                                                                                                                                                                             | 12         |
| **CAPICOM\_PROPID\_DESCRIPTION**                       | A human-readable description.<br/>                                                                                                                                                                                                                                                   | 13         |
| **CAPICOM\_PROPID\_ACCESS\_STATE**                     | The state of the access.<br/>                                                                                                                                                                                                                                                        | 14         |
| **CAPICOM\_PROPID\_SIGNATURE\_HASH**                   | A hash of the signature.<br/>                                                                                                                                                                                                                                                        | 15         |
| **CAPICOM\_PROPID\_SMART\_CARD\_DATA**                 | Smart card data.<br/>                                                                                                                                                                                                                                                                | 16         |
| **CAPICOM\_PROPID\_EFS**                               | An [*Encrypting File System*](../secgloss/e-gly.md) (EFS).<br/>                                                                                                                                                  | 17         |
| **CAPICOM\_PROPID\_FORTEZZA\_DATA**                    | Data created using the cryptographic protocols and algorithms owned by the [*National Institute of Standards and Technology*](../secgloss/n-gly.md) (NIST).<br/> | 18         |
| **CAPICOM\_PROPID\_ARCHIVED**                          | Information about whether the object is archived.<br/>                                                                                                                                                                                                                               | 19         |
| **CAPICOM\_PROPID\_KEY\_IDENTIFIER**                   | A key identifier.<br/>                                                                                                                                                                                                                                                               | 20         |
| **CAPICOM\_PROPID\_AUTO\_ENROLL**                      | Auto-enrollment information for a certificate.<br/>                                                                                                                                                                                                                                  | 21         |
| **CAPICOM\_PROPID\_PUBKEY\_ALG\_PARA**                 | Parameters for a public key algorithm.<br/>                                                                                                                                                                                                                                          | 22         |
| **CAPICOM\_PROPID\_CROSS\_CERT\_DIST\_POINTS**         | Information used to update dynamic cross certificates.<br/>                                                                                                                                                                                                                          | 23         |
| **CAPICOM\_PROPID\_ISSUER\_PUBLIC\_KEY\_MD5\_HASH**    | The MD5 hash of the issuer's public key.<br/>                                                                                                                                                                                                                                        | 24         |
| **CAPICOM\_PROPID\_SUBJECT\_PUBLIC\_KEY\_MD5\_HASH**   | The MD5 hash of the subject's public key.<br/>                                                                                                                                                                                                                                       | 25         |
| **CAPICOM\_PROPID\_ENROLLMENT**                        | Information about the certificate's enrollment.<br/>                                                                                                                                                                                                                                 | 26         |
| **CAPICOM\_PROPID\_DATE\_STAMP**                       | A date stamp.<br/>                                                                                                                                                                                                                                                                   | 27         |
| **CAPICOM\_PROPID\_ISSUER\_SERIAL\_NUMBER\_MD5\_HASH** | The MD5 hash of the issuer's serial number.<br/>                                                                                                                                                                                                                                     | 28         |
| **CAPICOM\_PROPID\_SUBJECT\_NAME\_MD5\_HASH**          | The MD5 hash of the subject's name.<br/>                                                                                                                                                                                                                                             | 29         |
| **CAPICOM\_PROPID\_EXTENDED\_ERROR\_INFO**             | Extended information about an error.<br/>                                                                                                                                                                                                                                            | 30         |
| **CAPICOM\_PROPID\_RENEWAL**                           | Information about the renewal of a [*certification authority*](../secgloss/c-gly.md).<br/>                                                                                                                     | 64         |
| **CAPICOM\_PROPID\_ARCHIVED\_KEY\_HASH**               | An archived hash of a key.<br/>                                                                                                                                                                                                                                                      | 65         |
| **CAPICOM\_PROPID\_FIRST\_RESERVED**                   | Information about the first reservation.<br/>                                                                                                                                                                                                                                        | 66         |
| **CAPICOM\_PROPID\_LAST\_RESERVED**                    | Information about the most recent reservation.<br/>                                                                                                                                                                                                                                  | 0x00007FFF |
| **CAPICOM\_PROPID\_FIRST\_USER**                       | Information about the first user.<br/>                                                                                                                                                                                                                                               | 0x00008000 |
| **CAPICOM\_PROPID\_LAST\_USER**                        | Information about the most recent user.<br/>                                                                                                                                                                                                                                         | 0x0000FFFF |



## Remarks

This enumeration is used by the following CAPICOM properties:

-   [**ExtendedProperty.PropID**](extendedproperty-propid.md)
-   [**ExtendedProperties.Remove**](extendedproperties-remove.md)

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
