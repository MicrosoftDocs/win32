---
description: A network provider is a DLL that enables the Windows operating system to interact with other kinds of networks, such as Novell. It is a client of the Windows WNet driver.
ms.assetid: d316f159-4fe3-4b78-9efc-177906875918
title: Network Provider API
ms.topic: article
ms.date: 05/31/2018
---

# Network Provider API

A network provider is a DLL that enables the Windows operating system to interact with other kinds of networks, such as Novell. It is a client of the Windows WNet driver. A network provider implements network-specific actions, such as making a connection, and exposes a common interface to Windows. This interface is called the Network Provider API and consists of functions implemented by the network provider. You can create a network provider DLL to support new network protocols.

Because each network exposes a common interface through its provider, Windows can interact with several types of networks without knowing their network-specific implementation details.

The [*Multiple Provider Router*](../secgloss/m-gly.md) (MPR) handles communication with all of the various network providers on the system and presents an integrated network to the user.

## Related topics

<dl> <dt>

[Network Providers](network-providers.md)
</dt> <dt>

[Credential Manager](credential-manager.md)
</dt> <dt>

[Multiple Provider Router](multiple-provider-router.md)
</dt> <dt>

[Functions Implemented by Network Providers](functions-implemented-by-network-providers.md)
</dt> <dt>

[Credential Management API](credential-management-api.md)
</dt> <dt>

[Connection Notification API](connection-notification-api.md)
</dt> </dl>

 

 
