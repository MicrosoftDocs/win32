---
description: This section describes best practices for porting an IPv6 broadcast application to the multicast capabilities available with Windows Sockets.
ms.assetid: 12e491fd-650f-43b4-afa1-9f37b1c30240
title: Porting Broadcast Applications to IPv6
ms.topic: article
ms.date: 05/31/2018
---

# Porting Broadcast Applications to IPv6

This section describes best practices for porting an IPv6 broadcast application to the multicast capabilities available with Windows Sockets.

## Comparing IPv4 to IPv6

The most notable consideration when preparing to port an IPv4 broadcast application to IPv6 is this: IPv6 has no implemented concept of broadcast. Instead, IPv6 uses multicast.

Multicast for IPv6 can emulate traditional broadcast capabilities found in IPv4. Setting the [IPV6\_ADD\_MEMBERSHIP](ipproto-ipv6-socket-options.md) socket option with the IPv6 address set to the link-local scope all nodes address (FF02::1) is equivalent to broadcasting on IPv4 broadcast addresses using the [SO\_BROADCAST](socket-options.md) socket option. This address is sometimes called the *all-nodes multicast group*. For applications that simply want broadcast emulation for IPv6, that approach is operationally equivalent. One notable difference with IPv6, however, is that multicasts on the all-nodes multicast group address are not received by default (IPv4 broadcasts are received by default). Application programmers must use the IPV6\_ADD\_MEMBERSHIP socket option to enable multicast reception from any source, including the all-nodes multicast group address.

> [!Note]  
> In IPv6, interface selection is specified in the argument structure passed to the multicast socket option or IOCTL.

 

But for richer, more robust, more selective and more manageable transmissions to multiple hosts, application developers should consider moving to a multicast model.

## Moving to Multicast

With multicast, application programmers can selectively choose a particular source/group pair, enabling a selective reception model. The Multicast Listener Discovery (MLD) on IPv6 and version 3 of the Internet Group Management Protocol (IGMPv3) on IPv4 support multicasting programming. In addition, multicast enables applications to specifically block (or unblock) senders within a group, further protecting applications from rogue broadcasters. This capability is available for IPv4 (requires IGMPv3) as well as IPv6 (requires MLDv2).

There are two primary scenarios for application programmers using multicast: those porting from IPv4 broadcast (or multicast) applications to IPv6, and those creating new IPv6 multicast applications.

For porting existing applications, there are two options to move to IPv6 multicast: using socket options and using IOCTLs.

-   Using socket options is a change-based approach, which enables developers to change the socket properties as required (such as blocking or unblocking a sender, adding a new source, and so on). This approach is more intuitive and the recommended approach. For more information on the change-based approach to multicast programming, see [MLD and IGMP Using Windows Sockets](igmp-and-windows-sockets.md).
-   Using IOCTLs is a final-state based approach, because it enables developers to provide a fully-configured socket state, including inclusion and exclusion lists, with one call. For more information on the final-state based approach, see [Final-State-Based Multicast Programming](final-state-based-multicast-programming.md).

For those creating new IPv6 multicast applications, the recommended practice is to use socket options, rather than using IOCTLs.

There is one other approach to creating multicast applications with IPv6, and that entails using the [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) function. While using the **WSAJoinLeaf** function is not the recommended practice, there are situations that may dictate its use. For example, one drawback to using socket options on Windows Server 2003 and earlier is that they are IP version specific. On these older versions of Windows, different sockets options must be for IPv6 and IPv4. On Windows Vista and later, new socket options are supported that can be used with both IPv4 and IPv6. The **WSAJoinLeaf** function, in contrast, is IP version and protocol agnostic, and therefore it can be a useful approach for building an application that must work with multiple IP versions on Windows Server 2003 and earlier. Using the **WSAJoinLeaf** function may be more appropriate in certain situations where protocol and IP-version agnosticism is required.

 

 



