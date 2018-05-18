---
Description: 'The CertEnroll.dll library implements five interfaces that can be used to create and manage a certificate request.'
ms.assetid: 'f4630095-6ba2-46f7-8825-e7a5b1cb185a'
title: Certificate Request Functions
---

# Certificate Request Functions

The CertEnroll.dll library implements five interfaces that can be used to create and manage a certificate request. Of these, the [**IX509CertificateRequest**](ix509certificaterequest.md) interface represents an abstract base object that defines method signatures inherited by the following four interfaces.

| Interface                                                                        | Description                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IX509CertificateRequestCertificate**](ix509certificaterequestcertificate.md) | Enables you to create a certificate directly without applying to a [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA).<br/>                                                                                                            |
| [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md)                 | Represents a [*Certificate Management over CMS*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-management-over-cms-gly) (CMC) (Certificate Management Message over CMS) certificate request that can contain a nested PKCS \#10 request or another CMC request object.<br/> |
| [**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md)             | Represents a [*PKCS \#7*](https://msdn.microsoft.com/library/windows/desktop/ms721603) certificate message syntax (CMS) request object that must contain a nested PKCS \#10 request.<br/>                                                                                                         |
| [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md)           | Represents a PKCS \#10 certificate request. A PKCS \#10 request can be sent directly to a CA, or it can be wrapped by a PKCS \#7 or CMC request.<br/>                                                                                                                                                            |



 

You can use a certificate request object to initialize an [**IX509Enrollment**](ix509enrollment.md) object to enroll a client in a certificate hierarchy and install the certificate response returned by the CA.

Each of the following sections identifies a function exported by Xenroll.dll to create, enumerate, or delete certificate requests. Each section also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists:

-   [createFilePKCS10WStr](#createfilepkcs10wstr)
-   [createFileRequestWStr](#createfilerequestwstr)
-   [createPKCS10WStr](#createpkcs10wstr)
-   [CreatePKCS7RequestFromRequest](#createpkcs7requestfromrequest)
-   [createRequestWStr](#createrequestwstr)
-   [DeleteRequestCert](#deleterequestcert)
-   [enumPendingRequestWStr](#enumpendingrequestwstr)
-   [removePendingRequestWStr](#removependingrequestwstr)
-   [Reset](#reset)
-   [setPendingRequestInfoWStr](#setpendingrequestinfowstr)
-   [Related topics](#related-topics)

## createFilePKCS10WStr

The [**createFilePKCS10WStr**](https://msdn.microsoft.com/library/windows/desktop/aa385537) function in Xenroll.dll creates a base64-encoded PKCS \#10 certificate request and saves it in a file.

The CertEnroll.dll library does not directly implement functionality to write a request to a file. You can, however, retrieve a certificate request by calling the [**RawData**](ix509certificaterequest-rawdata-property.md) property on the [**IX509CertificateRequest**](ix509certificaterequest.md) object and creating a custom function to copy the value to a file.

## createFileRequestWStr

The [**createFileRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385538) function in Xenroll.dll creates a PKCS \#7, PKCS \#10, or CMC certificate request and saves it in a file.

The CertEnroll.dll library does not directly implement functionality to write a request to a file. You can, however, retrieve a certificate request by calling the [**RawData**](ix509certificaterequest-rawdata-property.md) property on the [**IX509CertificateRequest**](ix509certificaterequest.md) object and creating a custom function to copy the value to a file.

## createPKCS10WStr

The [**createPKCS10WStr**](https://msdn.microsoft.com/library/windows/desktop/aa385542) function in Xenroll.dll creates a PKCS \#10 certificate request and copies it to a byte array.

You can use an [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) object to initialize a PKCS \#10 request from an existing request, an existing certificate, a [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603), a [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly), or a template.

## CreatePKCS7RequestFromRequest

The [**CreatePKCS7RequestFromRequest**](https://msdn.microsoft.com/library/windows/desktop/aa385544) function in Xenroll.dll creates a PKCS \#7 certificate request and copies it to a byte array.

You can use an [**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md) object to initialize a PKCS \#7 request from an existing request, an existing certificate, an inner request object, or a template.

## createRequestWStr

The [**createRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385546) function in Xenroll.dll creates a PKCS \#7, PKCS \#10, or CMC certificate request and copies it to a byte array.

To use the CertEnroll.dll library to create PKCS \#7, PKCS \#10, or CMC requests, you can create and initialize instances of the [**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md), [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md), or [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) objects.

## DeleteRequestCert

The [**DeleteRequestCert**](https://msdn.microsoft.com/library/windows/desktop/aa385548) function in Xenroll.dll specifies or retrieves a Boolean value that indicates whether a dummy certificate is removed after a certificate response has been installed.

The [**IX509Enrollment**](ix509enrollment.md) object in CertEnroll.dll automatically creates dummy certificates in the request store to temporarily save various certificate properties that are initialized during the enrollment process. After a certificate is issued by a CA, the properties are copied to the new certificate and the dummy certificate is deleted. The CertEnroll.dll library does not allow you to force a dummy certificate to remain after the certificate response has been installed.

## enumPendingRequestWStr

The [**enumPendingRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385568) function in Xenroll.dll retrieves a specified property value for a pending request.

The CertEnroll.dll library does not directly implement functionality to remove a pending certificate request.

## removePendingRequestWStr

The [**removePendingRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385668) function in Xenroll.dll removes a pending request from the request store.

The CertEnroll.dll library does not directly implement functionality to remove a pending certificate request.

## Reset

The [**Reset**](https://msdn.microsoft.com/library/windows/desktop/aa385688) function in Xenroll.dll returns the Certificate Enrollment Control to an initial state.

You can achieve the same result by using Certenroll.dll to create a new request object of the required type.

## setPendingRequestInfoWStr

The [**setPendingRequestInfoWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385919) function in Xenroll.dll specifies properties for the pending request.

The CertEnroll.dll library does not directly implement functionality to remove a pending certificate request. You can call the [**CAConfigString**](ix509enrollment-caconfigstring-property.md) property on the [**IX509Enrollment**](ix509enrollment.md) object to retrieve a configuration string but only for an active enrollment object.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**ISignerCertificate**](isignercertificate.md)
</dt> <dt>

[**IX509CertificateRequest**](ix509certificaterequest.md)
</dt> <dt>

[**IX509CertificateRequestCertificate**](ix509certificaterequestcertificate.md)
</dt> <dt>

[**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md)
</dt> <dt>

[**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md)
</dt> <dt>

[**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md)
</dt> <dt>

[**IX509Enrollment**](ix509enrollment.md)
</dt> </dl>

 

 




