---
Description: 'Properties are used to associate a value with a certificate.'
ms.assetid: 'a6433416-fe77-4bb0-bd8e-9410a49ab861'
title: External Property Functions
---

# External Property Functions

Properties are used to associate a value with a certificate. Properties are never sent to or processed by a [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA), and they are not stored inside a certificate. Typically, they are associated with a certificate after the certificate is received from the CA and before it is saved in a store. The properties are saved in the store along with the certificate. CertEnroll.dll implements the [**ICertProperty**](icertproperty.md) interface and the following interfaces derived from **ICertProperty**:

-   [**ICertPropertyArchived**](icertpropertyarchived.md)
-   [**ICertPropertyArchivedKeyHash**](icertpropertyarchivedkeyhash.md)
-   [**ICertPropertyAutoEnroll**](icertpropertyautoenroll.md)
-   [**ICertPropertyBackedUp**](icertpropertybackedup.md)
-   [**ICertPropertyDescription**](icertpropertydescription.md)
-   [**ICertPropertyEnrollment**](icertpropertyenrollment.md)
-   [**ICertPropertyFriendlyName**](icertpropertyfriendlyname.md)
-   [**ICertPropertyKeyProvInfo**](icertpropertykeyprovinfo.md)
-   [**ICertPropertyRenewal**](icertpropertyrenewal.md)
-   [**ICertPropertyRequestOriginator**](icertpropertyrequestoriginator.md)
-   [**ICertPropertySHA1Hash**](icertpropertysha1hash.md)

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

In CertEnroll.dll, all of the objects derived from [**ICertProperty**](icertproperty.md) implement a [**SetValueOnCertificate**](icertproperty-setvalueoncertificate-method.md) method that you can use to associate a property with a certificate. Also, the [**IX509Enrollment**](ix509enrollment.md) object directly implements the [**CertificateFriendlyName**](ix509enrollment-certificatefriendlyname-property.md) and [**CertificateDescription**](ix509enrollment-certificatedescription-property.md) properties.

## GetPrivateKeyArchiveCertificate

The [**GetPrivateKeyArchiveCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa385605) function in Xenroll.dll retrieves the exchange certificate used to archive a [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly).

You can use the [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) object in CertEnroll.dll to create a request for a CA to archive your private key. You must retrieve an exchange certificate from the CA and use the [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly) contained in that certificate to encrypt the private key that you are submitting for archival. To specify or retrieve a CA exchange certificate, call the [**KeyArchivalCertificate**](ix509certificaterequestcmc-keyarchivalcertificate-property.md) property on that object.

## resetBlobProperties

The [**resetBlobProperties**](https://msdn.microsoft.com/library/windows/desktop/aa383210) function in Xenroll.dll removes the property collection from the certificate.

In CertEnroll.dll, all of the property objects derived from [**ICertProperty**](icertproperty.md) implement the [**RemoveFromCertificate**](icertproperty-removefromcertificate-method.md) property that you can use to disassociate a property from a certificate.

## SetPrivateKeyArchiveCertificate

The [**SetPrivateKeyArchiveCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa386032) function in Xenroll.dll specifies an exchange certificate used to archive a private key.

You can use the [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) object in CertEnroll.dll to create a request for a CA to archive your private key. You must retrieve an exchange certificate from the CA and use the public key contained in that certificate to encrypt the private key that you are submitting for archival. To specify or retrieve a CA exchange certificate, call the [**KeyArchivalCertificate**](ix509certificaterequestcmc-keyarchivalcertificate-property.md) property on that object.

## SetSignerCertificate

The [**SetSignerCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa386142) function in Xenroll.dll Specifies a signer certificate.

The [**ISignerCertificate**](isignercertificate.md) object in CertEnroll.dll can be used to sign a [*PKCS \#7*](https://msdn.microsoft.com/library/windows/desktop/ms721603), CMC, or self-signed [*certificate request*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-request-gly). You can initialize the object by using an existing signing certificate and associate it with a request by calling one of the following properties:

-   [**SignerCertificates**](ix509certificaterequestcmc-signercertificates-property.md) on [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md)
-   [**SignerCertificate**](ix509certificaterequestpkcs7-signercertificate-property.md) on [**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md)
-   [**SignerCertificate**](ix509certificaterequestcertificate-signercertificate-property.md) on [**IX509CertificateRequestCertificate**](ix509certificaterequestcertificate.md)

Also, if you initialize a CMC request from an inner request and a template or you initialize a PKCS \#7 request from an existing request, the signing certificate may be set.

## ThumbPrintWStr

The [**ThumbPrintWStr**](https://msdn.microsoft.com/library/windows/desktop/aa386148) function in Xenroll.dll specifies or retrieves the value of the certificate hash.

In CertEnroll.dll, you can use the [**ICertPropertySHA1Hash**](icertpropertysha1hash.md) object to retrieve a [*hash*](https://msdn.microsoft.com/library/windows/desktop/ms721586#-security-hash-gly) value ([*thumbprint*](https://msdn.microsoft.com/library/windows/desktop/ms721627#-security-thumbprint-gly)) created by calling the [**InitializeFromCertificate**](ix509certificaterequestpkcs7-initializefromcertificate-method.md) method.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> </dl>

 

 



