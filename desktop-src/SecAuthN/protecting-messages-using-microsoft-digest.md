---
Description: Explains how to protect messages using Microsoft Digest.
ms.assetid: 15509d51-80c0-4d5c-aa24-4dc17de3f12c
title: Protecting Messages Using Microsoft Digest
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Protecting Messages Using Microsoft Digest

## HTTP and SASL

As a means of detecting certain types of security violations, the client and server use the [security support provider interface](sspi.md) (SSPI) message [*integrity*](security.i_gly#-security-integrity-gly) functions [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) and [**VerifySignature**](/windows/desktop/api/Sspi/nf-sspi-verifysignature) to protect messages.

A client calls the [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) function to sign a message using its [*security context*](security.s_gly#-security-security-context-gly). The server uses the [**VerifySignature**](/windows/desktop/api/Sspi/nf-sspi-verifysignature) function to verify the message's origin. In addition to verifying the [*signature*](security.d_gly#-security-digital-signature-gly) that accompanies the message, the **VerifySignature** function also checks that the [*nonce*](security.n_gly#-security-nonce-gly) count (specified by the nc directive) is one greater than the last count sent for the nonce. If this is not the case, the **VerifySignature** function returns an SEC\_OUT\_OF\_SEQUENCE error code.

## SASL Only

The [**EncryptMessage (General)**](/windows/desktop/api/Sspi/) and [**DecryptMessage (General)**](/windows/desktop/api/Sspi/) functions supply confidentiality for post-authentication messages exchanged between client and server.

In order to use the message confidentiality functions, the server and client must have established a [*security context*](security.s_gly#-security-security-context-gly) with the following attributes:

-   Quality of protection, specified by the qop directive, must be "auth-conf".
-   An encryption mechanism must have been specified by means of the cipher directive.

 

 



