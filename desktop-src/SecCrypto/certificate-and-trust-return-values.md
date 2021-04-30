---
description: Lists the certificate and certificate trust return values. These values are contained in the header file Winerror.h.
ms.assetid: f7d1bdcb-8e4f-493f-ad3c-9d4b9d21436b
title: Certificate and Trust Return Values
ms.topic: article
ms.date: 05/31/2018
---

# Certificate and Trust Return Values

The following table lists the certificate and certificate trust return values. These values are contained in the header file Winerror.h.



| Name                            | Description                                                                                                                    | Value      |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------|
| CERT\_E\_CRITICAL               | A certificate contains an unknown extension that is marked "critical."                                                         | 0x800B0105 |
| CERT\_E\_INVALID\_NAME          | The certificate has a name that is not valid. The name is either not included in the permitted list or is explicitly excluded. | 0x800B0114 |
| CERT\_E\_INVALID\_POLICY        | The certificate has a policy that is not valid.                                                                                | 0x800B0113 |
| CERT\_E\_ISSUERCHAINING         | A parent of a given certificate in fact did not issue that child certificate.                                                  | 0x800B0107 |
| CERT\_E\_MALFORMED              | A certificate is missing or has an empty value for an important field, such as a subject or issuer name.                       | 0x800B0108 |
| CERT\_E\_PATHLENCONST           | A path length constraint in the certification chain has been violated.                                                         | 0x800B0104 |
| CERT\_E\_UNTRUSTEDCA            | A certification chain processed correctly, but one of the CA certificates is not trusted by the policy provider.               | 0x800B0112 |
| CRYPT\_E\_NO\_REVOCATION\_CHECK | The revocation function was unable to check revocation for the certificate.                                                    | 0x80092012 |
| TRUST\_E\_BAD\_DIGEST           | The digital signature of the object did not verify.                                                                            | 0x80096010 |
| TRUST\_E\_BASIC\_CONSTRAINTS    | The basic constraint extension of a certificate has not been observed.                                                         | 0x80096019 |
| TRUST\_E\_CERT\_SIGNATURE       | The signature of the certificate cannot be verified.                                                                           | 0x80096004 |
| TRUST\_E\_COUNTER\_SIGNER       | One of the counter signatures was not valid.                                                                                   | 0x80096003 |
| TRUST\_E\_EXPLICIT\_DISTRUST    | The certificate was explicitly marked as untrusted by the user.                                                                | 0x800B0111 |
| TRUST\_E\_FINANCIAL\_CRITERIA   | The certificate does not meet or contain the Authenticode financial extensions.                                                | 0x8009601E |
| TRUST\_E\_NO\_SIGNER\_CERT      | The certificate for the signer of the message is not valid or not found.                                                       | 0x80096002 |
| TRUST\_E\_SYSTEM\_ERROR         | A system-level error occurred while verifying trust.                                                                           | 0x80096001 |
| TRUST\_E\_TIME\_STAMP           | The time stamp signature or certificate could not be verified or is malformed.                                                 | 0x80096005 |



 

 

 



