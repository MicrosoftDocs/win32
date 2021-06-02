---
description: The original Base Provider incorrectly reported that the SHA hash algorithm enumerating algorithms by calls to CryptGetProvParam with parameter PP\_ENUMALGS specified.
ms.assetid: 75128a4f-273a-4195-b206-30fc8bc589e9
title: SHA Functionality
ms.topic: article
ms.date: 05/31/2018
---

# SHA Functionality

The original Base Provider incorrectly reported that the [*SHA*](../secgloss/s-gly.md) hash algorithm enumerating algorithms by calls to [**CryptGetProvParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetprovparam) with parameter PP\_ENUMALGS specified. This has been fixed in the Base Provider. Both the revised Base Provider and the Extended Provider and now correctly report SHA-1.

A defined CALG\_SHA1 constant has been added to Wincrypt.h with the same value as CALG\_SHA.

 

 
