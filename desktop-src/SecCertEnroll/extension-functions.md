---
Description: The X.509 version 3 certificate format identifies multiple extensions that can be added to a certificate to provide enhanced information about key usage, certificate policies and constraints, alternative name forms, and more.
ms.assetid: d53107b7-a153-41cf-9876-1d28aaf99816
title: Extension Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Extension Functions

The [*X.509*](https://msdn.microsoft.com/library/windows/desktop/ms721636#-security-x-509-gly) version 3 certificate format identifies multiple extensions that can be added to a certificate to provide enhanced information about key usage, certificate policies and constraints, alternative name forms, and more.

CertEnroll.dll implements the following interfaces to manage certificate extensions:

-   [**IX509Extension**](/windows/win32/CertEnroll/nn-certenroll-ix509extension?branch=master)
-   [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master)
-   [**IX509ExtensionAlternativeNames**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionalternativenames?branch=master)
-   [**IX509ExtensionAuthorityKeyIdentifier**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionauthoritykeyidentifier?branch=master)
-   [**IX509ExtensionBasicConstraints**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionbasicconstraints?branch=master)
-   [**IX509ExtensionCertificatePolicies**](/windows/win32/CertEnroll/nn-certenroll-ix509extensioncertificatepolicies?branch=master)
-   [**IX509ExtensionEnhancedKeyUsage**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionenhancedkeyusage?branch=master)
-   [**IX509ExtensionKeyUsage**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionkeyusage?branch=master)
-   [**IX509ExtensionMSApplicationPolicies**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionmsapplicationpolicies?branch=master)
-   [**IX509ExtensionSmimeCapabilities**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionsmimecapabilities?branch=master)
-   [**IX509ExtensionSubjectKeyIdentifier**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier?branch=master)
-   [**IX509ExtensionTemplate**](/windows/win32/CertEnroll/nn-certenroll-ix509extensiontemplate?branch=master)
-   [**IX509ExtensionTemplateName**](/windows/win32/CertEnroll/nn-certenroll-ix509extensiontemplatename?branch=master)

Each of the following sections discusses a function exported by Xenroll.dll to manage certificate extensions. Each section also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists:

-   [AddCertTypeToRequestWStr](#addcerttypetorequestwstr)
-   [AddCertTypeToRequestWStrEx](#addcerttypetorequestwstrex)
-   [AddExtensionsToRequest](#addextensionstorequest)
-   [addExtensionToRequestWStr](#addextensiontorequestwstr)
-   [EnableSMIMECapabilities](#enablesmimecapabilities)
-   [IncludeSubjectKeyID](#includesubjectkeyid)
-   [resetExtensions](#resetextensions)
-   [Related topics](#related-topics)

## AddCertTypeToRequestWStr

The [**AddCertTypeToRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385512) function in Xenroll.dll adds a certificate template, by name, to a request.

Using CertEnroll.dll, the preferred method to incorporate a template into a certificate request is to use the [**InitializeFromTemplateName**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-initializefromtemplatename?branch=master) method on a PKCS\#10 or [*PKCS ) request object or the [**InitializeFromInnerRequestTemplateName**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestcmc-initializefrominnerrequesttemplatename?branch=master) method on a CMC request.

If a specific template is not available on the client but is expected to be understood by the [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA), you can use the [**IX509ExtensionTemplateName**](/windows/win32/CertEnroll/nn-certenroll-ix509extensiontemplatename?branch=master) interface to add a version 1 template or you can use the [**IX509ExtensionTemplate**](/windows/win32/CertEnroll/nn-certenroll-ix509extensiontemplate?branch=master) interface to add a version 2 template to a certificate request. For example, to add a version 1 template, perform the following actions:

1.  Create an [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) object.
2.  Create an [**IX509ExtensionTemplateName**](/windows/win32/CertEnroll/nn-certenroll-ix509extensiontemplatename?branch=master) object and call the [**InitializeEncode**](/windows/win32/CertEnroll/nf-certenroll-ix509extensiontemplatename-initializeencode?branch=master) method, specifying the template name.
3.  Add the extension created to the [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) collection by calling the [**Add**](/windows/win32/CertEnroll/nf-certenroll-ix509extensions-add?branch=master) method.
4.  Create an [**IX509AttributeExtensions**](/windows/win32/CertEnroll/nn-certenroll-ix509attributeextensions?branch=master) object and call the [**InitializeEncode**](/windows/win32/CertEnroll/nf-certenroll-ix509attributeextensions-initializeencode?branch=master) method, specifying the [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) collection on input.
5.  Retrieve an [**ICryptAttributes**](/windows/win32/CertEnroll/nn-certenroll-icryptattributes?branch=master) collection object by calling the [**CryptAttributes**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_cryptattributes?branch=master) property on an existing [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) or [**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master) request object.

## AddCertTypeToRequestWStrEx

The [**AddCertTypeToRequestWStrEx**](https://msdn.microsoft.com/library/windows/desktop/aa385513) function in Xenroll.dll adds a certificate template to a request by name, object identifier, and version.

For information about how to use CertEnroll.dll to incorporate template information in a request, see AddCertTypeToRequestWStr.

## AddExtensionsToRequest

The [**AddExtensionsToRequest**](https://msdn.microsoft.com/library/windows/desktop/aa385516) function in Xenroll.dll adds a collection of extensions to a request.

In CertEnroll.dll, extensions are added to the attributes collection of a CMC or a PKCS \#10 request. To add extensions, perform the following actions:

1.  Create an [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) object.
2.  Create an [**IX509Extension**](/windows/win32/CertEnroll/nn-certenroll-ix509extension?branch=master) object and call the [**Initialize**](/windows/win32/CertEnroll/nf-certenroll-ix509extension-initialize?branch=master) method to create an extension from an object identifier and extension value or use any of the interfaces listed earlier to define one of the more common extensions.
3.  Add each new extension created in the preceding step to the [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) collection by calling the [**Add**](/windows/win32/CertEnroll/nf-certenroll-ix509extensions-add?branch=master) method.

## addExtensionToRequestWStr

The [**addExtensionToRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385518) function in Xenroll.dll adds a specific extension to the request.

In CertEnroll.dll, a specific extension must be defined and added to an extensions collection before the extension collection is added to the attributes collection of a CMC or a PKCS \#10 request. For more information see the AddExtensionsToRequest discussion above.

## EnableSMIMECapabilities

The [**EnableSMIMECapabilities**](https://msdn.microsoft.com/library/windows/desktop/aa385560) function in Xenroll.dll specifies or retrieves a Boolean value that indicates whether to add the **SMIMECapabilities** extension to the request.

You can call the [**SmimeCapabilities**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_smimecapabilities?branch=master) property on the [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) object to automatically add an [**IX509ExtensionSmimeCapabilities**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionsmimecapabilities?branch=master) object to the request before encoding.

## IncludeSubjectKeyID

The [**IncludeSubjectKeyID**](https://msdn.microsoft.com/library/windows/desktop/aa385628) function in Xenroll.dll specifies or retrieves a Boolean value that indicates whether to add the **SubjectKeyIdentifier** extension to the request.

By default, the **SubjectKeyIdentifier** extension is created when the [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) request object is initialized. You can override this behavior by calling the [**SuppressOids**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_suppressoids?branch=master) property.

If you have a [*public/private key pair*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-private-key-pair-gly), you can also use the [**IX509ExtensionSubjectKeyIdentifier**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier?branch=master) interface in CertEnroll.dll to add a **SubjectKeyIdentifier** extension to a certificate request by performing the following actions:

1.  Create an [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) object.
2.  Create an [**IX509ExtensionSubjectKeyIdentifier**](/windows/win32/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier?branch=master) object and call the [**InitializeEncode**](/windows/win32/CertEnroll/nf-certenroll-ix509extensionsubjectkeyidentifier-initializeencode?branch=master) method, specifying a string that contains the identifier. Typically, this is a 20-byte SHA-1 hash of the [*public key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-public-key-gly) contained in the CA signing certificate.
3.  Add the extension created to the [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) collection by calling the [**Add**](/windows/win32/CertEnroll/nf-certenroll-ix509extensions-add?branch=master) method.
4.  Create an [**IX509AttributeExtensions**](/windows/win32/CertEnroll/nn-certenroll-ix509attributeextensions?branch=master) object and call the [**InitializeEncode**](/windows/win32/CertEnroll/nf-certenroll-ix509attributeextensions-initializeencode?branch=master) method, specifying the [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) collection on input.
5.  Retrieve an [**ICryptAttributes**](/windows/win32/CertEnroll/nn-certenroll-icryptattributes?branch=master) collection object by calling the [**CryptAttributes**](/windows/win32/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_cryptattributes?branch=master) property on an existing [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) or [**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master) request object.

## resetExtensions

The [**resetExtensions**](https://msdn.microsoft.com/library/windows/desktop/aa385694) function in Xenroll.dll removes the extension collection from the request.

To remove an extension from a request by index number using CertEnroll.dll, call the [**Remove**](/windows/win32/CertEnroll/nf-certenroll-ix509extensions-remove?branch=master) method on the [**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master) collection. To remove all attributes from a request, call the [**Clear**](/windows/win32/CertEnroll/nf-certenroll-ix509extensions-clear?branch=master) method.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**ICryptAttributes**](/windows/win32/CertEnroll/nn-certenroll-icryptattributes?branch=master)
</dt> <dt>

[**IX509Extension**](/windows/win32/CertEnroll/nn-certenroll-ix509extension?branch=master)
</dt> <dt>

[**IX509Extensions**](/windows/win32/CertEnroll/nn-certenroll-ix509extensions?branch=master)
</dt> </dl>

 

 



