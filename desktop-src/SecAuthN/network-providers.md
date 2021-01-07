---
description: A network provider is a DLL that supports a specific network protocol.
ms.assetid: 'ebd47c1b-f427-4fa1-a2ec-1e73be297bef'
title: Network Providers
ms.topic: article
ms.date: 05/31/2018
---

# Network Providers

A network provider is a DLL that supports a specific network protocol. It also implements the [Network Provider API](network-provider-api.md). This enables it to interact with the Windows operating system to receive standard network requests, such as connection or disconnection requests. To handle these requests, the network provider then calls the network-specific API that is appropriate to the network protocol the network provider supports. In other words, the network provider wraps the network-specific functionality in a DLL, which exposes a standard interface to Windows.

Using network providers, Windows can support many different types of network protocols without having to know the network-specific details of each network. This is essential because new network protocols are being developed all the time. With network providers, supporting a new protocol simply requires creating and installing a new network provider.

For information about network provider functions and structures, see the following topics:

-   [Network Provider Functions](authentication-functions.md)
-   [Network Provider Structures](authentication-structures.md)

 

 



