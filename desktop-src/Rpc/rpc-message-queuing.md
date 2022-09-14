---
title: RPC Message Queuing
description: Message Queuing (MSMQ) lets users communicate across networks and systems regardless of the current state of the communicating applications and systems.
ms.assetid: f1c8665b-3754-4c2e-b3ac-bba1f4b329e1
keywords:
- Remote Procedure Call RPC , described, message queuing
ms.topic: article
ms.date: 05/31/2018
---

# RPC Message Queuing

Message Queuing (MSMQ) lets users communicate across networks and systems regardless of the current state of the communicating applications and systems. Applications send and receive messages through message queues that MSMQ maintains. The message queues continue to function even when the client or server application is not running. Message queuing provides:

-   **Asynchronous messaging.** With MSMQ asynchronous messaging, a client application can send a message to a server and return immediately, even if the target computer or server program is not responding.
-   **Guaranteed message delivery.** When an application sends a message through MSMQ, the message will reach its destination even if the destination application is not running at the same time or the networks and systems are offline.
-   **Routing and dynamic configuration.** MSMQ provides flexible routing over heterogeneous networks. The configuration of such networks can be changed dynamically without any major changes to systems and networks themselves.
-   **Connectionless messaging.** Applications using MSMQ do not need to set up direct sessions with target applications.
-   [Security](security.md). MSMQ provides secure communication based on Windows security and the Cryptographic API (CryptoAPI) for encryption and digital signatures.
-   **Prioritized Messaging.** MSMQ transfers messages across networks based on priority, allowing faster communication for critical applications.

Microsoft RPC extends the Open Software Foundation–Data Communications Equipment (OSF-DCE) model for remote procedure calls by allowing distributed applications to use MSMQ as a transport and to control many of its features. This functionality is available both to conventional RPC applications and, through the **IRPCOptions** interface, to COM applications.

> [!Note]  
> RPC message queuing is available only on Windows 2000. Later versions of Windows do not support RPC message queuing.

 

The following topics provide an overview of message queuing:

-   [Overview of Message Queuing Services Architecture](overview-of-message-queuing-services-architecture.md)
-   [Message and Message Queue Properties](message-and-message-queue-properties.md)
-   [Using MSMQ as an RPC Transport](using-msmq-as-an-rpc-transport.md)
-   [System Requirements for RPC-Message\_Queuing Applications](system-requirements-for-rpc-message-queuing-applications.md)
-   [Developing RPC-Message Queuing Applications](developing-rpc-message-queuing-applications.md)
-   [MSMQ Security Services](msmq-security-services.md)

 

 




