---
Description: Functions exported by Xenroll.dll that can be used to manage a cryptographic provider.
ms.assetid: 4f6f353d-6b06-45b4-8808-56998d3727a4
title: Cryptographic Service Provider Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

The [**EnumAlgs**](https://msdn.microsoft.com/library/windows/desktop/aa385564) function in Xenroll.dll retrieves a cryptographic algorithm collection.

When using CertEnroll.dll, you can perform the following actions to retrieve information about the algorithms supported by a [*cryptographic service provider*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cryptographic-service-provider-gly) (CSP):

1.  Call the [**Request**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_request?branch=master) property on an existing [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**GetInnerRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest?branch=master) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) object.
4.  Call the [**PrivateKey**](https://msdn.microsoft.com/library/windows/desktop/aa387352) property on the PKCS \#10 request.
5.  Call the [**CspInformations**](/windows/win32/CertEnroll/nf-certenroll-ix509privatekey-get_cspinformations?branch=master) property on the [**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master) object retrieved from step 4.
6.  Call the [**CspAlgorithms**](/windows/win32/CertEnroll/nf-certenroll-icspinformation-get_cspalgorithms?branch=master) property on a specific [**ICspInformation**](/windows/win32/CertEnroll/nn-certenroll-icspinformation?branch=master) object in the [**ICspInformations**](/windows/win32/CertEnroll/nn-certenroll-icspinformations?branch=master) collection retrieved in step 5.

## enumContainersWStr

The [**enumContainersWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385565) function in Xenroll.dll retrieves a key container from the collection by index.

The CertEnroll.dll library does not directly implement this functionality.

## enumProvidersWStr

The [**enumProvidersWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385569) function in Xenroll.dll retrieves a CSP from the collection by index.

When using CertEnroll.dll, you can perform the following actions to retrieve the collection of cryptographic containers:

1.  Call the [**Request**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_request?branch=master) property on an existing [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**GetInnerRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest?branch=master) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) object.
4.  Call the [**PrivateKey**](https://msdn.microsoft.com/library/windows/desktop/aa387352) property on the PKCS \#10 request.
5.  Call the [**CspInformations**](/windows/win32/CertEnroll/nf-certenroll-ix509privatekey-get_cspinformations?branch=master) property on the [**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master) object retrieved from step 4.

## GetAlgNameWStr

The [**GetAlgNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385578) function in Xenroll.dll retrieves the name of a [*cryptographic algorithm*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cryptographic-algorithm-gly).

When using CertEnroll.dll, you can perform the following actions to retrieve the algorithm name:

1.  Call the [**Request**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_request?branch=master) property on an existing [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**GetInnerRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest?branch=master) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) object.
4.  Call the [**PrivateKey**](https://msdn.microsoft.com/library/windows/desktop/aa387352) property on the PKCS \#10 request.
5.  Call the [**Algorithm**](/windows/win32/CertEnroll/nf-certenroll-ix509privatekey-get_algorithm?branch=master) property on the [**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master) object to retrieve the algorithm object identifier.
6.  Call the [**FriendlyName**](/windows/win32/CertEnroll/nf-certenroll-iobjectid-get_friendlyname?branch=master) property on the [**IObjectId**](/windows/win32/CertEnroll/nn-certenroll-iobjectid?branch=master) interface to retrieve the algorithm display name.

## getProviderTypeWStr

The [**getProviderTypeWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385610) function in Xenroll.dll retrieves the cryptographic provider type.

When using CertEnroll.dll, you can perform the following actions to retrieve the provider type:

1.  Call the [**Request**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_request?branch=master) property on an existing [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**GetInnerRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest?branch=master) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) object.
4.  Call the [**PrivateKey**](https://msdn.microsoft.com/library/windows/desktop/aa387352) property on the PKCS \#10 request.
5.  Call the [**ProviderType**](/windows/win32/CertEnroll/nf-certenroll-ix509privatekey-get_providertype?branch=master) property on the [**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master) object retrieved from step 4.

## HashAlgID

The [**HashAlgID**](https://msdn.microsoft.com/library/windows/desktop/aa385621) function in Xenroll.dll retrieves an integer value that contains the ID of the algorithm used to sign a request.

When using CertEnroll.dll, you can perform the following actions to retrieve the hashing algorithm:

-   Retrieve an [**IX509SignatureInformation**](/windows/win32/CertEnroll/nn-certenroll-ix509signatureinformation?branch=master) interface by calling the [**SignatureInformation**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_signatureinformation?branch=master) property on a PKCS \#10 or CMC request or the [**SignerCertificate**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-get_signercertificate?branch=master) property on a [*PKCS \#7*](https://msdn.microsoft.com/library/windows/desktop/ms721603) request.
-   Call the [**HashAlgorithm**](/windows/win32/CertEnroll/nf-certenroll-ix509signatureinformation-get_hashalgorithm?branch=master) property on the signature information object to retrieve the hash algorithm object identifier.

## HashAlgorithmWStr

The [**HashAlgorithmWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385624) function in Xenroll.dll specifies or retrieves a string value that identifies the hashing algorithm used to sign a request.

When using CertEnroll.dll, you can perform the following actions to retrieve the hashing algorithm:

-   Retrieve an [**IX509SignatureInformation**](/windows/win32/CertEnroll/nn-certenroll-ix509signatureinformation?branch=master) interface by calling the [**SignatureInformation**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_signatureinformation?branch=master) property on a PKCS \#10 or CMC request or the [**SignerCertificate**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-get_signercertificate?branch=master) property on a PKCS \#7 request.
-   Call the [**HashAlgorithm**](/windows/win32/CertEnroll/nf-certenroll-ix509signatureinformation-get_hashalgorithm?branch=master) property on the signature information object to retrieve the hash algorithm object identifier.
-   Call the [**FriendlyName**](/windows/win32/CertEnroll/nf-certenroll-iobjectid-get_friendlyname?branch=master) property on the [**IObjectId**](/windows/win32/CertEnroll/nn-certenroll-iobjectid?branch=master) interface returned in step 2 to retrieve the algorithm display name.

## ProviderFlags

The [**ProviderFlags**](https://msdn.microsoft.com/library/windows/desktop/aa385654) function in Xenroll.dll specifies or retrieves the flags used when acquiring a handle to a CSP.

The CertEnroll.dll library does not map this function perfectly, but you can obtain rich property information from the enrollment object and the [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly). For more information, examine the properties exposed by the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) and [**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master) interfaces.

## ProviderNameWStr

The [**ProviderNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385657) function in Xenroll.dll specifies or retrieves the name of a CSP.

When using CertEnroll.dll, you can perform the following actions to retrieve the provider name:

1.  Call the [**Request**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_request?branch=master) property on an existing [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**GetInnerRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest?branch=master) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) object.
4.  Call the [**PrivateKey**](https://msdn.microsoft.com/library/windows/desktop/aa387352) property on the PKCS \#10 request.
5.  Call the [**ProviderName**](/windows/win32/CertEnroll/nf-certenroll-ix509privatekey-get_providername?branch=master) property on the [**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master) object retrieved from step 4.

## ProviderType

The [**ProviderType**](https://msdn.microsoft.com/library/windows/desktop/aa385659) function in Xenroll.dll specifies or retrieves an integer value that identifies the type of the CSP.

When using CertEnroll.dll, you can perform the following actions to retrieve the provider type:

1.  Call the [**Request**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_request?branch=master) property on an existing [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**GetInnerRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequest-getinnerrequest?branch=master) method on the request returned from step 1 to retrieve the innermost request.
3.  Call **QueryInterface** on the [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master) object returned from step 2 to cast to an [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) object.
4.  Call the [**PrivateKey**](https://msdn.microsoft.com/library/windows/desktop/aa387352) property on the PKCS \#10 request.
5.  Call the [**ProviderType**](/windows/win32/CertEnroll/nf-certenroll-ix509privatekey-get_providertype?branch=master) property on the [**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master) object retrieved from step 4.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**ICspAlgorithm**](/windows/win32/CertEnroll/nn-certenroll-icspalgorithm?branch=master)
</dt> <dt>

[**ICspAlgorithms**](/windows/win32/CertEnroll/nn-certenroll-icspalgorithms?branch=master)
</dt> <dt>

[**ICspInformation**](/windows/win32/CertEnroll/nn-certenroll-icspinformation?branch=master)
</dt> <dt>

[**ICspInformations**](/windows/win32/CertEnroll/nn-certenroll-icspinformations?branch=master)
</dt> <dt>

[**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master)
</dt> <dt>

[**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master)
</dt> </dl>

 

 



