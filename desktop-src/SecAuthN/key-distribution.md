---
description: The secret key authentication technique does not explain how the client and server get the secret session key to use in sessions with each other.
ms.assetid: 90ab0359-5079-49e9-809c-0c0005cc61bf
title: Key Distribution
ms.topic: article
ms.date: 05/31/2018
---

# Key Distribution

The secret key authentication technique does not explain how the client and server get the secret [*session key*](../secgloss/s-gly.md) to use in sessions with each other. If they are people, they could meet in secret and agree on the key. But if the client is a program running on a workstation and the server is a service running on a network server, that method will not work.

A client will want to communicate with many servers and will need different keys for each of them. A server communicates with many clients and needs different keys for each of them, as well. If each client needs a different key for every server, and each server needs a different key for every client, key distribution becomes a problem. In addition, the need to store and protect many keys on many computers creates an enormous security risk.

The name of the [*Kerberos protocol*](../secgloss/k-gly.md) suggests its solution to the problem of key distribution. Kerberos (or Cerberus) was a figure in classical Greek mythology—a fierce, three-headed dog who kept living intruders from entering the Underworld. Like the mythical guard, the Kerberos protocol has three heads: a client, a server, and a trusted third party to mediate between them. The trusted intermediary in this protocol is the Key Distribution Center (KDC).

The KDC is a service running on a physically secure server. It maintains a database with account information for all [*security principals*](../secgloss/s-gly.md) in its realm. A realm is the Kerberos equivalent of a domain in Windows.

Along with other information about each security principal, the KDC stores a cryptographic key known only to the principal and the KDC. This is the [*master key*](../secgloss/m-gly.md) used in exchanges between each security principal and the KDC. In most implementations of the Kerberos protocol, this master key is derived using a [*hash*](../secgloss/h-gly.md) function from a security principal's password.

When a client wants to create a secure connection with a server, the client begins by sending a request to the KDC, not to the server that it wants to reach. The KDC creates and sends to the client a unique [*session key*](../secgloss/s-gly.md) for the client and a server to use to authenticate each other. The KDC has access to both the client's master key and the server's master key. The KDC encrypts the server's copy of the session key using the server's master key, and the client's copy using the client's master key.

The KDC could fulfill its role as trusted intermediary by sending the session key directly to each of the security principals involved, but in practice this procedure will not work, for a number of reasons. Instead, the KDC sends both encrypted session keys to the client. The session key for the server is included in a [session ticket](session-tickets.md).

 

 
