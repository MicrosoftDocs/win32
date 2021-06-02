---
description: Attributes can be added to a certificate request to provide a certification authority (CA) with additional information that it can use when creating and issuing a certificate.
ms.assetid: 3eba5a2f-eeac-4e38-8705-b12bc183b7eb
title: Attribute Functions
ms.topic: article
ms.date: 05/31/2018
---

# Attribute Functions

Attributes can be added to a certificate request to provide a [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA) with additional information that it can use when creating and issuing a certificate.

CertEnroll.dll implements the following interfaces to define attributes and attribute collections:

-   [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute)
-   [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes)
-   [**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute)
-   [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes)
-   [**IX509AttributeClientId**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeclientid)
-   [**IX509AttributeExtensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeextensions)
-   [**IX509AttributeArchiveKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekey)
-   [**IX509AttributeArchiveKeyHash**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekeyhash)
-   [**IX509AttributeCspProvider**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributecspprovider)
-   [**IX509AttributeOSVersion**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeosversion)
-   [**IX509AttributeRenewalCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributerenewalcertificate)

The following sections identify functions exported by Xenroll.dll to associate cryptographic attributes with certificate requests and discuss how to use CertEnroll.dll to replace the function or indicate that no mapping between the two libraries exists:

-   [addAttributeToRequestWStr](#addattributetorequestwstr)
-   [AddAuthenticatedAttributesToPKCS7Request](#addauthenticatedattributestopkcs7request)
-   [addNameValuePairToRequestWStr](#addnamevaluepairtorequestwstr)
-   [AddNameValuePairToSignatureWStr](#addnamevaluepairtosignaturewstr)
-   [ClientId](#clientid)
-   [RenewalCertificate](#renewalcertificate)
-   [resetAttributes](#resetattributes)
-   [Related topics](#related-topics)

## addAttributeToRequestWStr

The [**addAttributeToRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-addattributetorequestwstr) function in Xenroll.dll adds an attribute to a certificate request.

In general, to add an attribute to a request by using the objects implemented in CertEnroll.dll, you can perform the following actions:

1.  Create an [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes) collection object.
2.  Create an [**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute) object and call the [**Initialize**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509attribute-initialize) method to create an attribute from an object identifier and attribute value or use any of the interfaces listed earlier to define one of the more common attributes.
3.  Add each new attribute created in the preceding step to the [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes) collection by using the [**Add**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509attributes-add) method.
4.  Create an [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute) object and initialize it by calling the [**InitializeFromValues**](/windows/desktop/api/CertEnroll/nf-certenroll-icryptattribute-initializefromvalues) method and specifying the [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes) collection on input.
5.  Retrieve an [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes) collection object by calling the [**CryptAttributes**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_cryptattributes) property on an existing [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) or [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) request object.
6.  Add the [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute) object to the [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes) collection.

## AddAuthenticatedAttributesToPKCS7Request

Authenticated attributes are name-value pairs that are signed by and added to a signature. The [**AddAuthenticatedAttributesToPKCS7Request**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-addauthenticatedattributestopkcs7request) function in Xenroll.dll adds an array of authenticated attributes to a [*PKCS \#7*](/windows/desktop/SecGloss/p-gly) request.

As discussed above for the [**addAttributeToRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-addattributetorequestwstr) function, you can use CertEnroll.dll to easily define and add a collection of attributes to a certificate request. You cannot, however, choose whether the attribute is authenticated. The enrollment process automatically makes this decision.

## addNameValuePairToRequestWStr

The [**addNameValuePairToRequestWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-addnamevaluepairtorequestwstr) function in Xenroll.dll adds an unauthenticated name-value pair to a request.

You can use the [**IX509NameValuePair**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepair) interface in CertEnroll.dll to define a name-value pair, and you can add a collection of name-value pairs to a CMC request object by performing the following actions:

1.  Create and initialize an [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) object. The initialization process creates an empty [**IX509NameValuePairs**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepairs) collection.
2.  Call the [**NameValuePairs**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_namevaluepairs) property on an existing CMC request object to retrieve the collection.
3.  Create and initialize an [**IX509NameValuePair**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepair) object.
4.  Add each new name-value pair to the [**IX509NameValuePairs**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepairs) collection by calling the [**Add**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509namevaluepairs-add) method.

The enrollment process places the collection of name-value pairs in the **TaggedAttribute** structure of the CMC request.

## AddNameValuePairToSignatureWStr

The [**AddNameValuePairToSignatureWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-addnamevaluepairtosignaturewstr) function in Xenroll.dll adds an authenticated name-value pair to a request. This is typically used to specify the requester name in an enroll-on-behalf-of (EOBO) request.

In CertEnroll.dll, use the [**RequesterName**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-get_requestername) property to specify the name in an EOBO request.

## ClientId

The [**ClientId**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-get_clientid) function in Xenroll.dll specifies or retrieves a **ClientId** attribute.

Use the [**ClientId**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequest-get_clientid) property in CertEnroll.dll to add this attribute to a CMC or PKCS \#10 request.

## RenewalCertificate

The [**RenewalCertificate**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_renewalcertificate) function in Xenroll.dll specifies or retrieves a **RenewalCertificate** attribute.

In CertEnroll.dll, when you call [**InitializeFromCertificate**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs7-initializefromcertificate) on a PKCS \#7 or PKCS ) object is automatically created.

## resetAttributes

The [**resetAttributes**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-resetattributes) function in Xenroll.dll removes the attribute collection from a request.

To remove an attribute from a request by index using CertEnroll.dll, call the [**Remove**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509attributes-remove) method on the [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes) collection. To remove all attributes from a request, call the [**Clear**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509attributes-clear) method.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute)
</dt> <dt>

[**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes)
</dt> <dt>

[**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute)
</dt> <dt>

[**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes)
</dt> <dt>

[**IX509NameValuePair**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepair)
</dt> <dt>

[**IX509NameValuePairs**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepairs)
</dt> </dl>

 

 
