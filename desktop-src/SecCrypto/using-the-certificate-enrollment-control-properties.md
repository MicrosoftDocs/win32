---
Description: 'Each Certificate Enrollment Control property is read/write and has an initialized default as well as a set of acceptable values.'
ms.assetid: 'e31dd6df-bc2a-401f-9343-a7dbb0f374bb'
title: Using the Certificate Enrollment Control Properties
---

# Using the Certificate Enrollment Control Properties

Each Certificate Enrollment Control property is read/write and has an initialized default as well as a set of acceptable values. You can set a property to any value within this set in order to modify the behavior of methods that use the property. To get a desired behavior, set the property before you call the method that uses that property's value.

Note, however, that after calling the following methods

-   [**acceptPKCS7**](icenroll4-acceptpkcs7.md)
-   [**acceptFilePKCS7**](icenroll4-acceptfilepkcs7.md)
-   [**createPKCS10**](icenroll4-createpkcs10.md)
-   [**createFilePKCS10**](icenroll4-createfilepkcs10.md)

the following properties are blocked from being reset

-   [**ProviderType**](icenroll4-providertype.md)
-   [**KeySpec**](icenroll4-keyspec.md)
-   [**ProviderFlags**](icenroll4-providerflags.md)
-   [**ContainerName**](icenroll4-containername.md)
-   [**ProviderName**](icenroll4-providername.md)

unless the [**ICEnroll4::Reset**](icenroll4-reset.md) method is called.

For information about individual properties and methods, see the reference topics for those properties and methods in the [Cryptography Reference](cryptography-reference.md).

The following sections contain language-specific information for setting and retrieving the Certificate Enrollment Control properties:

-   [Certificate Enrollment Control Properties in C++](certificate-enrollment-control-properties-in-c-.md)

 

 



