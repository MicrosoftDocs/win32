---
description: Instead of sending the encrypted session keys to both of the principals, the KDC sends both the client's and the server's copies of the session key to the client.
ms.assetid: 6b20ab30-2cd9-4f2e-a26b-316980c4bc78
title: Session Tickets
ms.topic: article
ms.date: 05/31/2018
---

# Session Tickets

Instead of sending the encrypted session keys to both of the principals, the [KDC](key-distribution-center.md) sends both the client's and the server's copies of the [*session key*](../secgloss/s-gly.md) to the client. The client's copy of the session key is encrypted with the client's [*master key*](../secgloss/m-gly.md) and therefore cannot be decrypted by any other entity. The server's copy of the session key is embedded, along with authorization data about the client, in a data structure called a ticket. The ticket is entirely encrypted with the server's master key and therefore cannot be read or changed by the client or any other entity that does not have access to the server's master key. It is the responsibility of the client to store the ticket safely until contact with the server.

> [!Note]  
> The KDC only provides a ticket-granting service. The client and server are responsible for keeping their respective master keys secure.

 

When the client receives the KDC's response, it extracts the ticket and its own copy of the session key, putting both aside in a secure cache. To establish a secure session with the server, it sends the server a message consisting of the ticket, still encrypted with the server's master key, and an [authenticator message](authenticator-messages.md) encrypted with the session key. Together, the ticket and authenticator message are the client's [*credentials*](../secgloss/c-gly.md) to the server.

When the server receives credentials from a client, it decrypts the ticket with its [*master key*](../secgloss/m-gly.md), extracts the [*session key*](../secgloss/s-gly.md), and uses the session key to decrypt the client's authenticator message. If everything checks out, the server knows that the client's credentials were issued by the KDC, a trusted authority. For mutual authentication, the server responds by encrypting the time stamp from the client's authenticator message using the session key. This encrypted message is sent to the client. The client then decrypts the message. If the returned message is the same as the time stamp in the original authenticator message, the server is authenticated.

As an added benefit, the server does not need to store the session keys it uses with its clients. It is each client's responsibility to manage the ticket for the server in its ticket cache and to present that ticket each time it accesses the server. Whenever the server receives a ticket from a client, it uses its master key to decrypt the ticket and extract the session key. When the server no longer needs the session key, the key is deleted.

The client does not need to access the KDC each time it wants access to this particular server. Tickets can be reused. As a precaution against the possibility of ticket theft, tickets have an expiration time, specified by the KDC in the ticket structure. How long a ticket is valid depends on Kerberos policy for the realm. Typically, tickets are good for no longer than eight hours, about the length of a normal [*logon session*](../secgloss/l-gly.md). When the user at a client workstation logs off, the client ticket cache is flushed and all tickets and client session keys are destroyed.

 

 
