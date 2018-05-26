---
Description: The original Base Provider incorrectly reported that the SHA hash algorithm enumerating algorithms by calls to CryptGetProvParam with parameter PP\_ENUMALGS specified.
ms.assetid: 75128a4f-273a-4195-b206-30fc8bc589e9
title: SHA Functionality
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SHA Functionality

The original Base Provider incorrectly reported that the [*SHA*](security.s_gly#-security-secure-hash-algorithm-gly) hash algorithm enumerating algorithms by calls to [**CryptGetProvParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetprovparam?branch=master) with parameter PP\_ENUMALGS specified. This has been fixed in the Base Provider. Both the revised Base Provider and the Extended Provider and now correctly report SHA-1.

A defined CALG\_SHA1 constant has been added to Wincrypt.h with the same value as CALG\_SHA.

 

 



