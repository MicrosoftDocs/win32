---
title: Protocol Identifiers
description: The following protocol identifiers are also listed in Routprot.h for the Windows SDK, and iprtmib.h for the Platform Software Development Kit (SDK).
ms.assetid: f67138b8-de5d-4907-a464-672d57864ebf
ms.topic: article
ms.date: 05/31/2018
---

# Protocol Identifiers

The following protocol identifiers are also listed in Routprot.h for the Windows SDK, and iprtmib.h for the Platform Software Development Kit (SDK).

## IP Protocols

The following routing protocols are associated with the IP transport.



| Protocol                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROTO\_IP\_OTHER, MIB\_IPPROTO\_OTHER                        | Some other protocol not specified in RFC 1354.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PROTO\_IP\_LOCAL, MIB\_IPPROTO\_LOCAL                        | A local interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PROTO\_IP\_NETMGMT, MIB\_IPPROTO\_NETMGMT                    | A static route. This value is used to identify route information for IP routing set through network management such as the Dynamic Host Configuration Protocol (DCHP), the Simple Network Management Protocol (SNMP), or by calls to the [**CreateIpForwardEntry**](/windows/desktop/api/iphlpapi/nf-iphlpapi-createipforwardentry), [**DeleteIpForwardEntry**](/windows/desktop/api/iphlpapi/nf-iphlpapi-deleteipforwardentry), or [**SetIpForwardEntry**](/windows/desktop/api/iphlpapi/nf-iphlpapi-setipforwardentry) functions.                                                                                              |
| PROTO\_IP\_ICMP, MIB\_IPPROTO\_ICMP                          | The result of ICMP redirect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PROTO\_IP\_EGP, MIB\_IPPROTO\_EGP                            | The Exterior Gateway Protocol (EGP), a dynamic routing protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PROTO\_IP\_GGP, MIB\_IPPROTO\_GGP                            | The Gateway-to-Gateway Protocol (GGP), a dynamic routing protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PROTO\_IP\_HELLO, MIB\_IPPROTO\_HELLO                        | The Hellospeak protocol, a dynamic routing protocol. This is a historical entry no longer in use and was an early routing protocol used by the original ARPANET routers that ran special software called the Fuzzball routing protocol, sometimes called Hellospeak, as described in RFC 891 and RFC 1305. For more information, see [https://www.ietf.org/rfc/rfc891.txt](https://www.ietf.org/rfc/rfc891.txt) and [https://www.ietf.org/rfc/rfc1305.txt](https://tools.ietf.org/html/rfc1305). |
| PROTO\_IP\_RIP, MIB\_IPPROTO\_RIP                            | The Berkeley Routing Information Protocol (RIP) or RIP-II, a dynamic routing protocol.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PROTO\_IP\_IS\_IS, MIB\_IPPROTO\_IS\_IS                      | The Intermediate System-to-Intermediate System (IS-IS) protocol, a dynamic routing protocol. The IS-IS protocol was developed for use in the Open Systems Interconnection (OSI) protocol suite.                                                                                                                                                                                                                                                                                                                      |
| PROTO\_IP\_ES\_IS, MIB\_IPPROTO\_ES\_IS                      | The End System-to-Intermediate System (ES-IS) protocol, a dynamic routing protocol. The ES-IS protocol was developed for use in the Open Systems Interconnection (OSI) protocol suite.                                                                                                                                                                                                                                                                                                                               |
| PROTO\_IP\_CISCO, MIB\_IPPROTO\_CISCO                        | The Cisco Interior Gateway Routing Protocol (IGRP), a dynamic routing protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PROTO\_IP\_BBN, MIB\_IPPROTO\_BBN                            | The Bolt, Beranek, and Newman (BBN) Interior Gateway Protocol (IGP) that used the Shortest Path First (SPF) algorithm. This was an early dynamic routing protocol.                                                                                                                                                                                                                                                                                                                                                   |
| PROTO\_IP\_OSPF, MIB\_IPPROTO\_OSPF                          | The Open Shortest Path First (OSPF) protocol, a dynamic routing protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PROTO\_IP\_BGP, MIB\_IPPROTO\_BGP                            | The Border Gateway Protocol (BGP), a dynamic routing protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PROTO\_IP\_BOOTP, MIB\_IPPROTO\_BOOTP                        | The Bootstrap Protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PROTO\_IPV6\_DHCPRELAY, MIB\_IPV6PROTO\_HDCPRELAY            | The DHCPv6 Relay protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PROTO\_IP\_NT\_AUTOSTATIC, MIB\_IPNT\_AUTOSTATIC             | A Windows specific entry added originally by a routing protocol, but which is now static.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PROTO\_IP\_NT\_STATIC, MIB\_IPNT\_STATIC                     | A Windows specific entry added as a static route from the routing user interface or a routing command.                                                                                                                                                                                                                                                                                                                                                                                                               |
| PROTO\_IP\_NT\_STATIC\_NON\_DOD, MIB\_IPNT\_STATIC\_NON\_DOD | A Windows specific entry added as a static route from the routing user interface or a routing command, except these routes do not cause Dial On Demand (DOD).                                                                                                                                                                                                                                                                                                                                                        |



 

Routes with a protocol identifier of PROTO\_IP\_LOCAL include:

-   The loopback route
-   The subnet route
-   All networks broadcast route for subnetted interfaces
-   All "1"s broadcast route
-   Local multicast route
-   Route to remote end of a PPP link

The identifier for the IP router manager is:

IPRTRMGR\_PID

This identifier can be used instead of a routing protocol identifier for MIB calls with the IP router manager. This identifier is used for MIB-II, Forwarding MIB, and some enterprise specific information. This identifier is also listed in Iprtrmib.h.

## IPX Protocols

The following routing protocols are associated with the IPX transport.



| Protocol            | Description                          |
|---------------------|--------------------------------------|
| IPX\_PROTOCOL\_RIP  | Routing Information Protocol for IPX |
| IPX\_PROTOCOL\_SAP  | Service Advertisement Protocol       |
| IPX\_PROTOCOL\_NLSP | NetWare Link Services Protocol       |



 

The identifier for the IPX router manager is:

IPX\_PROTOCOL\_BASE

Use this identifier instead of a routing protocol identifier for MIB calls with the IPX router manager.

 

 