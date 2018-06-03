---
Description: The semantics for datagram, or connectionless, contexts differ slightly from those for connection-oriented contexts.
ms.assetid: f312796c-cbe6-4be9-9886-52fdb34ced6b
title: Datagram Contexts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Datagram Contexts

The semantics for [*datagram*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-datagram-gly), or connectionless, contexts differ slightly from those for connection-oriented contexts. In a datagram's connectionless [*context*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-context-gly), a server cannot determine when the client has shut down or otherwise terminated the connection. In other words, no termination notice is passed from the transport application to the server as would occur in a connection-oriented context.

To use a datagram context, a client sets the ISC\_REQ\_DATAGRAM flag in its call to the [**InitializeSecurityContext (General)**](/windows/desktop/api/Sspi/) function.

> \[!Important\]  
> The [Microsoft Kerberos](microsoft-kerberos.md) package does not support datagram contexts in user-to-user mode.

 

To better support some models, particularly DCE-style RPC, the following rules apply when the client uses a datagram context:

-   The [*security package*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-package-gly) does not produce an authentication [*BLOB*](https://msdn.microsoft.com/library/windows/desktop/ms721569#-security-blob-gly) (binary large object) on the first call to [**InitializeSecurityContext (General)**](/windows/desktop/api/Sspi/). However, the client can use the returned security context in a call to the [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) function to generate a signature for a message.
-   The security package must allow for the context to be re-established multiple times to allow the server to drop the connection without notice. This implies that any keys used in the [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) and [**VerifySignature**](/windows/desktop/api/Sspi/nf-sspi-verifysignature) functions can be reset to a consistent [*state*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-state-gly).
-   The security package allows the caller to specify sequence information, and provides that sequence information at the receiver side. This is in addition to any sequence information maintained by the package.

A security package sets the SECPKG\_FLAG\_DATAGRAM flag to indicate that it supports datagram semantics.

 

 



