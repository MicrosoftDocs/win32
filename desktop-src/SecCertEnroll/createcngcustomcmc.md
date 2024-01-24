---
description: Creates a CMC request object from an inner nested PKCS \#10 request.
ms.assetid: 8a0dc078-22ca-4bff-9cc0-46823912d3da
title: createCNGCustomCMC
ms.topic: article
ms.date: 05/31/2018
---

# createCNGCustomCMC

The createCNGCustomCMC sample creates a CMC request object from an inner nested PKCS \#10 request. The inner request is created by using an asymmetric [*private key*](/windows/desktop/SecGloss/p-gly). The private key is created by using the Cryptography API: Next Generation (CNG) cryptographic provider and the algorithm specified on the command line. Custom options such as export policy and key protection level are also set on the private key.

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\createCNGCustomCMC folder.

## Discussion

The createCNGCustomCMC sample:

1.  Processes the following command line arguments:
    -   The name of a CNG [*cryptographic service provider*](/windows/desktop/SecGloss/c-gly) (CSP).
    -   The name of the algorithm used to generate an asymmetric private key.
    -   The name of the algorithm used to [*hash*](/windows/desktop/SecGloss/h-gly) the [*certificate request*](/windows/desktop/SecGloss/c-gly).
    -   An output file in which to save the certificate request.
    -   An optional string (AlternateSignature) which, if present, specifies that a discrete rather than a combined signature algorithm be used. For more information, see the [**AlternateSignatureAlgorithm**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-get_alternatesignaturealgorithm) property.
2.  Creates an [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object and sets the following properties:
    -   [**LegacyCsp**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_legacycsp)
    -   [**ProviderName**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_providername)
    -   [**Algorithm**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_algorithm)
    -   [**KeyProtection**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_keyprotection)
    -   [**ExportPolicy**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_exportpolicy)
3.  Creates an asymmetric private key.
4.  Creates an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object and initializes it by using the private key.
5.  Creates an [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) object and initializes it by using the PKCS \#10 request object created in step 4.
6.  Sets the alternate signature algorithm flag to **VARIANT\_TRUE** or **VARIANT\_FALSE** depending on whether an alternate signature string is specified on the command line. For more information, see [**AlternateSignatureAlgorithm**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-get_alternatesignaturealgorithm).
7.  Creates a [*hashing algorithm*](/windows/desktop/SecGloss/h-gly) [*object identifier*](/windows/desktop/SecGloss/o-gly) (OID) from the algorithm name specified on the command line and sets the OID on the CMC request object.
8.  Signs the certificate request and encodes it by using [*Distinguished Encoding Rules*](/windows/desktop/SecGloss/d-gly) (DER).
9.  Retrieves a string that contains the encoded CMC certificate request and saves it to a file. The EncodeToFileW function is defined in EnrollCommon.cpp.

## Related topics

<dl> <dt>

[CMC Request](cmc-request.md)
</dt> <dt>

[PKCS \#10 Request](pkcs--10-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> <dt>

[**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey)
</dt> </dl>

 

 
