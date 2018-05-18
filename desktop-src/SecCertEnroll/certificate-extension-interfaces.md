---
Description: 'The following interfaces can be used to create certificate extensions.'
ms.assetid: '52750a0a-0cd9-40cc-8c23-839e4e20fd77'
title: Certificate Extension Interfaces
---

# Certificate Extension Interfaces

The following interfaces can be used to create certificate extensions.



| Interface                                                                            | Description                                                                                                                                    |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAlternativeName**](ialternativename.md)                                         | Represents an instance of an **AlternativeNames** extension.                                                                                   |
| [**IAlternativeNames**](ialternativenames.md)                                       | Manages a collection of [**IAlternativeName**](ialternativename.md) objects.                                                                  |
| [**ICertificatePolicy**](icertificatepolicy.md)                                     | Specifies a certificate policy that identifies the purpose for which the certificate can be used.                                              |
| [**ICertificatePolicies**](icertificatepolicies.md)                                 | Manages a collection of [**ICertificatePolicy**](icertificatepolicy.md) objects.                                                              |
| [**IPolicyQualifier**](ipolicyqualifier.md)                                         | Represents a qualifier that can be associated with a certificate policy.                                                                       |
| [**IPolicyQualifiers**](ipolicyqualifiers.md)                                       | Manages a collection of [**IPolicyQualifier**](ipolicyqualifier.md) objects.                                                                  |
| [**IX509Extension**](ix509extension.md)                                             | Defines an extension for a certificate request.                                                                                                |
| [**IX509ExtensionAlternativeNames**](ix509extensionalternativenames.md)             | Specifies one or more alternative name forms for the subject of a certificate.                                                                 |
| [**IX509ExtensionAuthorityKeyIdentifier**](ix509extensionauthoritykeyidentifier.md) | Represents an **AuthorityKeyIdentifier** extension.                                                                                            |
| [**IX509ExtensionBasicConstraints**](ix509extensionbasicconstraints.md)             | Specifies whether the certificate subject is a certification authority and, if so, the depth of the subordinate certification authority chain. |
| [**IX509ExtensionCertificatePolicies**](ix509extensioncertificatepolicies.md)       | Represents a collection of policy information terms.                                                                                           |
| [**IX509ExtensionMSApplicationPolicies**](ix509extensionmsapplicationpolicies.md)   | Represents a collection of object identifiers that indicate how a certificate can be used by an application.                                   |
| [**IX509ExtensionEnhancedKeyUsage**](ix509extensionenhancedkeyusage.md)             | Represents a collection of object identifiers that identify the intended uses of the public key contained in a certificate.                    |
| [**IX509ExtensionKeyUsage**](ix509extensionkeyusage.md)                             | Represents restrictions on the operations that can be performed by the public key contained in the certificate.                                |
| [**IX509Extensions**](ix509extensions.md)                                           | Manages a collection of [**IX509Extension**](ix509extension.md) objects.                                                                      |
| [**IX509ExtensionSmimeCapabilities**](ix509extensionsmimecapabilities.md)           | Represents a collection that reports the decryption capabilities of an email recipient to an email sender.                                     |
| [**IX509ExtensionSubjectKeyIdentifier**](ix509extensionsubjectkeyidentifier.md)     | Represents a **SubjectKeyIdentifier** extension used to identify a signing certificate.                                                        |
| [**IX509ExtensionTemplate**](ix509extensiontemplate.md)                             | Represents a **CertificateTemplate** extension that contains a version 2 template.                                                             |
| [**IX509ExtensionTemplateName**](ix509extensiontemplatename.md)                     | Represents a **CertificateTemplateName** extension that contains a version 1 template.                                                         |
| [**ISmimeCapabilities**](ismimecapabilities.md)                                     | Manages a collection of [**ISmimeCapability**](ismimecapability.md) objects.                                                                  |
| [**ISmimeCapability**](ismimecapability.md)                                         | Represents an **SMIMECapabilities** extension that identifies the decryption capabilities of an email recipient.                               |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



