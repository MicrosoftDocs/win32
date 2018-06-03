---
Description: The Schannel protocol engine performs the handshaking and authentication in a secure process and the bulk encryption/message passing in the application process.
ms.assetid: bcd49aaf-b0e3-4c31-be95-986b8ad843a8
title: Crossing Process Boundaries
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Crossing Process Boundaries

The [*Schannel*](https://www.bing.com/search?q=*Schannel*) protocol engine performs the handshaking and authentication in a secure [*process*](https://www.bing.com/search?q=*process*) and the bulk encryption/message passing in the application process. This means that the [*bulk encryption keys*](https://www.bing.com/search?q=*bulk encryption keys*) and [*MAC*](https://www.bing.com/search?q=*MAC*) keys must be copied from one process to another. To copy the keys from one process to another, use the [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey) and [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey) functions as follows:

1.  The secure process exports each key into an [*OPAQUEKEYBLOB*](https://www.bing.com/search?q=*OPAQUEKEYBLOB*) using [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey), then destroys the key using [**CryptDestroyKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroykey). Note that if the key is stored in hardware, the CSP must recognize this and must not attempt to destroy the key.
2.  The secure process passes the OPAQUEKEYBLOBs to the application process in a manner beyond the scope of this document.
3.  The application process imports each OPAQUEKEYBLOB back into the CSP using [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey). At this point, the key must be in exactly the same [*state*](https://www.bing.com/search?q=*state*) as when it was exported.

 

 



