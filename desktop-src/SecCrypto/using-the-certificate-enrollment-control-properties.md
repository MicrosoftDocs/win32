---
description: Each Certificate Enrollment Control property is read/write and has an initialized default as well as a set of acceptable values.
ms.assetid: e31dd6df-bc2a-401f-9343-a7dbb0f374bb
title: Using the Certificate Enrollment Control Properties
ms.topic: article
ms.date: 05/31/2018
---

# Using the Certificate Enrollment Control Properties

Each Certificate Enrollment Control property is read/write and has an initialized default as well as a set of acceptable values. You can set a property to any value within this set in order to modify the behavior of methods that use the property. To get a desired behavior, set the property before you call the method that uses that property's value.

Note, however, that after calling the following methods

-   [**acceptPKCS7**](/windows/desktop/api/Xenroll/nf-xenroll-icenroll-acceptpkcs7)
-   [**acceptFilePKCS7**](/windows/desktop/api/Xenroll/nf-xenroll-icenroll-acceptfilepkcs7)
-   [**createPKCS10**](/windows/desktop/api/Xenroll/nf-xenroll-icenroll-createpkcs10)
-   [**createFilePKCS10**](/windows/desktop/api/Xenroll/nf-xenroll-icenroll-createfilepkcs10)

the following properties are blocked from being reset

-   [**ProviderType**](/windows/win32/api/xenroll/nf-xenroll-icenroll-get_providertype)
-   [**KeySpec**](/windows/win32/api/xenroll/nf-xenroll-icenroll-get_keyspec)
-   [**ProviderFlags**](/windows/win32/api/xenroll/nf-xenroll-icenroll-get_providerflags)
-   [**ContainerName**](/windows/win32/api/xenroll/nf-xenroll-icenroll-get_containername)
-   [**ProviderName**](/windows/win32/api/xenroll/nf-xenroll-icenroll-get_providername)

unless the [**ICEnroll4::Reset**](/windows/desktop/api/Xenroll/nf-xenroll-icenroll3-reset) method is called.

For information about individual properties and methods, see the reference topics for those properties and methods in the [Cryptography Reference](cryptography-reference.md).

The following sections contain language-specific information for setting and retrieving the Certificate Enrollment Control properties:

-   [Certificate Enrollment Control Properties in C++](certificate-enrollment-control-properties-in-c-.md)

 

 
