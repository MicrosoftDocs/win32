---
Description: Properties are used to associate a value with a certificate.
ms.assetid: a6433416-fe77-4bb0-bd8e-9410a49ab861
title: External Property Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# External Property Functions

Properties are used to associate a value with a certificate. Properties are never sent to or processed by a [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA), and they are not stored inside a certificate. Typically, they are associated with a certificate after the certificate is received from the CA and before it is saved in a store. The properties are saved in the store along with the certificate. CertEnroll.dll implements the [**ICertProperty**](/windows/win32/CertEnroll/nn-certenroll-icertproperty?branch=master) interface and the following interfaces derived from **ICertProperty**:

-   [**ICertPropertyArchived**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyarchived?branch=master)
-   [**ICertPropertyArchivedKeyHash**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyarchivedkeyhash?branch=master)
-   [**ICertPropertyAutoEnroll**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyautoenroll?branch=master)
-   [**ICertPropertyBackedUp**](/windows/win32/CertEnroll/nn-certenroll-icertpropertybackedup?branch=master)
-   [**ICertPropertyDescription**](/windows/win32/CertEnroll/nn-certenroll-icertpropertydescription?branch=master)
-   [**ICertPropertyEnrollment**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyenrollment?branch=master)
-   [**ICertPropertyFriendlyName**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyfriendlyname?branch=master)
-   [**ICertPropertyKeyProvInfo**](/windows/win32/CertEnroll/nn-certenroll-icertpropertykeyprovinfo?branch=master)
-   [**ICertPropertyRenewal**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyrenewal?branch=master)
-   [**ICertPropertyRequestOriginator**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyrequestoriginator?branch=master)
-   [**ICertPropertySHA1Hash**](/windows/win32/CertEnroll/nn-certenroll-icertpropertysha1hash?branch=master)

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

In CertEnroll.dll, all of the objects derived from [**ICertProperty**](/windows/win32/CertEnroll/nn-certenroll-icertproperty?branch=master) implement a [**SetValueOnCertificate**](/windows/win32/CertEnroll/nf-certenroll-icertproperty-setvalueoncertificate?branch=master) method that you can use to associate a property with a certificate. Also, the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object directly implements the [**CertificateFriendlyName**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_certificatefriendlyname?branch=master) and [**CertificateDescription**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_certificatedescription?branch=master) properties.

## GetPrivateKeyArchiveCertificate

The [**GetPrivateKeyArchiveCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa385605) function in Xenroll.dll retrieves the exchange certificate used to archive a [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly).

You can use the [**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master) object in CertEnroll.dll to create a request for a CA to archive your private key. You must retrieve an exchange certificate from the CA and use the [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly) contained in that certificate to encrypt the private key that you are submitting for archival. To specify or retrieve a CA exchange certificate, call the [**KeyArchivalCertificate**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_keyarchivalcertificate?branch=master) property on that object.

## resetBlobProperties

The [**resetBlobProperties**](https://msdn.microsoft.com/library/windows/desktop/aa383210) function in Xenroll.dll removes the property collection from the certificate.

In CertEnroll.dll, all of the property objects derived from [**ICertProperty**](/windows/win32/CertEnroll/nn-certenroll-icertproperty?branch=master) implement the [**RemoveFromCertificate**](/windows/win32/CertEnroll/nf-certenroll-icertproperty-removefromcertificate?branch=master) property that you can use to disassociate a property from a certificate.

## SetPrivateKeyArchiveCertificate

The [**SetPrivateKeyArchiveCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa386032) function in Xenroll.dll specifies an exchange certificate used to archive a private key.

You can use the [**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master) object in CertEnroll.dll to create a request for a CA to archive your private key. You must retrieve an exchange certificate from the CA and use the public key contained in that certificate to encrypt the private key that you are submitting for archival. To specify or retrieve a CA exchange certificate, call the [**KeyArchivalCertificate**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_keyarchivalcertificate?branch=master) property on that object.

## SetSignerCertificate

The [**SetSignerCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa386142) function in Xenroll.dll Specifies a signer certificate.

The [**ISignerCertificate**](/windows/win32/CertEnroll/nn-certenroll-isignercertificate?branch=master) object in CertEnroll.dll can be used to sign a [*PKCS \#7*](https://msdn.microsoft.com/library/windows/desktop/ms721603), CMC, or self-signed [*certificate request*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-request-gly). You can initialize the object by using an existing signing certificate and associate it with a request by calling one of the following properties:

-   [**SignerCertificates**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_signercertificates?branch=master) on [**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master)
-   [**SignerCertificate**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-get_signercertificate?branch=master) on [**IX509CertificateRequestPkcs7**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7?branch=master)
-   [**SignerCertificate**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestcertificate-get_signercertificate?branch=master) on [**IX509CertificateRequestCertificate**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcertificate?branch=master)

Also, if you initialize a CMC request from an inner request and a template or you initialize a PKCS \#7 request from an existing request, the signing certificate may be set.

## ThumbPrintWStr

The [**ThumbPrintWStr**](https://msdn.microsoft.com/library/windows/desktop/aa386148) function in Xenroll.dll specifies or retrieves the value of the certificate hash.

In CertEnroll.dll, you can use the [**ICertPropertySHA1Hash**](/windows/win32/CertEnroll/nn-certenroll-icertpropertysha1hash?branch=master) object to retrieve a [*hash*](https://msdn.microsoft.com/library/windows/desktop/ms721586#-security-hash-gly) value ([*thumbprint*](https://msdn.microsoft.com/library/windows/desktop/ms721627#-security-thumbprint-gly)) created by calling the [**InitializeFromCertificate**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-initializefromcertificate?branch=master) method.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> </dl>

 

 



