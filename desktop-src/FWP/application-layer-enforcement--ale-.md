---
title: Application Layer Enforcement (ALE)
description: ALE is a set of Windows Filtering Platform (WFP) kernel-mode layers that are used for stateful filtering.
ms.assetid: ffebd312-9220-476c-a4ba-28e2e8ac8879
ms.topic: article
ms.date: 05/31/2018
---

# Application Layer Enforcement (ALE)

ALE is a set of Windows Filtering Platform (WFP) kernel-mode layers that are used for stateful filtering.

Stateful filtering keeps track of the state of network connections and allows only packets that match a known connection state. For example, stateful filtering for a TCP connection initiated from behind a firewall can allow only incoming packets that match previous outgoing packets sent by the party protected.

Filters in the ALE layers authorize inbound and outbound connection creation, port assignments, socket operations such as [**listen()**](/windows/desktop/api/winsock2/nf-winsock2-listen), raw socket creation, and promiscuous mode receiving.

Traffic at the ALE layers is classified either per-connection or per-socket operation. At non-ALE layers, filters can only classify traffic on a per-packet basis.

ALE layers are the only WFP layers where network traffic can be filtered based on the application identity—using a normalized file name—and based on the user identity—using a security descriptor. (See FLT\_FILE\_NAME\_INFORMATION in the Windows Driver Kit (WDK) documentation, for more information on normalized file names.)

In addition, when IPsec is used to secure the connection, filtering at ALE layers can also be performed on the remote machine identity and on the remote user identity. The remote machine and user identities are obtained from the credentials used in the creation of an IPsec session.

For this reason, policies that enforce who (for example, "administrator") and/or which application (for example, "Internet Explorer") are allowed to perform the network operations mentioned above are authored at the ALE layers.

ALE provides enforcement for policies such as "allow Windows Messenger all access to the network while blocking all other applications." In such an example, when the application "Messenger" connects across the network, ALE traps the event, determines that it was initiated by Messenger and queries the WFP filter engine to determine whether the socket should be allowed to proceed.

> [!Note]  
> Due to the nature of true dual-IP sockets, classifications at the IPv4 ALE layer may not occur. This is by design, because for all intents and purposes, the socket is an IPv6 socket. To see the V4 traffic for such a socket, create filters at the V6 layer using the IPv6-mapped address.

 

## Related topics

<dl> <dt>

[ALE Layers](ale-layers.md)
</dt> <dt>

[ALE Stateful Filtering](ale-stateful-filtering.md)
</dt> <dt>

[ALE Multicast/Broadcast Traffic](ale-multicast-broadcast-traffic.md)
</dt> <dt>

[ALE Reauthorization](ale-re-authorization.md)
</dt> <dt>

[ALE Flow Customization](ale-flow-customization.md)
</dt> </dl>

 

 