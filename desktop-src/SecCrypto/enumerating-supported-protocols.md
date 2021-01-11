---
description: Supported protocols and cipher suites can be listed by calls to CryptGetProvParam with PP\_ENUMALGS or PP\_ENUMALGS\_EX.
ms.assetid: 8f0c2129-6841-4793-a404-bb6ee8f41683
title: Enumerating Supported Protocols
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Supported Protocols

Supported protocols and cipher suites can be listed by calls to [**CryptGetProvParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetprovparam) with PP\_ENUMALGS or PP\_ENUMALGS\_EX. The PP\_ENUMALGS\_EX value works like PP\_ENUMALGS but returns a [**PROV\_ENUMALGS\_EX**](/windows/desktop/api/Wincrypt/ns-wincrypt-prov_enumalgs_ex) structure that holds more extensive information on the algorithms supported by the provider.

For more information about defined protocol flags and their values, see [Protocol Flags](protocol-flags.md).

Given that the **hCryptProv** member is the [*handle*](../secgloss/h-gly.md) of an open cryptographic [*context*](../secgloss/c-gly.md) acquired by using [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) with its *dwProvType* parameter set to PROV\_RSA\_SCHANNEL, the following example lists the names of all algorithms available in the CSP.


```C++
PROV_ENUMALGS_EX EnumAlgs;     //   Structure to hold information on 
                               //   a supported algorithm
DWORD dFlag = CRYPT_FIRST;     //   Flag indicating that the first
                               //   supported algorithm is to be
                               //   enumerated. Changed to 0 after the
                               //   first call to the function.
cbData = sizeof(PROV_ENUMALGS_EX);

while( CryptGetProvParam(
    hCryptProv,          // handle to an open cryptographic provider
    PP_ENUMALGS_EX, 
    (BYTE *)&EnumAlgs,  // information on the next algorithm
    &cbData,            // number of bytes in the PROV_ENUMALGS_EX
    dFlag))             // flag to indicate whether this is a first or
                        // subsequent algorithm supported by the
                        // CSP.
{
    printf("Supported Algorithm name %s\n", EnumAlgs.szName);
    dFlag = CRYPT_NEXT;          // Set to CRYPT_NEXT after the first call,
} //  end of while loop. When all of the supported algorithms have
  //  been enumerated, the function returns FALSE.
```



The following table lists some algorithms returned by a typical domestic PROV\_RSA\_SCHANNEL CSP. Notice that neither SSL2 SHA MACs nor SSL2 DES encryption is supported by the CSP in this example.



| Algorithm identifier                                                                        | Minimum key length | Maximum key length | Protocols | Algorithm name |
|---------------------------------------------------------------------------------------------|--------------------|--------------------|-----------|----------------|
| [*CALG\_RSA\_KEYX*](../secgloss/c-gly.md) | 512                | 2048               | 0x0007    | "RSA\_KEYX"    |
| [*CALG\_MD5*](../secgloss/c-gly.md)                 | 128                | 128                | 0x0007    | "MD5"          |
| [*CALG\_SHA*](../secgloss/c-gly.md)                 | 160                | 160                | 0x0005    | "SHA"          |
| [*CALG\_RC4*](../secgloss/c-gly.md)                 | 40                 | 128                | 0x0007    | "RC4"          |
| CALG\_DES                                                                                   | 56                 | 56                 | 0x0005    | "DES"          |



 

To prepare to send ClientHello or ServerHello messages, the [*Schannel*](../secgloss/s-gly.md) protocol engine enumerates the algorithms and key sizes supported by the CSP and builds a list internally of supported cipher suites.

 

 
