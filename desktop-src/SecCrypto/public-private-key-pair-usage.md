---
Description: All normal RSA/Schannel and Diffie-Hellman/Schannel operations use the AT\_KEYEXCHANGE public/private key pair.
ms.assetid: e12afdbb-7ba8-444e-a43f-e262b481a353
title: Public/Private Key Pair Usage
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Public/Private Key Pair Usage

All normal [*RSA*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)/Schannel and [*Diffie-Hellman*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2)/Schannel operations use the AT\_KEYEXCHANGE [*public/private key pair*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a). To provide server [*authentication*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02), the server-side of Schannel operations must have access to its [*X.509*](https://msdn.microsoft.com/28dba6ef-939f-4789-9789-ee6e0fef0177) certificate containing its public key and access to the matching [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a). The client-side of [*Schannel*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) needs its certificate with its public key and access to its private key if client authentication is implemented.

Since Schannel protocol engines never use the AT\_SIGNATURE public/private key pair, that key pair need not be supported by a new CSP supporting only RSA/Schannel or Diffie-Hellman/Schannel.

If a protocol engine uses an SSL 3.0 export cipher suite with an AT\_KEYEXCHANGE key pair larger than 512 bits, the server must use an additional RSA key pair. This additional key pair is always exactly 512 bits and it can be ephemeral. The pair is stored as an AT\_KEYEXCHANGE element in a key container owned by the protocol engine. A handle to this key container is typically acquired at protocol engine startup.

Diffie-Hellman supports only [*CALG\_DH\_EPHEM*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) and uses normal RSA or DSS public keys.

 

 



