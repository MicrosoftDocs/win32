---
description: The Security Support Provider Interface (SSPI) model provides a single interface for a client/server transport application using the various security packages available on a computer or network.
ms.assetid: ffd7e531-3e0e-40c4-865e-34fa24321655
title: Procedures Used with Most Security Packages and Protocols
ms.topic: article
ms.date: 05/31/2018
---

# Procedures Used with Most Security Packages and Protocols

The [*Security Support Provider Interface*](../secgloss/s-gly.md) (SSPI) model provides a single interface for a client/server transport application using the various [*security packages*](../secgloss/s-gly.md) available on a computer or network. SSPI allows an application to use a security package without dealing with the underlying [*security protocols*](../secgloss/s-gly.md) of the package. At the same time, SSPI also allows sophisticated, security-aware applications to take advantage of the advanced capabilities of specific security packages.

Applications initialize SSPI using the following steps to secure a network connection for most security packages:

-   [Using SecBufferDesc and SecBuffer](using-secbufferdesc-and-secbuffer.md)
-   [Initializing SSPI](initializing-sspi.md)
-   [Establishing a Secure Connection with Authentication](establishing-a-secure-connection-with-authentication.md)
-   [Ensuring Communication Integrity During Message Exchange](ensuring-communication-integrity-during-message-exchange.md)
-   [Ending an SSPI Session](ending-an-sspi-session.md)

 

 
