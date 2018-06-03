---
Description: Properties are used to associate a value with a certificate.
ms.assetid: a6433416-fe77-4bb0-bd8e-9410a49ab861
title: External Property Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# External Property Functions

Properties are used to associate a value with a certificate. Properties are never sent to or processed by a [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA), and they are not stored inside a certificate. Typically, they are associated with a certificate after the certificate is received from the CA and before it is saved in a store. The properties are saved in the store along with the certificate. CertEnroll.dll implements the [**ICertProperty**](/windows/desktop/api/CertEnroll/nn-certenroll-icertproperty) interface and the following interfaces derived from **ICertProperty**:

-   [**ICertPropertyArchived**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyarchived)
-   [**ICertPropertyArchivedKeyHash**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyarchivedkeyhash)
-   [**ICertPropertyAutoEnroll**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyautoenroll)
-   [**ICertPropertyBackedUp**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertybackedup)
-   [**ICertPropertyDescription**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertydescription)
-   [**ICertPropertyEnrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyenrollment)
-   [**ICertPropertyFriendlyName**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyfriendlyname)
-   [**ICertPropertyKeyProvInfo**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertykeyprovinfo)
-   [**ICertPropertyRenewal**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyrenewal)
-   [**ICertPropertyRequestOriginator**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyrequestoriginator)
-   [**ICertPropertySHA1Hash**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertysha1hash)

Each of the following sections identifies a function exported by Xenroll.dll to manage external certificate properties. Each section also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists:

-   [addBlobPropertyToCertificateWStr](#addblobpropertytocertificatewstr)
-   [GetPrivateKeyArchiveCertificate](#getprivatekeyarchivecertificate)
-   [resetBlobProperties](#resetblobproperties)
-   [SetPrivateKeyArchiveCertificate](#setprivatekeyarchivecertificate)
-   [SetSignerCertificate](#setsignercertificate)
-   [ThumbPrintWStr](#thumbprintwstr)
-   [Related topics](#related-topics)

## addBlobPropertyToCertificateWStr

The [**addBlobPropertyToCertificateWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385510) function in Xenroll.dll adds a property to the certificate.

In CertEnroll.dll, all of the objects derived from [**ICertProperty**](/windows/desktop/api/CertEnroll/nn-certenroll-icertproperty) implement a [**SetValueOnCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-icertproperty-setvalueoncertificate) method that you can use to associate a property with a certificate. Also, the [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object directly implements the [**CertificateFriendlyName**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_certificatefriendlyname) and [**CertificateDescription**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-get_certificatedescription) properties.

## GetPrivateKeyArchiveCertificate

The [**GetPrivateKeyArchiveCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa385605) function in Xenroll.dll retrieves the exchange certificate used to archive a [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly).

You can use the [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) object in CertEnroll.dll to create a request for a CA to archive your private key. You must retrieve an exchange certificate from the CA and use the [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly) contained in that certificate to encrypt the private key that you are submitting for archival. To specify or retrieve a CA exchange certificate, call the [**KeyArchivalCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_keyarchivalcertificate) property on that object.

## resetBlobProperties

The [**resetBlobProperties**](https://msdn.microsoft.com/library/windows/desktop/aa383210) function in Xenroll.dll removes the property collection from the certificate.

In CertEnroll.dll, all of the property objects derived from [**ICertProperty**](/windows/desktop/api/CertEnroll/nn-certenroll-icertproperty) implement the [**RemoveFromCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-icertproperty-removefromcertificate) property that you can use to disassociate a property from a certificate.

## SetPrivateKeyArchiveCertificate

The [**SetPrivateKeyArchiveCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa386032) function in Xenroll.dll specifies an exchange certificate used to archive a private key.

You can use the [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) object in CertEnroll.dll to create a request for a CA to archive your private key. You must retrieve an exchange certificate from the CA and use the public key contained in that certificate to encrypt the private key that you are submitting for archival. To specify or retrieve a CA exchange certificate, call the [**KeyArchivalCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_keyarchivalcertificate) property on that object.

## SetSignerCertificate

The [**SetSignerCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa386142) function in Xenroll.dll Specifies a signer certificate.

The [**ISignerCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificate) object in CertEnroll.dll can be used to sign a [*PKCS \#7*](https://msdn.microsoft.com/library/windows/desktop/ms721603), CMC, or self-signed [*certificate request*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-request-gly). You can initialize the object by using an existing signing certificate and associate it with a request by calling one of the following properties:

-   [**SignerCertificates**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_signercertificates) on [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc)
-   [**SignerCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-get_signercertificate) on [**IX509CertificateRequestPkcs7**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7)
-   [**SignerCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcertificate-get_signercertificate) on [**IX509CertificateRequestCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcertificate)

Also, if you initialize a CMC request from an inner request and a template or you initialize a PKCS \#7 request from an existing request, the signing certificate may be set.

## ThumbPrintWStr

The [**ThumbPrintWStr**](https://msdn.microsoft.com/library/windows/desktop/aa386148) function in Xenroll.dll specifies or retrieves the value of the certificate hash.

In CertEnroll.dll, you can use the [**ICertPropertySHA1Hash**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertysha1hash) object to retrieve a [*hash*](https://msdn.microsoft.com/library/windows/desktop/ms721586#-security-hash-gly) value ([*thumbprint*](https://msdn.microsoft.com/library/windows/desktop/ms721627#-security-thumbprint-gly)) created by calling the [**InitializeFromCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-initializefromcertificate) method.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> </dl>

 

 



