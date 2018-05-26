---
Description: The IX509CertificateRequestPkcs10V3 interface exposes the following properties.
ms.assetid: 96FCB9C4-7DDB-4B6B-A776-5A33E07B0BD3
title: IX509CertificateRequestPkcs10V3 Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IX509CertificateRequestPkcs10V3 Properties

The [**IX509CertificateRequestPkcs10V3**](/windows/win32/Certenroll/nn-certenroll-ix509certificaterequestpkcs10v3?branch=master) interface exposes the following properties.

## In this section



| Topic                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttestationEncryptionCertificate property**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_attestationencryptioncertificate?branch=master)<br/> | The certificate used to encrypt the EKPUB and EKCERT values from the client. This property must be set to a valid certificate that chains to a trusted machine root.<br/>                                                                                                                                                                                |
| [**AttestPrivateKey property**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_attestprivatekey?branch=master)<br/>                                 | True if the created private key needs to be attested; otherwise false. If true, it is expected that the [**AttestationEncryptionCertificate**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_attestationencryptioncertificate?branch=master) property has been set. <br/>                                                                                                        |
| [**ChallengePassword property**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_challengepassword?branch=master)<br/>                               | The password to use when creating a request with a challenge. To create a request without a challenge, do not set the [**ChallengePassword**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_challengepassword?branch=master) property.<br/>                                                                                                                                      |
| [**EncryptionAlgorithm property**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_encryptionalgorithm?branch=master)<br/>                           | The encryption algorithm used to encrypt the EKPUB and EKCERT values from the client.<br/>                                                                                                                                                                                                                                                               |
| [**EncryptionStrength property**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_encryptionstrength?branch=master)<br/>                             | Identifies the bit length for the [**EncryptionAlgorithm**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_encryptionalgorithm?branch=master) to use for encryption. If the **EncryptionAlgorithm** only supports one bit length, then you do not need to specify a value for the [**EncryptionStrength**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_encryptionstrength?branch=master) property.<br/> |
| [**NameValuePairs property**](/windows/win32/Certenroll/nf-certenroll-ix509certificaterequestpkcs10v3-get_namevaluepairs?branch=master)<br/>                                     | A collection of name/value pairs of additional certificate property values.<br/>                                                                                                                                                                                                                                                                         |



 

 

 




