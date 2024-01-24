---
description: The IX509CertificateRequestPkcs10V3 interface exposes the following properties.
ms.assetid: 96FCB9C4-7DDB-4B6B-A776-5A33E07B0BD3
title: IX509CertificateRequestPkcs10V3 Properties
ms.topic: reference
ms.date: 05/31/2018
---

# IX509CertificateRequestPkcs10V3 Properties

The [**IX509CertificateRequestPkcs10V3**](/windows/desktop/api/Certenroll/nn-certenroll-ix509certificaterequestpkcs10v3) interface exposes the following properties.

## In this section



| Topic                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttestationEncryptionCertificate property**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_attestationencryptioncertificate)<br/> | The certificate used to encrypt the EKPUB and EKCERT values from the client. This property must be set to a valid certificate that chains to a trusted machine root.<br/>                                                                                                                                                                                |
| [**AttestPrivateKey property**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_attestprivatekey)<br/>                                 | True if the created private key needs to be attested; otherwise false. If true, it is expected that the [**AttestationEncryptionCertificate**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_attestationencryptioncertificate) property has been set. <br/>                                                                                                        |
| [**ChallengePassword property**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_challengepassword)<br/>                               | The password to use when creating a request with a challenge. To create a request without a challenge, do not set the [**ChallengePassword**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_challengepassword) property.<br/>                                                                                                                                      |
| [**EncryptionAlgorithm property**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_encryptionalgorithm)<br/>                           | The encryption algorithm used to encrypt the EKPUB and EKCERT values from the client.<br/>                                                                                                                                                                                                                                                               |
| [**EncryptionStrength property**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_encryptionstrength)<br/>                             | Identifies the bit length for the [**EncryptionAlgorithm**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_encryptionalgorithm) to use for encryption. If the **EncryptionAlgorithm** only supports one bit length, then you do not need to specify a value for the [**EncryptionStrength**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_encryptionstrength) property.<br/> |
| [**NameValuePairs property**](/windows/desktop/api/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_namevaluepairs)<br/>                                     | A collection of name/value pairs of additional certificate property values.<br/>                                                                                                                                                                                                                                                                         |



 

 

 




