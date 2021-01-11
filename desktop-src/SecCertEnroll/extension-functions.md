---
description: The X.509 version 3 certificate format identifies multiple extensions that can be added to a certificate to provide enhanced information about key usage, certificate policies and constraints, alternative name forms, and more.
ms.assetid: d53107b7-a153-41cf-9876-1d28aaf99816
title: Extension Functions
ms.topic: article
ms.date: 05/31/2018
---

# Extension Functions

The [*X.509*](/windows/desktop/SecGloss/x-gly) version 3 certificate format identifies multiple extensions that can be added to a certificate to provide enhanced information about key usage, certificate policies and constraints, alternative name forms, and more.

CertEnroll.dll implements the following interfaces to manage certificate extensions:

-   [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)
-   [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions)
-   [**IX509ExtensionAlternativeNames**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionalternativenames)
-   [**IX509ExtensionAuthorityKeyIdentifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionauthoritykeyidentifier)
-   [**IX509ExtensionBasicConstraints**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionbasicconstraints)
-   [**IX509ExtensionCertificatePolicies**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensioncertificatepolicies)
-   [**IX509ExtensionEnhancedKeyUsage**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionenhancedkeyusage)
-   [**IX509ExtensionKeyUsage**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionkeyusage)
-   [**IX509ExtensionMSApplicationPolicies**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionmsapplicationpolicies)
-   [**IX509ExtensionSmimeCapabilities**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsmimecapabilities)
-   [**IX509ExtensionSubjectKeyIdentifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier)
-   [**IX509ExtensionTemplate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplate)
-   [**IX509ExtensionTemplateName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplatename)

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

The [**AddCertTypeToRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-addcerttypetorequestwstr) function in Xenroll.dll adds a certificate template, by name, to a request.

Using CertEnroll.dll, the preferred method to incorporate a template into a certificate request is to use the [**InitializeFromTemplateName**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-initializefromtemplatename) method on a PKCS\#10 or [*PKCS ) request object or the [**InitializeFromInnerRequestTemplateName**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-initializefrominnerrequesttemplatename) method on a CMC request.

If a specific template is not available on the client but is expected to be understood by the [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA), you can use the [**IX509ExtensionTemplateName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplatename) interface to add a version 1 template or you can use the [**IX509ExtensionTemplate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplate) interface to add a version 2 template to a certificate request. For example, to add a version 1 template, perform the following actions:

1.  Create an [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) object.
2.  Create an [**IX509ExtensionTemplateName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplatename) object and call the [**InitializeEncode**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509extensiontemplatename-initializeencode) method, specifying the template name.
3.  Add the extension created to the [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) collection by calling the [**Add**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509extensions-add) method.
4.  Create an [**IX509AttributeExtensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeextensions) object and call the [**InitializeEncode**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509attributeextensions-initializeencode) method, specifying the [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) collection on input.
5.  Retrieve an [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes) collection object by calling the [**CryptAttributes**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_cryptattributes) property on an existing [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) or [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) request object.

## AddCertTypeToRequestWStrEx

The [**AddCertTypeToRequestWStrEx**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-addcerttypetorequestwstrex) function in Xenroll.dll adds a certificate template to a request by name, object identifier, and version.

For information about how to use CertEnroll.dll to incorporate template information in a request, see AddCertTypeToRequestWStr.

## AddExtensionsToRequest

The [**AddExtensionsToRequest**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-addextensionstorequest) function in Xenroll.dll adds a collection of extensions to a request.

In CertEnroll.dll, extensions are added to the attributes collection of a CMC or a PKCS \#10 request. To add extensions, perform the following actions:

1.  Create an [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) object.
2.  Create an [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension) object and call the [**Initialize**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509extension-initialize) method to create an extension from an object identifier and extension value or use any of the interfaces listed earlier to define one of the more common extensions.
3.  Add each new extension created in the preceding step to the [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) collection by calling the [**Add**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509extensions-add) method.

## addExtensionToRequestWStr

The [**addExtensionToRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-addextensiontorequestwstr) function in Xenroll.dll adds a specific extension to the request.

In CertEnroll.dll, a specific extension must be defined and added to an extensions collection before the extension collection is added to the attributes collection of a CMC or a PKCS \#10 request. For more information see the AddExtensionsToRequest discussion above.

## EnableSMIMECapabilities

The [**EnableSMIMECapabilities**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-get_enablesmimecapabilities) function in Xenroll.dll specifies or retrieves a Boolean value that indicates whether to add the **SMIMECapabilities** extension to the request.

You can call the [**SmimeCapabilities**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_smimecapabilities) property on the [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object to automatically add an [**IX509ExtensionSmimeCapabilities**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsmimecapabilities) object to the request before encoding.

## IncludeSubjectKeyID

The [**IncludeSubjectKeyID**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-get_includesubjectkeyid) function in Xenroll.dll specifies or retrieves a Boolean value that indicates whether to add the **SubjectKeyIdentifier** extension to the request.

By default, the **SubjectKeyIdentifier** extension is created when the [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) request object is initialized. You can override this behavior by calling the [**SuppressOids**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_suppressoids) property.

If you have a [*public/private key pair*](/windows/desktop/SecGloss/p-gly), you can also use the [**IX509ExtensionSubjectKeyIdentifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier) interface in CertEnroll.dll to add a **SubjectKeyIdentifier** extension to a certificate request by performing the following actions:

1.  Create an [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) object.
2.  Create an [**IX509ExtensionSubjectKeyIdentifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier) object and call the [**InitializeEncode**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509extensionsubjectkeyidentifier-initializeencode) method, specifying a string that contains the identifier. Typically, this is a 20-byte SHA-1 hash of the [*public key*](/windows/desktop/SecGloss/p-gly) contained in the CA signing certificate.
3.  Add the extension created to the [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) collection by calling the [**Add**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509extensions-add) method.
4.  Create an [**IX509AttributeExtensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeextensions) object and call the [**InitializeEncode**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509attributeextensions-initializeencode) method, specifying the [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) collection on input.
5.  Retrieve an [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes) collection object by calling the [**CryptAttributes**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_cryptattributes) property on an existing [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) or [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) request object.

## resetExtensions

The [**resetExtensions**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-resetextensions) function in Xenroll.dll removes the extension collection from the request.

To remove an extension from a request by index number using CertEnroll.dll, call the [**Remove**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509extensions-remove) method on the [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) collection. To remove all attributes from a request, call the [**Clear**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509extensions-clear) method.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes)
</dt> <dt>

[**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)
</dt> <dt>

[**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions)
</dt> </dl>

 

 
