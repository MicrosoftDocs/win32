---
description: Provides the names for CAPICOM object identifiers.
ms.assetid: 6c1eb2cc-84ac-4920-99ba-56ac8de4a851
title: CAPICOM_OID enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_OID
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_OID enumeration

The **CAPICOM\_OID** enumeration provides the names for CAPICOM object identifiers.

This enumeration is used by the [**OID.Name**](oid-name.md) property.

## Members



| Member                                                        | Description                                                                                                                                                                                                                                    | Value |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_OID\_OTHER**                                       | The object is not one of the predefined CAPICOM object types.<br/>                                                                                                                                                                       | 0     |
| **CAPICOM\_OID\_AUTHORITY\_KEY\_IDENTIFIER\_EXTENSION**       | The object is a certificate extension that contains the public key identifier of the certification authority (CA).<br/>                                                                                                                  | 1     |
| **CAPICOM\_OID\_KEY\_ATTRIBUTES\_EXTENSION**                  | The object is a certificate extension that contains optional attributes of a public key.<br/>                                                                                                                                            | 2     |
| **CAPICOM\_OID\_CERT\_POLICIES\_95\_EXTENSION**               | The object is a certificate extension that contains Windows 95 certificate policy information.<br/>                                                                                                                                      | 3     |
| **CAPICOM\_OID\_KEY\_USAGE\_RESTRICTION\_EXTENSION**          | The object is a certificate extension that contains restrictions on the use of a certificate's public key.<br/>                                                                                                                          | 4     |
| **CAPICOM\_OID\_LEGACY\_POLICY\_MAPPINGS\_EXTENSION**         | The object is a certificate extension that contains legacy policy mapping information.<br/>                                                                                                                                              | 5     |
| **CAPICOM\_OID\_SUBJECT\_ALT\_NAME\_EXTENSION**               | The object is a certificate extension that contains an alternative name for the subject of the certificate.<br/>                                                                                                                         | 6     |
| **CAPICOM\_OID\_ISSUER\_ALT\_NAME\_EXTENSION**                | The object is a certificate extension that contains an alternative name for the issuer of the certificate.<br/>                                                                                                                          | 7     |
| **CAPICOM\_OID\_BASIC\_CONSTRAINTS\_EXTENSION**               | The object is a certificate extension that indicates whether the certified subject can act as a CA, an end-entity, or both. <br/>                                                                                                        | 8     |
| **CAPICOM\_OID\_SUBJECT\_KEY\_IDENTIFIER\_EXTENSION**         | The object is a certificate extension that contains the key identifier of the subject of the certificate.<br/>                                                                                                                           | 9     |
| **CAPICOM\_OID\_KEY\_USAGE\_EXTENSION**                       | The object is a certificate extension that contains information about the intended use of a certificate's public key.<br/>                                                                                                               | 10    |
| **CAPICOM\_OID\_PRIVATEKEY\_USAGE\_PERIOD\_EXTENSION**        | The object is a certificate extension that contains information about the time period during which a certificate's private key is usable.<br/>                                                                                           | 11    |
| **CAPICOM\_OID\_SUBJECT\_ALT\_NAME2\_EXTENSION**              | The object is a certificate extension that contains an alternative name for the subject of the certificate.<br/>                                                                                                                         | 12    |
| **CAPICOM\_OID\_ISSUER\_ALT\_NAME2\_EXTENSION**               | The object is a certificate extension that contains an alternative name for the issuer of the certificate.<br/>                                                                                                                          | 13    |
| **CAPICOM\_OID\_BASIC\_CONSTRAINTS2\_EXTENSION**              | The object is a certificate extension that indicates whether the certified subject can act as a CA, an end-entity, or both. <br/>                                                                                                        | 14    |
| **CAPICOM\_OID\_NAME\_CONSTRAINTS\_EXTENSION**                | The object is a certificate extension that contains information about certificates that are specifically permitted or excluded from trust.<br/>                                                                                          | 15    |
| **CAPICOM\_OID\_CRL\_DIST\_POINTS\_EXTENSION**                | The object is a certificate extension that contains information used to update the certificate revocation list (CRL).<br/>                                                                                                               | 16    |
| **CAPICOM\_OID\_CERT\_POLICIES\_EXTENSION**                   | The object is a certificate extension that contains a list of the policies that the certificate supports.<br/>                                                                                                                           | 17    |
| **CAPICOM\_OID\_POLICY\_MAPPINGS\_EXTENSION**                 | The object is a certificate extension that provides mappings between policies in different domains.<br/>                                                                                                                                 | 18    |
| **CAPICOM\_OID\_AUTHORITY\_KEY\_IDENTIFIER2\_EXTENSION**      | The object is a certificate extension that contains the public key identifier of the CA.<br/>                                                                                                                                            | 19    |
| **CAPICOM\_OID\_POLICY\_CONSTRAINTS\_EXTENSION**              | The object is a certificate extension that contains established policies for accepting certificates as trusted.<br/>                                                                                                                     | 20    |
| **CAPICOM\_OID\_ENHANCED\_KEY\_USAGE\_EXTENSION**             | The object is a certificate extension that contains enhanced information about the intended use of a certificate's public key.<br/>                                                                                                      | 21    |
| **CAPICOM\_OID\_CERTIFICATE\_TEMPLATE\_EXTENSION**            | The object is a certificate extension that contains a certificate template.<br/>                                                                                                                                                         | 22    |
| **CAPICOM\_OID\_APPLICATION\_CERT\_POLICIES\_EXTENSION**      | The object is a certificate extension that contains the application policy of the certificate.<br/>                                                                                                                                      | 23    |
| **CAPICOM\_OID\_APPLICATION\_POLICY\_MAPPINGS\_EXTENSION**    | The object is a certificate extension that contains mappings between different application policies.<br/>                                                                                                                                | 24    |
| **CAPICOM\_OID\_APPLICATION\_POLICY\_CONSTRAINTS\_EXTENSION** | The object is a certificate extension that contains the application policy constraints of the certificate.<br/>                                                                                                                          | 25    |
| **CAPICOM\_OID\_AUTHORITY\_INFO\_ACCESS\_EXTENSION**          | The object is a certificate extension that indicates how to access CA information and services for the issuer of the certificate.<br/>                                                                                                   | 26    |
| **CAPICOM\_OID\_SERVER\_AUTH\_EKU**                           | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used to authenticate a server.<br/>                                                                                                                | 100   |
| **CAPICOM\_OID\_CLIENT\_AUTH\_EKU**                           | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used to authenticate a client.<br/>                                                                                                                | 101   |
| **CAPICOM\_OID\_CODE\_SIGNING\_EKU**                          | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used to create a digital signature.<br/>                                                                                                           | 102   |
| **CAPICOM\_OID\_EMAIL\_PROTECTION\_EKU**                      | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for email protection.<br/>                                                                                                                    | 103   |
| **CAPICOM\_OID\_IPSEC\_END\_SYSTEM\_EKU**                     | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for an IPsec end system.<br/>                                                                                                                 | 104   |
| **CAPICOM\_OID\_IPSEC\_TUNNEL\_EKU**                          | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for IPsec tunneling.<br/>                                                                                                                     | 105   |
| **CAPICOM\_OID\_IPSEC\_USER\_EKU**                            | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for an IPsec user.<br/>                                                                                                                       | 106   |
| **CAPICOM\_OID\_TIME\_STAMPING\_EKU**                         | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for time stamping.<br/>                                                                                                                       | 107   |
| **CAPICOM\_OID\_CTL\_USAGE\_SIGNING\_EKU**                    | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used to sign the certificate trust list (CTL).<br/>                                                                                                | 108   |
| **CAPICOM\_OID\_TIME\_STAMP\_SIGNING\_EKU**                   | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used to sign a time stamp.<br/>                                                                                                                    | 109   |
| **CAPICOM\_OID\_SERVER\_GATED\_CRYPTO\_EKU**                  | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for [*server-gated cryptography*](../secgloss/s-gly.md) (SGC).<br/> | 110   |
| **CAPICOM\_OID\_ENCRYPTING\_FILE\_SYSTEM\_EKU**               | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for the [*Encrypting File System*](../secgloss/e-gly.md) (EFS).<br/>      | 111   |
| **CAPICOM\_OID\_EFS\_RECOVERY\_EKU**                          | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for recovery of the EFS.<br/>                                                                                                                 | 112   |
| **CAPICOM\_OID\_WHQL\_CRYPTO\_EKU**                           | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for Windows Hardware Quality Labs (WHQL) cryptography.<br/>                                                                                   | 113   |
| **CAPICOM\_OID\_NT5\_CRYPTO\_EKU**                            | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for Windows Server 2003 and Windows XP cryptography.<br/>                                                                                     | 114   |
| **CAPICOM\_OID\_OEM\_WHQL\_CRYPTO\_EKU**                      | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for Original Equipment Manufacturers (OEM) WHQL cryptography.<br/>                                                                            | 115   |
| **CAPICOM\_OID\_EMBEDED\_NT\_CRYPTO\_EKU**                    | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for Windows NT Embedded cryptography.<br/>                                                                                                    | 116   |
| **CAPICOM\_OID\_ROOT\_LIST\_SIGNER\_EKU**                     | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used to sign a root list.<br/>                                                                                                                     | 117   |
| **CAPICOM\_OID\_QUALIFIED\_SUBORDINATION\_EKU**               | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for qualified subordination.<br/>                                                                                                             | 118   |
| **CAPICOM\_OID\_KEY\_RECOVERY\_EKU**                          | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for key recovery.<br/>                                                                                                                        | 119   |
| **CAPICOM\_OID\_DIGITAL\_RIGHTS\_EKU**                        | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for digital rights.<br/>                                                                                                                      | 120   |
| **CAPICOM\_OID\_LICENSES\_EKU**                               | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for licenses.<br/>                                                                                                                            | 121   |
| **CAPICOM\_OID\_LICENSE\_SERVER\_EKU**                        | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for a license server.<br/>                                                                                                                    | 122   |
| **CAPICOM\_OID\_SMART\_CARD\_LOGON\_EKU**                     | The object is an [**EKU**](eku.md) object that specifies that the certificate can be used for smart card logon.<br/>                                                                                                                    | 123   |
| **CAPICOM\_OID\_PKIX\_POLICY\_QUALIFIER\_CPS**                | The object is a Certification Practice Statement (CPS) that can be used for the public key infrastructure X.509 (PKIX) policy qualifier.<br/>                                                                                            | 124   |
| **CAPICOM\_OID\_PKIX\_POLICY\_QUALIFIER\_USERNOTICE**         | The object is a user notice that can be used for the public key infrastructure X.509 (PKIX) policy qualifier.<br/>                                                                                                                       | 125   |



## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
