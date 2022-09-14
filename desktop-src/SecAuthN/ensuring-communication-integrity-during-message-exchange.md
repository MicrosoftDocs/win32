---
description: After a security context is established, the application can use the message support functions to transmit tamper-resistant messages.
ms.assetid: 43d7b940-1816-429f-be6e-40978efed278
title: Ensuring Communication Integrity During Message Exchange
ms.topic: article
ms.date: 05/31/2018
---

# Ensuring Communication Integrity During Message Exchange

After a [*security context*](/windows/desktop/SecGloss/s-gly) is established, the application can use the [message support](authentication-functions.md) functions to transmit tamper-resistant messages.

The client or server passes the security context and a message to the [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) function to generate a secure signature that prevents the message from being modified while in transit. The receiver of the message calls the [**VerifySignature**](/windows/desktop/api/Sspi/nf-sspi-verifysignature) function. **VerifySignature** uses the information in the signature to verify that the message received was not modified during transmission. The client and server can also exchange encrypted messages using [**EncryptMessage (General)**](/windows/win32/api/sspi/nf-sspi-encryptmessage) and [**DecryptMessage (General)**](/windows/win32/api/sspi/nf-sspi-decryptmessage).

The server in an authenticated connection can also make connections with other remote computers in the name of the client after calling [**ImpersonateSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-impersonatesecuritycontext).

 

 
