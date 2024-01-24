---
description: A master key is key data material from which other keys are derived.
ms.assetid: c8445f74-659a-470b-9007-07ea98d36dcd
title: Creating the Master Key
ms.topic: article
ms.date: 05/31/2018
---

# Creating the Master Key

A [*master key*](../secgloss/m-gly.md) is key data material from which other keys are derived. Depending on the protocol and cipher suite used, the master key can be from 5 to 48 bytes in length. For the [*RSA*](../secgloss/r-gly.md)/[*Schannel*](../secgloss/s-gly.md) CSP, the master key is created by the client-side and transferred to the server in an RSA envelope. For a [*Diffie-Hellman*](../secgloss/d-gly.md)/Schannel CSP, the master key is created by performing a Diffie-Hellman key exchange.

Code for creating and exchanging master keys is demonstrated in:

-   [Diffie-Hellman Client Code for Creating the Master Key](diffie-hellman-client-code-for-creating-the-master-key.md)
-   [Diffie-Hellman Server Code for Creating the Master Key](diffie-hellman-server-code-for-creating-the-master-key.md)
-   [RSA Client Code for Creating the Master Key](rsa-client-code-for-creating-the-master-key.md)
-   [RSA Server Code for Creating the Master Key](rsa-server-code-for-creating-the-master-key.md)
-   [Specifying the Algorithms](specifying-the-algorithms.md)

 

 
