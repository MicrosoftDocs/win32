---
Description: 'Attributes can be added to a certificate request to provide a certification authority (CA) with additional information that it can use when creating and issuing a certificate.'
ms.assetid: '3eba5a2f-eeac-4e38-8705-b12bc183b7eb'
title: Attribute Functions
---

# Attribute Functions

Attributes can be added to a certificate request to provide a [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA) with additional information that it can use when creating and issuing a certificate.

CertEnroll.dll implements the following interfaces to define attributes and attribute collections:

-   [**ICryptAttribute**](icryptattribute.md)
-   [**ICryptAttributes**](icryptattributes.md)
-   [**IX509Attribute**](ix509attribute.md)
-   [**IX509Attributes**](ix509attributes.md)
-   [**IX509AttributeClientId**](ix509attributeclientid.md)
-   [**IX509AttributeExtensions**](ix509attributeextensions.md)
-   [**IX509AttributeArchiveKey**](ix509attributearchivekey.md)
-   [**IX509AttributeArchiveKeyHash**](ix509attributearchivekeyhash.md)
-   [**IX509AttributeCspProvider**](ix509attributecspprovider.md)
-   [**IX509AttributeOSVersion**](ix509attributeosversion.md)
-   [**IX509AttributeRenewalCertificate**](ix509attributerenewalcertificate.md)

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

The [**addAttributeToRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385506) function in Xenroll.dll adds an attribute to a certificate request.

In general, to add an attribute to a request by using the objects implemented in CertEnroll.dll, you can perform the following actions:

1.  Create an [**IX509Attributes**](ix509attributes.md) collection object.
2.  Create an [**IX509Attribute**](ix509attribute.md) object and call the [**Initialize**](ix509attribute-initialize-method.md) method to create an attribute from an object identifier and attribute value or use any of the interfaces listed earlier to define one of the more common attributes.
3.  Add each new attribute created in the preceding step to the [**IX509Attributes**](ix509attributes.md) collection by using the [**Add**](ix509attributes-add-method.md) method.
4.  Create an [**ICryptAttribute**](icryptattribute.md) object and initialize it by calling the [**InitializeFromValues**](icryptattribute-initializefromvalues-method.md) method and specifying the [**IX509Attributes**](ix509attributes.md) collection on input.
5.  Retrieve an [**ICryptAttributes**](icryptattributes.md) collection object by calling the [**CryptAttributes**](ix509certificaterequestpkcs10-cryptattributes-property.md) property on an existing [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) or [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) request object.
6.  Add the [**ICryptAttribute**](icryptattribute.md) object to the [**ICryptAttributes**](icryptattributes.md) collection.

## AddAuthenticatedAttributesToPKCS7Request

Authenticated attributes are name-value pairs that are signed by and added to a signature. The [**AddAuthenticatedAttributesToPKCS7Request**](https://msdn.microsoft.com/library/windows/desktop/aa385508) function in Xenroll.dll adds an array of authenticated attributes to a [*PKCS \#7*](https://msdn.microsoft.com/library/windows/desktop/ms721603) request.

As discussed above for the [**addAttributeToRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385506) function, you can use CertEnroll.dll to easily define and add a collection of attributes to a certificate request. You cannot, however, choose whether the attribute is authenticated. The enrollment process automatically makes this decision.

## addNameValuePairToRequestWStr

The [**addNameValuePairToRequestWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385520) function in Xenroll.dll adds an unauthenticated name-value pair to a request.

You can use the [**IX509NameValuePair**](ix509namevaluepair.md) interface in CertEnroll.dll to define a name-value pair, and you can add a collection of name-value pairs to a CMC request object by performing the following actions:

1.  Create and initialize an [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) object. The initialization process creates an empty [**IX509NameValuePairs**](ix509namevaluepairs.md) collection.
2.  Call the [**NameValuePairs**](ix509certificaterequestcmc-namevaluepairs-property.md) property on an existing CMC request object to retrieve the collection.
3.  Create and initialize an [**IX509NameValuePair**](ix509namevaluepair.md) object.
4.  Add each new name-value pair to the [**IX509NameValuePairs**](ix509namevaluepairs.md) collection by calling the [**Add**](ix509namevaluepairs-add-method.md) method.

The enrollment process places the collection of name-value pairs in the **TaggedAttribute** structure of the CMC request.

## AddNameValuePairToSignatureWStr

The [**AddNameValuePairToSignatureWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385521) function in Xenroll.dll adds an authenticated name-value pair to a request. This is typically used to specify the requester name in an enroll-on-behalf-of (EOBO) request.

In CertEnroll.dll, use the [**RequesterName**](ix509certificaterequestpkcs7-requestername-property.md) property to specify the name in an EOBO request.

## ClientId

The [**ClientId**](https://msdn.microsoft.com/library/windows/desktop/aa385531) function in Xenroll.dll specifies or retrieves a **ClientId** attribute.

Use the [**ClientId**](ix509certificaterequest-clientid-property.md) property in CertEnroll.dll to add this attribute to a CMC or PKCS \#10 request.

## RenewalCertificate

The [**RenewalCertificate**](https://msdn.microsoft.com/library/windows/desktop/aa385671) function in Xenroll.dll specifies or retrieves a **RenewalCertificate** attribute.

In CertEnroll.dll, when you call [**InitializeFromCertificate**](ix509certificaterequestpkcs7-initializefromcertificate-method.md) on a PKCS \#7 or PKCS ) object is automatically created.

## resetAttributes

The [**resetAttributes**](https://msdn.microsoft.com/library/windows/desktop/aa385691) function in Xenroll.dll removes the attribute collection from a request.

To remove an attribute from a request by index using CertEnroll.dll, call the [**Remove**](ix509attributes-remove-method.md) method on the [**IX509Attributes**](ix509attributes.md) collection. To remove all attributes from a request, call the [**Clear**](ix509attributes-clear-method.md) method.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**ICryptAttribute**](icryptattribute.md)
</dt> <dt>

[**ICryptAttributes**](icryptattributes.md)
</dt> <dt>

[**IX509Attribute**](ix509attribute.md)
</dt> <dt>

[**IX509Attributes**](ix509attributes.md)
</dt> <dt>

[**IX509NameValuePair**](ix509namevaluepair.md)
</dt> <dt>

[**IX509NameValuePairs**](ix509namevaluepairs.md)
</dt> </dl>

 

 



