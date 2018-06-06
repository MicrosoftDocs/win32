---
Description: Certificates have associated properties, such as a display name, description, and allowed uses, that can be viewed and edited.
ms.assetid: 23faaa03-af3e-4497-8607-4e34f8889368
title: Creating, Viewing, and Managing Certificates
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating, Viewing, and Managing Certificates

[*Certificates*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) are read-only structures. The contents of a certificate can be viewed but cannot be modified. Information in the certificate itself includes the certificate's validity dates, issuer, subject, and the public key. However, certificates have associated properties, such as a display name, description, and allowed uses, that can be viewed and edited.

This section demonstrates creating test certificates, viewing certificates, and managing certificates and other security objects. The certificates and [*Software Publisher Certificates*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) (SPCs) that can be created with MakeCert are strictly for test purposes. A test [*root certificate*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd) and a test root [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) are provided for testing purposes only. Independent software vendors must obtain a certificate from GTE, VeriSign, Inc., or other [*certification authority*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CA) to sign code that will be distributed to the public.

This section includes the following topics:

-   [Using MakeCert](using-makecert.md)
-   [Using Cert2SPC](using-cert2spc.md)
-   [Using CertMgr](using-certmgr.md)

 

 



