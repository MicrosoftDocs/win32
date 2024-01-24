---
description: The following interfaces can be used to create certificate extensions.
ms.assetid: 52750a0a-0cd9-40cc-8c23-839e4e20fd77
title: Certificate Extension Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Extension Interfaces

The following interfaces can be used to create certificate extensions.



| Interface                                                                            | Description                                                                                                                                    |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAlternativeName**](/windows/desktop/api/CertEnroll/nn-certenroll-ialternativename)                                         | Represents an instance of an **AlternativeNames** extension.                                                                                   |
| [**IAlternativeNames**](/windows/desktop/api/CertEnroll/nn-certenroll-ialternativenames)                                       | Manages a collection of [**IAlternativeName**](/windows/desktop/api/CertEnroll/nn-certenroll-ialternativename) objects.                                                                  |
| [**ICertificatePolicy**](/windows/desktop/api/CertEnroll/nn-certenroll-icertificatepolicy)                                     | Specifies a certificate policy that identifies the purpose for which the certificate can be used.                                              |
| [**ICertificatePolicies**](/windows/desktop/api/CertEnroll/nn-certenroll-icertificatepolicies)                                 | Manages a collection of [**ICertificatePolicy**](/windows/desktop/api/CertEnroll/nn-certenroll-icertificatepolicy) objects.                                                              |
| [**IPolicyQualifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ipolicyqualifier)                                         | Represents a qualifier that can be associated with a certificate policy.                                                                       |
| [**IPolicyQualifiers**](/windows/desktop/api/CertEnroll/nn-certenroll-ipolicyqualifiers)                                       | Manages a collection of [**IPolicyQualifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ipolicyqualifier) objects.                                                                  |
| [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)                                             | Defines an extension for a certificate request.                                                                                                |
| [**IX509ExtensionAlternativeNames**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionalternativenames)             | Specifies one or more alternative name forms for the subject of a certificate.                                                                 |
| [**IX509ExtensionAuthorityKeyIdentifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionauthoritykeyidentifier) | Represents an **AuthorityKeyIdentifier** extension.                                                                                            |
| [**IX509ExtensionBasicConstraints**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionbasicconstraints)             | Specifies whether the certificate subject is a certification authority and, if so, the depth of the subordinate certification authority chain. |
| [**IX509ExtensionCertificatePolicies**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensioncertificatepolicies)       | Represents a collection of policy information terms.                                                                                           |
| [**IX509ExtensionMSApplicationPolicies**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionmsapplicationpolicies)   | Represents a collection of object identifiers that indicate how a certificate can be used by an application.                                   |
| [**IX509ExtensionEnhancedKeyUsage**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionenhancedkeyusage)             | Represents a collection of object identifiers that identify the intended uses of the public key contained in a certificate.                    |
| [**IX509ExtensionKeyUsage**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionkeyusage)                             | Represents restrictions on the operations that can be performed by the public key contained in the certificate.                                |
| [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions)                                           | Manages a collection of [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension) objects.                                                                      |
| [**IX509ExtensionSmimeCapabilities**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsmimecapabilities)           | Represents a collection that reports the decryption capabilities of an email recipient to an email sender.                                     |
| [**IX509ExtensionSubjectKeyIdentifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier)     | Represents a **SubjectKeyIdentifier** extension used to identify a signing certificate.                                                        |
| [**IX509ExtensionTemplate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplate)                             | Represents a **CertificateTemplate** extension that contains a version 2 template.                                                             |
| [**IX509ExtensionTemplateName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplatename)                     | Represents a **CertificateTemplateName** extension that contains a version 1 template.                                                         |
| [**ISmimeCapabilities**](/windows/desktop/api/CertEnroll/nn-certenroll-ismimecapabilities)                                     | Manages a collection of [**ISmimeCapability**](/windows/desktop/api/CertEnroll/nn-certenroll-ismimecapability) objects.                                                                  |
| [**ISmimeCapability**](/windows/desktop/api/CertEnroll/nn-certenroll-ismimecapability)                                         | Represents an **SMIMECapabilities** extension that identifies the decryption capabilities of an email recipient.                               |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



