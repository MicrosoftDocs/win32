---
description: The CertEnroll.dll library implements five interfaces that can be used to create and manage a certificate request.
ms.assetid: f4630095-6ba2-46f7-8825-e7a5b1cb185a
title: Certificate Request Functions
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Request Functions

The CertEnroll.dll library implements five interfaces that can be used to create and manage a certificate request. Of these, the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) interface represents an abstract base object that defines method signatures inherited by the following four interfaces.

| Interface                                                                        | Description                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IX509CertificateRequestCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcertificate) | Enables you to create a certificate directly without applying to a [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA).<br/>                                                                                                            |
| [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc)                 | Represents a [*Certificate Management over CMS*](/windows/desktop/SecGloss/c-gly) (CMC) (Certificate Management Message over CMS) certificate request that can contain a nested PKCS \#10 request or another CMC request object.<br/> |
| [**IX509CertificateRequestPkcs7**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7)             | Represents a [*PKCS \#7*](/windows/desktop/SecGloss/p-gly) certificate message syntax (CMS) request object that must contain a nested PKCS \#10 request.<br/>                                                                                                         |
| [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10)           | Represents a PKCS \#10 certificate request. A PKCS \#10 request can be sent directly to a CA, or it can be wrapped by a PKCS \#7 or CMC request.<br/>                                                                                                                                                            |



 

You can use a certificate request object to initialize an [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object to enroll a client in a certificate hierarchy and install the certificate response returned by the CA.

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

The [**createFilePKCS10WStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-createfilepkcs10wstr) function in Xenroll.dll creates a base64-encoded PKCS \#10 certificate request and saves it in a file.

The CertEnroll.dll library does not directly implement functionality to write a request to a file. You can, however, retrieve a certificate request by calling the [**RawData**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-get_rawdata) property on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object and creating a custom function to copy the value to a file.

## createFileRequestWStr

The [**createFileRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-createfilerequestwstr) function in Xenroll.dll creates a PKCS \#7, PKCS \#10, or CMC certificate request and saves it in a file.

The CertEnroll.dll library does not directly implement functionality to write a request to a file. You can, however, retrieve a certificate request by calling the [**RawData**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-get_rawdata) property on the [**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest) object and creating a custom function to copy the value to a file.

## createPKCS10WStr

The [**createPKCS10WStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-createpkcs10wstr) function in Xenroll.dll creates a PKCS \#10 certificate request and copies it to a byte array.

You can use an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object to initialize a PKCS \#10 request from an existing request, an existing certificate, a [*private key*](/windows/desktop/SecGloss/p-gly), a [*public key*](/windows/desktop/SecGloss/p-gly), or a template.

## CreatePKCS7RequestFromRequest

The [**CreatePKCS7RequestFromRequest**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-createpkcs7requestfromrequest) function in Xenroll.dll creates a PKCS \#7 certificate request and copies it to a byte array.

You can use an [**IX509CertificateRequestPkcs7**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7) object to initialize a PKCS \#7 request from an existing request, an existing certificate, an inner request object, or a template.

## createRequestWStr

The [**createRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-createrequestwstr) function in Xenroll.dll creates a PKCS \#7, PKCS \#10, or CMC certificate request and copies it to a byte array.

To use the CertEnroll.dll library to create PKCS \#7, PKCS \#10, or CMC requests, you can create and initialize instances of the [**IX509CertificateRequestPkcs7**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7), [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10), or [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) objects.

## DeleteRequestCert

The [**DeleteRequestCert**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_deleterequestcert) function in Xenroll.dll specifies or retrieves a Boolean value that indicates whether a dummy certificate is removed after a certificate response has been installed.

The [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object in CertEnroll.dll automatically creates dummy certificates in the request store to temporarily save various certificate properties that are initialized during the enrollment process. After a certificate is issued by a CA, the properties are copied to the new certificate and the dummy certificate is deleted. The CertEnroll.dll library does not allow you to force a dummy certificate to remain after the certificate response has been installed.

## enumPendingRequestWStr

The [**enumPendingRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-enumpendingrequestwstr) function in Xenroll.dll retrieves a specified property value for a pending request.

The CertEnroll.dll library does not directly implement functionality to remove a pending certificate request.

## removePendingRequestWStr

The [**removePendingRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-removependingrequestwstr) function in Xenroll.dll removes a pending request from the request store.

The CertEnroll.dll library does not directly implement functionality to remove a pending certificate request.

## Reset

The [**Reset**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-reset) function in Xenroll.dll returns the Certificate Enrollment Control to an initial state.

You can achieve the same result by using Certenroll.dll to create a new request object of the required type.

## setPendingRequestInfoWStr

The [**setPendingRequestInfoWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-setpendingrequestinfowstr) function in Xenroll.dll specifies properties for the pending request.

The CertEnroll.dll library does not directly implement functionality to remove a pending certificate request. You can call the [**CAConfigString**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_caconfigstring) property on the [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object to retrieve a configuration string but only for an active enrollment object.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**ISignerCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificate)
</dt> <dt>

[**IX509CertificateRequest**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequest)
</dt> <dt>

[**IX509CertificateRequestCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcertificate)
</dt> <dt>

[**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc)
</dt> <dt>

[**IX509CertificateRequestPkcs7**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7)
</dt> <dt>

[**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10)
</dt> <dt>

[**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment)
</dt> </dl>

 

