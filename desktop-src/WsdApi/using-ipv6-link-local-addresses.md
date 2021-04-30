---
description: IPv6 link-local addressing in SOAP messages provides a unique challenge, as IPv6 link-local addresses require a scope ID to be meaningful, but the scope ID only has meaning for the local machine.
ms.assetid: 63495335-e447-4564-b669-0896c7aac63f
title: Using IPv6 Link-Local Addresses
ms.topic: article
ms.date: 05/31/2018
---

# Using IPv6 Link-Local Addresses

IPv6 link-local addressing in SOAP messages provides a unique challenge, as IPv6 link-local addresses require a scope ID to be meaningful, but the scope ID only has meaning for the local machine. All client and device implementations must remove the scope ID before sending an IPv6 link-local address in a SOAP message. Additionally, when an IPv6 link-local address is received in a message, the interface the message was received on must be known so the complete link local address with scope ID can be reconstructed.

 

 



