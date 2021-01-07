---
description: Each of the following sections discusses a function exported by Xenroll.dll to manage Personal Information Exchange (PFX) messages.
ms.assetid: f7e6b3a6-eae4-49f8-a624-609742741560
title: Personal Information Exchange Functions
ms.topic: article
ms.date: 05/31/2018
---

# Personal Information Exchange Functions

Each of the following sections discusses a function exported by Xenroll.dll to manage Personal Information Exchange (PFX) messages. Each section also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists.

## createFilePFXWStr

The [**createFilePFXWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-createfilepfxwstr) function in Xenroll.dll saves a certificate chain and [*private key*](/windows/desktop/SecGloss/p-gly) in a file by using the PFX format.

The CertEnroll.dll library does not directly implement functionality to copy the PFX message to a file. You can, however, use the [**CreatePFX**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-createpfx) method on the [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) interface to create an encoded PFX message and write a custom function to save the message in a file.

## createPFXWStr

The [**createPFXWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-createpfxwstr) function in Xenroll.dll saves a certificate chain and private key in a PFX format string.

You can use the [**CreatePFX**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-createpfx) method on the [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) interface to create an encoded PFX message that contains the certificate chain and key. You can specify a password, export options, and encoding type. To retrieve a string that is equivalent to that returned from [**createPFXWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll4-createpfxwstr), pass the XCN\_CRYPT\_STRING\_BINARY flag in the in the *Encoding* parameter of the [**CreatePFX**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-createpfx) method.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment)
</dt> </dl>

 

 
