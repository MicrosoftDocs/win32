---
description: Functions exported by Xenroll.dll that can be used to manage a cryptographic provider.
ms.assetid: 4f6f353d-6b06-45b4-8808-56998d3727a4
title: Cryptographic Service Provider Functions
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Service Provider Functions

Each of the following sections identifies a function exported by Xenroll.dll that can be used to manage a cryptographic provider. Each topic also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists:

-   [EnumAlgs](#enumalgs)
-   [enumContainersWStr](#enumcontainerswstr)
-   [enumProvidersWStr](#enumproviderswstr)
-   [GetAlgNameWStr](#getalgnamewstr)
-   [getProviderTypeWStr](#getprovidertypewstr)
-   [HashAlgID](#hashalgid)
-   [HashAlgorithmWStr](#hashalgorithmwstr)
-   [ProviderFlags](#providerflags)
-   [ProviderNameWStr](#providernamewstr)
-   [ProviderType](#getprovidertypewstr)
-   [Related topics](#related-topics)

## EnumAlgs

The [**EnumAlgs**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-enumalgs) function in Xenroll.dll retrieves a cryptographic algorithm collection.

When using CertEnroll.dll, you can perform the following actions to retrieve information about the algorithms supported by a [*cryptographic service provider*](/windows/desktop/SecGloss/c-gly) (CSP):

1.  Call the [**Request**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_request) property on an existing [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object.
2.  Call the [**GetInnerRequest**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.
4.  Call the [**PrivateKey**](/windows/desktop/SecCrypto/privatekey) property on the PKCS \#10 request.
5.  Call the [**CspInformations**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_cspinformations) property on the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object retrieved from step 4.
6.  Call the [**CspAlgorithms**](/windows/desktop/api/CertEnroll/nf-certenroll-icspinformation-get_cspalgorithms) property on a specific [**ICspInformation**](/windows/desktop/api/CertEnroll/nn-certenroll-icspinformation) object in the [**ICspInformations**](/windows/desktop/api/CertEnroll/nn-certenroll-icspinformations) collection retrieved in step 5.

## enumContainersWStr

The [**enumContainersWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-enumcontainerswstr) function in Xenroll.dll retrieves a key container from the collection by index.

The CertEnroll.dll library does not directly implement this functionality.

## enumProvidersWStr

The [**enumProvidersWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-enumproviderswstr) function in Xenroll.dll retrieves a CSP from the collection by index.

When using CertEnroll.dll, you can perform the following actions to retrieve the collection of cryptographic containers:

1.  Call the [**Request**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_request) property on an existing [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object.
2.  Call the [**GetInnerRequest**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.
4.  Call the [**PrivateKey**](/windows/desktop/SecCrypto/privatekey) property on the PKCS \#10 request.
5.  Call the [**CspInformations**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_cspinformations) property on the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object retrieved from step 4.

## GetAlgNameWStr

The [**GetAlgNameWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-getalgnamewstr) function in Xenroll.dll retrieves the name of a [*cryptographic algorithm*](/windows/desktop/SecGloss/c-gly).

When using CertEnroll.dll, you can perform the following actions to retrieve the algorithm name:

1.  Call the [**Request**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_request) property on an existing [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object.
2.  Call the [**GetInnerRequest**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.
4.  Call the [**PrivateKey**](/windows/desktop/SecCrypto/privatekey) property on the PKCS \#10 request.
5.  Call the [**Algorithm**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_algorithm) property on the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object to retrieve the algorithm object identifier.
6.  Call the [**FriendlyName**](/windows/desktop/api/CertEnroll/nf-certenroll-iobjectid-get_friendlyname) property on the [**IObjectId**](/windows/desktop/api/CertEnroll/nn-certenroll-iobjectid) interface to retrieve the algorithm display name.

## getProviderTypeWStr

The [**getProviderTypeWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-getprovidertypewstr) function in Xenroll.dll retrieves the cryptographic provider type.

When using CertEnroll.dll, you can perform the following actions to retrieve the provider type:

1.  Call the [**Request**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_request) property on an existing [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object.
2.  Call the [**GetInnerRequest**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.
4.  Call the [**PrivateKey**](/windows/desktop/SecCrypto/privatekey) property on the PKCS \#10 request.
5.  Call the [**ProviderType**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_providertype) property on the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object retrieved from step 4.

## HashAlgID

The [**HashAlgID**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-get_hashalgid) function in Xenroll.dll retrieves an integer value that contains the ID of the algorithm used to sign a request.

When using CertEnroll.dll, you can perform the following actions to retrieve the hashing algorithm:

-   Retrieve an [**IX509SignatureInformation**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509signatureinformation) interface by calling the [**SignatureInformation**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_signatureinformation) property on a PKCS \#10 or CMC request or the [**SignerCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-get_signercertificate) property on a [*PKCS \#7*](/windows/desktop/SecGloss/p-gly) request.
-   Call the [**HashAlgorithm**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509signatureinformation-get_hashalgorithm) property on the signature information object to retrieve the hash algorithm object identifier.

## HashAlgorithmWStr

The [**HashAlgorithmWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_hashalgorithmwstr) function in Xenroll.dll specifies or retrieves a string value that identifies the hashing algorithm used to sign a request.

When using CertEnroll.dll, you can perform the following actions to retrieve the hashing algorithm:

-   Retrieve an [**IX509SignatureInformation**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509signatureinformation) interface by calling the [**SignatureInformation**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_signatureinformation) property on a PKCS \#10 or CMC request or the [**SignerCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-get_signercertificate) property on a PKCS \#7 request.
-   Call the [**HashAlgorithm**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509signatureinformation-get_hashalgorithm) property on the signature information object to retrieve the hash algorithm object identifier.
-   Call the [**FriendlyName**](/windows/desktop/api/CertEnroll/nf-certenroll-iobjectid-get_friendlyname) property on the [**IObjectId**](/windows/desktop/api/CertEnroll/nn-certenroll-iobjectid) interface returned in step 2 to retrieve the algorithm display name.

## ProviderFlags

The [**ProviderFlags**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_providerflags) function in Xenroll.dll specifies or retrieves the flags used when acquiring a handle to a CSP.

The CertEnroll.dll library does not map this function perfectly, but you can obtain rich property information from the enrollment object and the [*private key*](/windows/desktop/SecGloss/p-gly). For more information, examine the properties exposed by the [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) and [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) interfaces.

## ProviderNameWStr

The [**ProviderNameWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_providernamewstr) function in Xenroll.dll specifies or retrieves the name of a CSP.

When using CertEnroll.dll, you can perform the following actions to retrieve the provider name:

1.  Call the [**Request**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_request) property on an existing [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object.
2.  Call the [**GetInnerRequest**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.
4.  Call the [**PrivateKey**](/windows/desktop/SecCrypto/privatekey) property on the PKCS \#10 request.
5.  Call the [**ProviderName**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_providername) property on the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object retrieved from step 4.

## ProviderType

The [**ProviderType**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_providertype) function in Xenroll.dll specifies or retrieves an integer value that identifies the type of the CSP.

When using CertEnroll.dll, you can perform the following actions to retrieve the provider type:

1.  Call the [**Request**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_request) property on an existing [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object.
2.  Call the [**GetInnerRequest**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.
4.  Call the [**PrivateKey**](/windows/desktop/SecCrypto/privatekey) property on the PKCS \#10 request.
5.  Call the [**ProviderType**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509privatekey-get_providertype) property on the [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey) object retrieved from step 4.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**ICspAlgorithm**](/windows/desktop/api/CertEnroll/nn-certenroll-icspalgorithm)
</dt> <dt>

[**ICspAlgorithms**](/windows/desktop/api/CertEnroll/nn-certenroll-icspalgorithms)
</dt> <dt>

[**ICspInformation**](/windows/desktop/api/CertEnroll/nn-certenroll-icspinformation)
</dt> <dt>

[**ICspInformations**](/windows/desktop/api/CertEnroll/nn-certenroll-icspinformations)
</dt> <dt>

[**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment)
</dt> <dt>

[**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey)
</dt> </dl>

 

 
