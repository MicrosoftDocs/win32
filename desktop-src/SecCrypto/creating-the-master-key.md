---
Description: A master key is key data material from which other keys are derived.
ms.assetid: c8445f74-659a-470b-9007-07ea98d36dcd
title: Creating the Master Key
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating the Master Key

A [*master key*](security.m_gly#-security-master-key-gly) is key data material from which other keys are derived. Depending on the protocol and cipher suite used, the master key can be from 5 to 48 bytes in length. For the [*RSA*](security.r_gly#-security-rsa-gly)/[*Schannel*](security.s_gly#-security-schannel-gly) CSP, the master key is created by the client-side and transferred to the server in an RSA envelope. For a [*Diffie-Hellman*](security.d_gly#-security-diffie-hellman-algorithm-gly)/Schannel CSP, the master key is created by performing a Diffie-Hellman key exchange.

Code for creating and exchanging master keys is demonstrated in:

-   [Diffie-Hellman Client Code for Creating the Master Key](diffie-hellman-client-code-for-creating-the-master-key.md)
-   [Diffie-Hellman Server Code for Creating the Master Key](diffie-hellman-server-code-for-creating-the-master-key.md)
-   [RSA Client Code for Creating the Master Key](rsa-client-code-for-creating-the-master-key.md)
-   [RSA Server Code for Creating the Master Key](rsa-server-code-for-creating-the-master-key.md)
-   [Specifying the Algorithms](specifying-the-algorithms.md)

 

 



