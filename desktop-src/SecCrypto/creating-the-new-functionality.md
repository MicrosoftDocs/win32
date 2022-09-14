---
description: The following functions are among the CryptoAPI functions that can be extended.
ms.assetid: eb4c1352-1432-4f45-a309-fa17b694a35e
title: Creating the New Functionality
ms.topic: article
ms.date: 05/31/2018
---

# Creating the New Functionality

The following functions are among the CryptoAPI functions that can be extended.



| CryptoAPI function                                   | OID function name define                         | OID function name string  |
|------------------------------------------------------|--------------------------------------------------|---------------------------|
| [**CryptEncodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobject)       | CRYPT\_OID\_ENCODE\_ OBJECT\_FUNC<br/>     | "CryptDllEncodeObject"    |
| [**CryptDecodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobject)       | CRYPT\_OID\_DECODE\_ OBJECT\_FUNC<br/>     | "CryptDllDecodeObject"    |
| [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore)               | CRYPT\_OID\_OPEN\_ STORE\_PROV\_FUNC<br/>  | "CertDllOpenStoreProv"    |
| [**CertVerifyCTLUsage**](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifyctlusage)     | CRYPT\_OID\_VERIFY\_ CTL\_USAGE\_FUNC<br/> | "CertDllVerifyCTLUsage"   |
| [**CertVerifyRevocation**](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifyrevocation) | CRYPT\_OID\_VERIFY\_ REVOCATION\_FUNC<br/> | "CertDllVerifyRevocation" |



 

In normal use with an existing OID and encoding type, the code in the CryptoAPI function, itself, is used. If one of these functions is called with an OID and encoding type that code in the CryptoAPI function was not designed to handle, a new function, containing the new functionality, must be created in a DLL. That DLL must be registered in the registry or installed in memory.

When one of the listed functions is called with the newly designated OID and encoding type, the code in the new DLL is used rather than the code provided as part of the CryptoAPI function.

The name of the newly developed function can be the name listed under "OID function name string" in the previous table or a different name can be given when the new function code is registered.

The new function must use an appropriate prototype. In all cases except for [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore), this prototype is the same as the CryptoAPI function that calls the new function. In the case of **CertOpenStore** the prototype is as follows.


```C++
#include <windows.h>

BOOL WINAPI CertDllOpenStoreProv(
  IN LPCSTR lpszStoreProvider,
  IN DWORD dwEncodingType,
  IN HCRYPTPROV hCryptProv,
  IN DWORD dwFlags,
  IN const void *pvPara,
  IN HCERTSTORE hCertStore,
  IN OUT PCERT_STORE_PROV_INFO pStoreProvInfo
);
```



> [!Note]  
> If the prototypes do not match, the system stack will be corrupted.

 

In addition to providing the code for the new function in a DLL, extending the functionality of [**CryptEncodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobject) or [**CryptDecodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobject) requires a type definition for the new C data structure to be placed in a header file included when the user's program is compiled.

 

 




