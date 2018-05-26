---
Description: The following interfaces can be used to create certificate extensions.
ms.assetid: 52750a0a-0cd9-40cc-8c23-839e4e20fd77
title: Certificate Extension Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Extension Interfaces

The following interfaces can be used to create certificate extensions.



| Interface                                                                            | Description                                                                                                                                    |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAlternativeName**](/windows/win32/CertEnroll/nn-certenroll-ialternativename?branch=master)                                         | Represents an instance of an **AlternativeNames** extension.                                                                                   |
| [**IAlternativeNames**](/windows/win32/CertEnroll/nn-certenroll-ialternativenames?branch=master)                                       | Manages a collection of [**IAlternativeName**](/windows/win32/CertEnroll/nn-certenroll-ialternativename?branch=master) objects.                                                                  |
| [**ICertificatePolicy**](/windows/win32/CertEnroll/nn-certenroll-icertificatepolicy?branch=master)                                     | Specifies a certificate policy that identifies the purpose for which the certificate can be used.                                              |
| [**ICertificatePolicies**](/windows/win32/CertEnroll/nn-certenroll-icertificatepolicies?branch=master)                                 | Manages a collection of [**ICertificatePolicy**](/windows/win32/CertEnroll/nn-certenroll-icertificatepolicy?branch=master) objects.                                                              |
| [**IPolicyQualifier**](/windows/win32/CertEnroll/nn-certenroll-ipolicyqualifier?branch=master)                                         | Represents a qualifier that can be associated with a certificate policy.                                                                       |
| [**IPolicyQualifiers**](/windows/win32/CertEnroll/nn-certenroll-ipolicyqualifiers?branch=master)                                       | Manages a collection of [**IPolicyQualifier**](/windows/win32/CertEnroll/nn-certenroll-ipolicyqualifier?branch=master) objects.                                                                  |
| [**IX509Extension**](/windows/win32/CertEnroll/nn-certenroll-ix509extension?branch=master)                                             | Defines an extension for a certificate request.                                                                                                |
| [**IX509ExtensionAlternativeNames**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionalternativenames?branch=master)             | Specifies one or more alternative name forms for the subject of a certificate.                                                                 |
| [**IX509ExtensionAuthorityKeyIdentifier**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionauthoritykeyidentifier?branch=master) | Represents an **AuthorityKeyIdentifier** extension.                                                                                            |
| [**IX509ExtensionBasicConstraints**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionbasicconstraints?branch=master)             | Specifies whether the certificate subject is a certification authority and, if so, the depth of the subordinate certification authority chain. |
| [**IX509ExtensionCertificatePolicies**](/windows/win32/CertEnroll/nn-certenroll-ix509extensioncertificatepolicies?branch=master)       | Represents a collection of policy information terms.                                                                                           |
| [**IX509ExtensionMSApplicationPolicies**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionmsapplicationpolicies?branch=master)   | Represents a collection of object identifiers that indicate how a certificate can be used by an application.                                   |
| [**IX509ExtensionEnhancedKeyUsage**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionenhancedkeyusage?branch=master)             | Represents a collection of object identifiers that identify the intended uses of the public key contained in a certificate.                    |
| [**IX509ExtensionKeyUsage**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionkeyusage?branch=master)                             | Represents restrictions on the operations that can be performed by the public key contained in the certificate.                                |
| [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master)                                           | Manages a collection of [**IX509Extension**](/windows/win32/CertEnroll/nn-certenroll-ix509extension?branch=master) objects.                                                                      |
| [**IX509ExtensionSmimeCapabilities**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionsmimecapabilities?branch=master)           | Represents a collection that reports the decryption capabilities of an email recipient to an email sender.                                     |
| [**IX509ExtensionSubjectKeyIdentifier**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier?branch=master)     | Represents a **SubjectKeyIdentifier** extension used to identify a signing certificate.                                                        |
| [**IX509ExtensionTemplate**](/windows/win32/CertEnroll/nn-certenroll-ix509extensiontemplate?branch=master)                             | Represents a **CertificateTemplate** extension that contains a version 2 template.                                                             |
| [**IX509ExtensionTemplateName**](/windows/win32/CertEnroll/nn-certenroll-ix509extensiontemplatename?branch=master)                     | Represents a **CertificateTemplateName** extension that contains a version 1 template.                                                         |
| [**ISmimeCapabilities**](/windows/win32/CertEnroll/nn-certenroll-ismimecapabilities?branch=master)                                     | Manages a collection of [**ISmimeCapability**](/windows/win32/CertEnroll/nn-certenroll-ismimecapability?branch=master) objects.                                                                  |
| [**ISmimeCapability**](/windows/win32/CertEnroll/nn-certenroll-ismimecapability?branch=master)                                         | Represents an **SMIMECapabilities** extension that identifies the decryption capabilities of an email recipient.                               |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



