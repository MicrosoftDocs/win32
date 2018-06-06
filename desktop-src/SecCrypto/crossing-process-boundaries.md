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

The [*Schannel*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) protocol engine performs the handshaking and authentication in a secure [*process*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) and the bulk encryption/message passing in the application process. This means that the [*bulk encryption keys*](https://msdn.microsoft.com/2e570727-7da0-4e17-bf5d-6fe0e6aef65b) and [*MAC*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1) keys must be copied from one process to another. To copy the keys from one process to another, use the [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey) and [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey) functions as follows:

1.  The secure process exports each key into an [*OPAQUEKEYBLOB*](https://msdn.microsoft.com/e6be8932-015e-4058-b249-1671b3fea521) using [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey), then destroys the key using [**CryptDestroyKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroykey). Note that if the key is stored in hardware, the CSP must recognize this and must not attempt to destroy the key.
2.  The secure process passes the OPAQUEKEYBLOBs to the application process in a manner beyond the scope of this document.
3.  The application process imports each OPAQUEKEYBLOB back into the CSP using [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey). At this point, the key must be in exactly the same [*state*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) as when it was exported.

 

 



