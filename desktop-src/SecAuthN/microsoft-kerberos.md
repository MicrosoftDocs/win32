---
description: The Kerberos protocol defines how clients interact with a network authentication service \[Platform Software Development Kit (SDK)\].
ms.assetid: e7870e72-1386-4818-bf6f-73430ae942a8
title: Microsoft Kerberos
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Kerberos

The [*Kerberos protocol*](../secgloss/k-gly.md) defines how clients interact with a network authentication service. Clients obtain tickets from the Kerberos Key Distribution Center (KDC), and they present these tickets to servers when connections are established. Kerberos tickets represent the client's network [*credentials*](../secgloss/c-gly.md).

Information in this section provides theoretical background on the use of the Kerberos protocol in an authentication process. This is background information that can add to a developer's understanding of what is happening behind the scenes in an SSPI process that uses the Kerberos Version 5 protocol.

The Kerberos authentication protocol provides a mechanism for mutual authentication between entities before a secure network connection is established. Throughout this documentation, the two entities are called the client and the server even though secure network connections can be made between servers. Both client and server can also be referred to as [*security principals*](../secgloss/s-gly.md).

The Kerberos protocol assumes that transactions between clients and servers take place on an open network where most clients and many servers are not physically secure, and packets traveling along the network can be monitored and modified at will. The assumed environment is like today's Internet where an attacker can easily pose as either a client or a server, and can readily eavesdrop on or tamper with communications between legitimate clients and servers.

This section provides the following information:

-   [Basic Authentication Concepts](basic-authentication-concepts.md)
-   [Kerberos Subprotocols](kerberos-subprotocols.md)
-   [Kerberos Model](kerberos-components.md)
-   [SSPI/Kerberos Interoperability with GSSAPI](sspi-kerberos-interoperability-with-gssapi.md)

Your application should not access the Kerberos [*security package*](../secgloss/s-gly.md) directly; instead, it should use the [*Negotiate*](../secgloss/n-gly.md) security package. Negotiate allows your application to take advantage of more advanced [*security protocols*](../secgloss/s-gly.md) if they are supported by the systems involved in the authentication. Currently, the Negotiate security package selects between [*Kerberos*](../secgloss/k-gly.md) and NTLM. Negotiate selects Kerberos unless it cannot be used by one of the systems involved in the authentication.

 

 
