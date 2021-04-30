---
description: The Certificate Enrollment API supports the following attributes. You can create an individual attribute by using the corresponding interface identified in each of the following sections.
ms.assetid: e14fd472-1974-4ad2-b35a-3ab58ba0d707
title: Supported Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Supported Attributes

The Certificate Enrollment API supports the following attributes. You can create an individual attribute by using the corresponding interface identified in each of the following sections.

## ClientId

The [**IX509AttributeClientId**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeclientid) interface can be used to define an attribute that contains information about the client computer that sent the certificate request. The information can be used for diagnostics.

**Applies To:** PKCS \#10 or CMC request.

**OID:** XCN\_OID\_REQUEST\_CLIENT\_INFO (1.3.6.1.4.1.311.21.20)

## Extensions

The [**IX509AttributeExtensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeextensions) interface can be used to define a set of X.509 version 3 certificate extensions. The following extensions are supported. For more information, see the Extension Interfaces topic.



| Extension              | Description                                                                                                                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AlternativeNames       | Contains one or more alternative name forms of the issuer associated with the certificate.                                                                                                                                       |
| AuthorityKeyIdentifier | Contains a unique key identifier to differentiate between multiple certificate signing keys of the [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA). |
| BasicConstraints       | Indicates whether the subject can act as a CA.                                                                                                                                                                                   |
| CertificatePolicies    | Identifies the policies and optional qualifier information associated with the certificate.                                                                                                                                      |
| MSApplicationPolicies  | Identifies one or more uses for the certificate. This extension is similar to the EnhancedKeyUsage extension but is Microsoft-defined.                                                                                           |
| EnhancedKeyUsage       | Identifies one or more uses of the public key contained in the certificate. The enhanced key usage extension can be used in addition to or in place of the key usage extension.                                                  |
| KeyUsage               | Identifies restrictions on the operations that can be performed by the public key contained in the certificate.                                                                                                                  |
| SmimeCapabilities      | Reports the decryption capabilities of an email recipient to the email sender to enable the sender to choose the most secure symmetric algorithm supported by both parties.                                                      |
| SubjectKeyIdentifier   | Contains a unique key identifier that can be used to differentiate between multiple signing keys associated with the certificate owner.                                                                                          |
| Template               | Identifies the template to use when issuing or renewing a certificate. The extension contains the object identifier (OID) of the template.                                                                                       |
| TemplateName           | Identifies the template to use when issuing or renewing a certificate. The extension contains the name of the template.                                                                                                          |



 

**Applies To:** PKCS \#10 request.

**OID:** XCN\_OID\_RSA\_certExtensions (1.2.840.113549.1.9.14)

## ArchiveKey

The [**IX509AttributeArchiveKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekey) interface can be used to define an attribute that contains an encrypted private key submitted to a CA for archiving.

**Applies To:** CMC request.

**OID:** XCN\_OID\_ARCHIVED\_KEY\_ATTR (1.3.6.1.4.1.311.21.13)

## ArchiveKeyHash

The [**IX509AttributeArchiveKeyHash**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekeyhash) interface can be used to define a hash of the private key contained in the **ArchiveKey** attribute.

**Applies To:** CMC request.

**OID:** XCN\_OID\_ENCRYPTED\_KEY\_HASH (1.3.6.1.4.1.311.21.21)

## CspProvider

The [**IX509AttributeCspProvider**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributecspprovider) interface can be used to define an attribute that contains information about the [*cryptographic service provider*](/windows/desktop/SecGloss/c-gly) (CSP) used by the requester for cryptographic operations.

**Applies To:** PKCS \#10 request. This attribute is automatically created when you create an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.

**OID:** XCN\_OID\_ENROLLMENT\_CSP\_PROVIDER (1.3.6.1.4.1.311.13.2.2)

## OSVersion

The [**IX509AttributeOSVersion**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeosversion) interface can be used to create an attribute that contains version information about the client operating system. The information can be used by the CA to determine the type of processing to apply when creating the certificate.

**Applies To:** PKCS \#10 or CMC request.

**OID:** XCN\_OID\_OS\_VERSION (1.3.6.1.4.1.311.13.2.3)

## RenewalCertificate

The [**IX509AttributeRenewalCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributerenewalcertificate) interface can be used to create an attribute that contains the certificate being renewed.

**Applies To:** PKCS \#10 request. This attribute is automatically created if you create a PKCS \#10 request by initiating it with the certificate being renewed.

**OID:** XCN\_OID\_RENEWAL\_CERTIFICATE (1.3.6.1.4.1.311.13.1)

 

 
