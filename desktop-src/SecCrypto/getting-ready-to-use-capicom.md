---
description: Applications that use CAPICOM objects must be created by using CAPICOM.dll. CAPICOM.dll must also be present and registered at run time to use CAPICOM objects.
ms.assetid: 69de5232-e2f9-4aed-935d-5fbcd7998cc9
title: Getting Ready to Use CAPICOM
ms.topic: article
ms.date: 05/31/2018
---

# Getting Ready to Use CAPICOM

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

Applications that use CAPICOM objects must be created by using CAPICOM.dll. CAPICOM.dll must also be present and registered at run time to use CAPICOM objects. CAPICOM.dll should be added to Visual Basic projects references to use CAPICOM objects.

CAPICOM is available as a redistributable file that can be downloaded from [Platform SDK Redistributable: CAPICOM](https://www.microsoft.com/download/details.aspx?id=25281). For information about CAPICOM versions, see [CAPICOM Versions](capicom-versions.md).

**To register CAPICOM.dll**

-   At a command prompt, change the directory to the directory where CAPICOM.dll is stored, and then enter the following command:

    **regsvr32 CAPICOM.dll**

## Example Code Limitations

To provide more concise, more readable code, principles of good programming practice are not always followed in these examples. In particular, only limited error responses are shown. Working applications should always check returned error codes and perform appropriate actions when an error is encountered.

## Necessary Key Containers, Keys, and Certificates in CAPICOM

While some operations with CAPICOM objects can be done on any computer by any user, creating [*digital signatures*](../secgloss/d-gly.md) and retrieving the plaintext content of an enveloped message using CAPICOM objects are certificate-based operations. The user who creates a digital signature and the user who retrieves the encrypted contents of an enveloped message must have a digital certificate with an available associated private key. If a certificate with an associated private key is not present, the cryptographic operation will fail. Users of CAPICOM applications must ensure that they have the appropriate certificate and available private key when the applications are running.

Some examples in the following sections perform operations that require an available [*public/private key pair*](../secgloss/p-gly.md) for encrypting and decrypting files, messages, and signatures. Many of these programs will compile and run but fail at run time without the existence of proper [*key containers*](../secgloss/k-gly.md), keys, certificate stores, and [*certificates*](../secgloss/c-gly.md) in those stores.

**To create a self-signed certificate**

1.  Install the signing tools. These are installed as part of the Microsoft Windows Software Development Kit (SDK), the Platform Software Development Kit (SDK), or the .NET Framework SDK.
2.  After Makecert.exe is downloaded, run the following command at a command prompt, substituting a user name for *UserName*, an organization name for *OrganizationName*, and a company name for *CompanyName*:

    **makecert -r -n "cn=***UserName***, ou=***OrganizationName***, o=***CompanyName***" -ss my**

3.  The certificate can be placed in the My store of the current user. Import the certificate created into the root store so that it is trusted.

 

 
