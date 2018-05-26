---
Description: Certificates have associated properties, such as a display name, description, and allowed uses, that can be viewed and edited.
ms.assetid: 23faaa03-af3e-4497-8607-4e34f8889368
title: Creating, Viewing, and Managing Certificates
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating, Viewing, and Managing Certificates

[*Certificates*](security.c_gly#-security-certificate-gly) are read-only structures. The contents of a certificate can be viewed but cannot be modified. Information in the certificate itself includes the certificate's validity dates, issuer, subject, and the public key. However, certificates have associated properties, such as a display name, description, and allowed uses, that can be viewed and edited.

This section demonstrates creating test certificates, viewing certificates, and managing certificates and other security objects. The certificates and [*Software Publisher Certificates*](security.s_gly#-security-software-publisher-certificate-gly) (SPCs) that can be created with MakeCert are strictly for test purposes. A test [*root certificate*](security.r_gly#-security-root-certificate-gly) and a test root [*private key*](security.p_gly#-security-private-key-gly) are provided for testing purposes only. Independent software vendors must obtain a certificate from GTE, VeriSign, Inc., or other [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA) to sign code that will be distributed to the public.

This section includes the following topics:

-   [Using MakeCert](using-makecert.md)
-   [Using Cert2SPC](using-cert2spc.md)
-   [Using CertMgr](using-certmgr.md)

 

 



