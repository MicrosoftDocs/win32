---
Description: Explains how to use SSPI message support.
ms.assetid: 14d4813e-413e-4ef9-85f0-96986c3c1eca
title: Using Message Support
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Message Support

After a handshake has been completed and a secure connection has been established, an application can use the [**MakeSignature**](/windows/win32/Sspi/nf-sspi-makesignature?branch=master), [**EncryptMessage (General)**](/windows/win32/Sspi/?branch=master), [**VerifySignature**](/windows/win32/Sspi/nf-sspi-verifysignature?branch=master), and [**DecryptMessage (General)**](/windows/win32/Sspi/?branch=master) functions to exchange signed or encrypted application data with the remote computer.

Examples that use these functions after a [*security context*](security.s_gly#-security-security-context-gly) has been established are demonstrated in the following sections:

-   [Signing a Message](signing-a-message.md)
-   [Verifying a Message](verifying-a-message.md)
-   [Encrypting a Message](encrypting-a-message.md)
-   [Decrypting a Message](decrypting-a-message.md)

 

 



