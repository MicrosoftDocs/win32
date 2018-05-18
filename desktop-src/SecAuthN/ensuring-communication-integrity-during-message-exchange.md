---
Description: 'After a security context is established, the application can use the message support functions to transmit tamper-resistant messages.'
ms.assetid: '43d7b940-1816-429f-be6e-40978efed278'
title: Ensuring Communication Integrity During Message Exchange
---

# Ensuring Communication Integrity During Message Exchange

After a [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) is established, the application can use the [message support](authentication-functions.md#message-support) functions to transmit tamper-resistant messages.

The client or server passes the security context and a message to the [**MakeSignature**](makesignature.md) function to generate a secure signature that prevents the message from being modified while in transit. The receiver of the message calls the [**VerifySignature**](verifysignature.md) function. **VerifySignature** uses the information in the signature to verify that the message received was not modified during transmission. The client and server can also exchange encrypted messages using [**EncryptMessage (General)**](encryptmessage--general-.md) and [**DecryptMessage (General)**](decryptmessage--general-.md).

The server in an authenticated connection can also make connections with other remote computers in the name of the client after calling [**ImpersonateSecurityContext**](impersonatesecuritycontext.md).

 

 



