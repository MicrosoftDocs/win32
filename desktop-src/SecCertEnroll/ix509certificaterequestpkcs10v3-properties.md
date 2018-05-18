---
Description: 'The IX509CertificateRequestPkcs10V3 interface exposes the following properties.'
ms.assetid: '96FCB9C4-7DDB-4B6B-A776-5A33E07B0BD3'
title: IX509CertificateRequestPkcs10V3 Properties
---

# IX509CertificateRequestPkcs10V3 Properties

The [**IX509CertificateRequestPkcs10V3**](ix509certificaterequestpkcs10v3.md) interface exposes the following properties.

## In this section



| Topic                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttestationEncryptionCertificate property**](ix509certificaterequestpkcs10v3-attestationencryptioncertificate.md)<br/> | The certificate used to encrypt the EKPUB and EKCERT values from the client. This property must be set to a valid certificate that chains to a trusted machine root.<br/>                                                                                                                                                                                |
| [**AttestPrivateKey property**](ix509certificaterequestpkcs10v3-attestprivatekey.md)<br/>                                 | True if the created private key needs to be attested; otherwise false. If true, it is expected that the [**AttestationEncryptionCertificate**](ix509certificaterequestpkcs10v3-attestationencryptioncertificate.md) property has been set. <br/>                                                                                                        |
| [**ChallengePassword property**](ix509certificaterequestpkcs10v3-challengepassword.md)<br/>                               | The password to use when creating a request with a challenge. To create a request without a challenge, do not set the [**ChallengePassword**](ix509certificaterequestpkcs10v3-challengepassword.md) property.<br/>                                                                                                                                      |
| [**EncryptionAlgorithm property**](ix509certificaterequestpkcs10v3-encryptionalgorithm.md)<br/>                           | The encryption algorithm used to encrypt the EKPUB and EKCERT values from the client.<br/>                                                                                                                                                                                                                                                               |
| [**EncryptionStrength property**](ix509certificaterequestpkcs10v3-encryptionstrength.md)<br/>                             | Identifies the bit length for the [**EncryptionAlgorithm**](ix509certificaterequestpkcs10v3-encryptionalgorithm.md) to use for encryption. If the **EncryptionAlgorithm** only supports one bit length, then you do not need to specify a value for the [**EncryptionStrength**](ix509certificaterequestpkcs10v3-encryptionstrength.md) property.<br/> |
| [**NameValuePairs property**](ix509certificaterequestpkcs10v3-namevaluepairs.md)<br/>                                     | A collection of name/value pairs of additional certificate property values.<br/>                                                                                                                                                                                                                                                                         |



 

 

 




