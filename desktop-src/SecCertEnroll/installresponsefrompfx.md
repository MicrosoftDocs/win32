---
description: Installs an enrolled certificate from a Personal Information Exchange (PFX) file to the certificate store.
ms.assetid: f42379d0-b80e-4d95-ab34-9bb35fde06fd
title: installResponseFromPFX
ms.topic: article
ms.date: 05/31/2018
---

# installResponseFromPFX

The installResponseFromPFX sample installs an enrolled certificate from a Personal Information Exchange (PFX) file to the certificate store.

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\installResponseFromPFX folder.

## Discussion

The installResponseFromPFX sample:

1.  Processes the command line arguments. The command line should contain:
    -   The name of the sample.
    -   The name of the PFX file that contains the enrolled certificate.
    -   A password associated with the PFX file.
2.  Reads the PFX file, trying the base64 format first and the binary format if base64 fails. The DecodeFileW() function is defined in enrollCommon.cpp.
3.  Converts the enrolled certificate to a **BSTR** and uses it to initialize an [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object. The convertWszToBstr function is defined in enrollCommon.cpp.
4.  Installs the certificate in the certificate store.

## Related topics

<dl> <dt>

[enrollEOBOCMC](enrolleobocmc.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 



