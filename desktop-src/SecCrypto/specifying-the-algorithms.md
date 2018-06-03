---
Description: After a master key is created or imported, both RSA/Schannel and Diffie-Hellman/Schannel inform the CSP of the type of bulk encryption keys and MAC keys that will be derived from the master key.
ms.assetid: d0976a7e-3c8e-4bbe-80e1-568a27ab81c6
title: Specifying the Algorithms
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Specifying the Algorithms

After a [*master key*](https://www.bing.com/search?q=*master key*) is created or imported, both [*RSA*](https://www.bing.com/search?q=*RSA*)/Schannel and [*Diffie-Hellman*](https://www.bing.com/search?q=*Diffie-Hellman*)/Schannel inform the [*CSP*](https://www.bing.com/search?q=*CSP*) of the type of [*bulk encryption keys*](https://www.bing.com/search?q=*bulk encryption keys*) and [*MAC keys*](https://www.bing.com/search?q=*MAC keys*) that will be derived from the master key. The following example specifies these algorithms. The same code is used for both client and server.


```C++
#include <windows.h>
#include <stdio.h>

typedef struct _SCHANNEL_ALG 
{
    DWORD  dwUse;
    ALG_ID Algid;
    DWORD  cBits;
    DWORD  dwFlags;
    DWORD  dwReserved;
} SCHANNEL_ALG, *PSCHANNEL_ALG;

SCHANNEL_ALG Algorithm;

//--------------------------------------------------------------------
// Algorithms for the SCHANNEL_ALG structure

#define SCHANNEL_MAC_KEY   0x00000000
#define SCHANNEL_ENC_KEY   0x00000001

//--------------------------------------------------------------------
// dwFlags for the SCHANNEL_ALG structure
// This flag will be set when the SSL cipher suite is exportable 
// outside the United States and Canada. The use of this flag notifies
// the CSP that it must perform the extra export steps when deriving 
// the key.

#define INTERNATIONAL USAGE   0x00000001

void main()
{
//--------------------------------------------------------------------
// Specify the bulk encryption algorithm.

Algorithm.dwUse = SCHANNEL_ENC_KEY;
Algorithm.Algid = CALG_RC4;    // or CALG_RC2, CALG_DES, and so on
Algorithm.cBits = 40;          // or 64, 128, 192, and so on
if (!CryptSetKeyParam(
         hMasterKey, 
         KP_SCHANNEL_ALG, 
         (PBYTE)&amp;Algorithm, 
         0))
{
    printf("Failed called to CryptSetKeyParam\n");
    exit(1);
};

//--------------------------------------------------------------------
// Specify hash algorithm.
Algorithm.dwUse = SCHANNEL_MAC_KEY;
Algorithm.Algid = CALG_MD5;    // or CALG_SHA, and so on
Algorithm.cBits = 128;         // or 160...
if (!CryptSetKeyParam(
          hMasterKey, 
          KP_SCHANNEL_ALG, 
          (PBYTE)&amp;Algorithm, 
          0))
{
    printf("Failed called to CryptSetKeyParam\n");
    exit(1);
};
```



> [!Note]  
> An [*Schannel*](https://www.bing.com/search?q=*Schannel*) protocol engine must not specify algorithms and key sizes not supported by the CSP. For more information, see [Enumerating Supported Protocols](enumerating-supported-protocols.md). If unsupported algorithms or key sizes are specified, the CSP function must fail and return the NTE\_BAD\_DATA error code.

 

 

 



