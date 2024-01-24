---
description: The following command wraps an X.509 certificate, MyCert.cer, into a test PKCS \#7 Software Publisher Certificate (SPC), called MyCert.spc.
ms.assetid: c3287289-d2bf-4d1d-80f0-e7dd41a3cbe3
title: Using Cert2SPC
ms.topic: article
ms.date: 05/31/2018
---

# Using Cert2SPC

The following command wraps an [*X.509*](../secgloss/x-gly.md) certificate, *MyCert*.cer, into a test PKCS \#7 [*Software Publisher Certificate*](../secgloss/s-gly.md) (SPC), called *MyCert*.spc. The SPC created is to be used for test purposes only. An SPC used to actually sign code to be distributed to the public must be obtained from GTE, VeriSign, Inc., or another trusted [*certification authority*](../secgloss/c-gly.md) (CA).

**Cert2SPC** *MyCert***.cer** *MyCert***.spc**

 

 
