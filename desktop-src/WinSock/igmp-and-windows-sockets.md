---
description: Windows Sockets enables the Multicast Listener Discovery (MLD) on IPv6 and the Internet Group Management Protocol (IGMP) on IPv4 for multicast applications through the use of socket options and IOCTLs.
ms.assetid: a5de4273-e86e-4f13-b068-256cb38706d4
title: MLD and IGMP Using Windows Sockets
ms.topic: article
ms.date: 05/31/2018
---

# MLD and IGMP Using Windows Sockets

Windows Sockets enables the Multicast Listener Discovery (MLD) on IPv6 and the Internet Group Management Protocol (IGMP) on IPv4 for multicast applications through the use of socket options and IOCTLs. This page describes the socket options that enable multicast programming, and describes how they are used. For definitions of each socket option, consult the [Socket Options](socket-options.md) page.

For information on using IOCTLs for multicast programming, see [Final-State-Based Multicast Programming](final-state-based-multicast-programming.md) later in this section.

On Windows Vista and later, a set of socket options are available for multicast programming that support IPv6 and IPv4 addresses. These socket options are IP agnostic and can be used on both IPv6 and IPv4. On IPv6, these socket options use MLDv2. On IPv4, these socket options use IGMPv3. These IP agnostic options are the preferred socket options for multicast programming on Windows Vista and later. Windows Sockets uses the following socket options: 

| Socket option               | Argument type                                            |
|-----------------------------|----------------------------------------------------------|
| MCAST\_BLOCK\_SOURCE        | [**GROUP\_SOURCE\_REQ**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_source_req) structure |
| MCAST\_JOIN\_GROUP          | [**GROUP\_REQ**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_req) structure                |
| MCAST\_JOIN\_SOURCE\_GROUP  | [**GROUP\_SOURCE\_REQ**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_source_req) structure |
| MCAST\_LEAVE\_GROUP         | [**GROUP\_REQ**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_req) structure                |
| MCAST\_LEAVE\_SOURCE\_GROUP | [**GROUP\_SOURCE\_REQ**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_source_req) structure |
| MCAST\_UNBLOCK\_SOURCE      | [**GROUP\_SOURCE\_REQ**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-group_source_req) structure |



 

A set of socket options are available for multicast programming that support IPv6 only addresses. These socket options use MLDv1 or MLDv2. The version of MLD used is dependent on the version of Windows. MLDv2 is supported on Windows Vista and later. Windows Sockets uses the following socket options: 

| Socket option          | Argument type                             |
|------------------------|-------------------------------------------|
| IPV6\_ADD\_MEMBERSHIP  | [**ipv6\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ipv6_mreq) structure |
| IPV6\_DROP\_MEMBERSHIP | [**ipv6\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ipv6_mreq) structure |



 

A set of socket options are available for multicast programming that support IPv4 only addresses. These socket options use IGMPv3 or IGMPv2. The version of IGMP used is dependent on the version of Windows. IGMPv3 is supported on Windows Vista and later. Windows Sockets uses the following socket options:

| Socket option                | Argument type                                        |
|------------------------------|------------------------------------------------------|
| IP\_ADD\_MEMBERSHIP          | [**ip\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq) structure                |
| IP\_ADD\_SOURCE\_MEMBERSHIP  | [**ip\_mreq\_source**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq_source) structure |
| IP\_BLOCK\_SOURCE            | [**ip\_mreq\_source**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq_source) structure |
| IP\_DROP\_MEMBERSHIP         | [**ip\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq) structure                |
| IP\_DROP\_SOURCE\_MEMBERSHIP | [**ip\_mreq\_source**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq_source) structure |
| IP\_UNBLOCK\_SOURCE          | [**ip\_mreq\_source**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq_source) structure |



 

When IGMPv3 is available, the IP\_ADD\_SOURCE\_MEMBERSHIP, IP\_BLOCK\_SOURCE, IP\_DROP\_SOURCE\_MEMBERSHIP, and IP\_UNBLOCK\_SOURCE options are handled more efficiently since the router can handle the filtering. When only IGMPv2 is available, the host must handle the filtering.

There are two categories into which most applications are likely to fall: any-source and controlled-source.

-   **Any-source** applications accept all sources by default, allowing individual sources to be turned off as required. An example of an any-source application is a video conference call that enables all recipients to participate.
-   **Controlled-source** applications limit sources to a given list, such as an Internet radio station, or the broadcast of a notable event. The process of using socket options is slightly different for each.

On Windows Vista and later, the following steps apply for any-source applications:

- Use **MCAST\_JOIN\_GROUP** to join a group.  
- Use **MCAST\_BLOCK\_SOURCE** to turn off a given source, if required.  
- Use **MCAST\_UNBLOCK\_SOURCE** to re-allow a blocked source, if required.  
- Use **MCAST\_LEAVE\_GROUP** to leave the group.  

On Windows Vista and later, the following steps apply for controlled-source applications:

- Use **MCAST\_JOIN\_SOURCE\_GROUP** to join each group/source pair.  
- Use **MCAST\_LEAVE\_SOURCE\_GROUP** to leave each group/source, or use **MCAST\_LEAVE\_GROUP** to leave all sources, if the same group address is used by all sources.  

The following steps apply for any-source applications:

- Use **IP\_ADD\_MEMBERSHIP** to join a group (**IPV6\_ADD\_MEMBERSHIP** for IPv6).  
- Use **IP\_BLOCK\_SOURCE** to turn off a given source, if required.  
- Use **IP\_UNBLOCK\_SOURCE** to re-allow a blocked source, if required.  
- Use **IP\_DROP\_MEMBERSHIP** to leave the group (**IPV6\_DROP\_MEMBERSHIP** for IPv6).  

The following steps apply for controlled-source applications:

- Use **IP\_ADD\_SOURCE\_MEMBERSHIP** to join each group/source pair.  
- Use **IP\_DROP\_SOURCE\_MEMBERSHIP** to leave each group/source, or use **IP\_DROP\_MEMBERSHIP** to leave all sources, if the same group address is used by all sources.  

The order in which these socket options are set has associated rules. For information and troubleshooting information on multicast socket options, see [Multicast Socket Option Behavior](multicast-socket-option-behavior.md).
