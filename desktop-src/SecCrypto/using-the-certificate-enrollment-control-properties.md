---
Description: Each Certificate Enrollment Control property is read/write and has an initialized default as well as a set of acceptable values.
ms.assetid: e31dd6df-bc2a-401f-9343-a7dbb0f374bb
title: Using the Certificate Enrollment Control Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Certificate Enrollment Control Properties

Each Certificate Enrollment Control property is read/write and has an initialized default as well as a set of acceptable values. You can set a property to any value within this set in order to modify the behavior of methods that use the property. To get a desired behavior, set the property before you call the method that uses that property's value.

Note, however, that after calling the following methods

-   [**acceptPKCS7**](/windows/win32/Xenroll/nf-xenroll-icenroll-acceptpkcs7?branch=master)
-   [**acceptFilePKCS7**](/windows/win32/Xenroll/nf-xenroll-icenroll-acceptfilepkcs7?branch=master)
-   [**createPKCS10**](/windows/win32/Xenroll/nf-xenroll-icenroll-createpkcs10?branch=master)
-   [**createFilePKCS10**](/windows/win32/Xenroll/nf-xenroll-icenroll-createfilepkcs10?branch=master)

the following properties are blocked from being reset

-   [**ProviderType**](/windows/win32/Xenroll/?branch=master)
-   [**KeySpec**](/windows/win32/Xenroll/?branch=master)
-   [**ProviderFlags**](/windows/win32/Xenroll/?branch=master)
-   [**ContainerName**](/windows/win32/Xenroll/?branch=master)
-   [**ProviderName**](/windows/win32/Xenroll/?branch=master)

unless the [**ICEnroll4::Reset**](/windows/win32/Xenroll/nf-xenroll-icenroll3-reset?branch=master) method is called.

For information about individual properties and methods, see the reference topics for those properties and methods in the [Cryptography Reference](cryptography-reference.md).

The following sections contain language-specific information for setting and retrieving the Certificate Enrollment Control properties:

-   [Certificate Enrollment Control Properties in C++](certificate-enrollment-control-properties-in-c-.md)

 

 



