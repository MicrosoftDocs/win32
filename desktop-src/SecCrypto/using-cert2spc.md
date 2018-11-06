---
Description: The following command wraps an X.509 certificate, MyCert.cer, into a test PKCS \#7 Software Publisher Certificate (SPC), called MyCert.spc.
ms.assetid: c3287289-d2bf-4d1d-80f0-e7dd41a3cbe3
title: Using Cert2SPC
ms.topic: article
ms.date: 05/31/2018
---

# Using Cert2SPC

The following command wraps an [*X.509*](https://msdn.microsoft.com/en-us/library/ms721636(v=VS.85).aspx) certificate, *MyCert*.cer, into a test PKCS \#7 [*Software Publisher Certificate*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) (SPC), called *MyCert*.spc. The SPC created is to be used for test purposes only. An SPC used to actually sign code to be distributed to the public must be obtained from GTE, VeriSign, Inc., or another trusted [*certification authority*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CA).

**Cert2SPC** *MyCert***.cer** *MyCert***.spc**

 

 



