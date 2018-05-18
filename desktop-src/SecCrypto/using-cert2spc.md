---
Description: 'The following command wraps an X.509 certificate, MyCert.cer, into a test PKCS \#7 Software Publisher Certificate (SPC), called MyCert.spc.'
ms.assetid: 'c3287289-d2bf-4d1d-80f0-e7dd41a3cbe3'
title: Using Cert2SPC
---

# Using Cert2SPC

The following command wraps an [*X.509*](security.x_gly#-security-x-509-gly) certificate, *MyCert*.cer, into a test PKCS \#7 [*Software Publisher Certificate*](security.s_gly#-security-software-publisher-certificate-gly) (SPC), called *MyCert*.spc. The SPC created is to be used for test purposes only. An SPC used to actually sign code to be distributed to the public must be obtained from GTE, VeriSign, Inc., or another trusted [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA).

**Cert2SPC** *MyCert***.cer** *MyCert***.spc**

 

 



