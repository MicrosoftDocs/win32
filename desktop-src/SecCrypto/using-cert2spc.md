---
Description: The following command wraps an X.509 certificate, MyCert.cer, into a test PKCS \#7 Software Publisher Certificate (SPC), called MyCert.spc.
ms.assetid: c3287289-d2bf-4d1d-80f0-e7dd41a3cbe3
title: Using Cert2SPC
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Cert2SPC

The following command wraps an [*X.509*](https://msdn.microsoft.com/28dba6ef-939f-4789-9789-ee6e0fef0177) certificate, *MyCert*.cer, into a test PKCS \#7 [*Software Publisher Certificate*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) (SPC), called *MyCert*.spc. The SPC created is to be used for test purposes only. An SPC used to actually sign code to be distributed to the public must be obtained from GTE, VeriSign, Inc., or another trusted [*certification authority*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CA).

**Cert2SPC** *MyCert***.cer** *MyCert***.spc**

 

 



