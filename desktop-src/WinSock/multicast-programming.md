---
description: Multicast programming is enabled through Windows Sockets.
ms.assetid: 'f729945b-b469-4baf-ac06-2431ee2d0e71'
title: Multicast Programming
ms.topic: article
ms.date: 05/31/2018
---

# Multicast Programming

Multicast programming is enabled through Windows Sockets. Windows Sockets enables the Multicast Listener Discovery (MLD) versions 1 (MLDv1) and 2 (MLDv2) on IPv6 and the Internet Group Management Protocol versions 2 (IGMPv2) and 3 (IGMPv3) through the use of socket options or IOCTLs. This section describes the Windows implementation, explains how to enable multicast programming using Windows Sockets, and provides programming samples to illustrate its use.

The second version of IGMP, hereafter referred to as IGMPv2, enables hosts to join and leave multicast groups identified by an IPv4 multicast address on a specific network interface. Windows Sockets enables an application to join and leave such groups on specific sockets. A drawback of IGMPv2, however, is that any IPv4 source address joined to the IGMPv2 group can transmit to all members, potentially flooding the group and making it unusable for transmissions that require a primary source, such as an Internet radio station. The problem with IGMPv2 is its inability to selectively choose a single IPv4 source address (or even a few sources), and its inability to block senders (such as rogue broadcasters or denial-of-service perpetrators) for a given multicast group. IGMPv3 addresses those shortcomings.

With Windows Sockets and IGMPv3, applications can select a particular multicast IPv4 source address and multicast group pair. In addition, Windows Sockets enables developers to selectively allow additional broadcasters in a given source/group pair, or enables applications to block specific broadcasters. IGMPv3 is supported on Windows Vista and later.

The first version of MLD on IPv6, referred to as MLDv1, is very similar to IGMPv2 and suffers from the same limitations. MLDv1 enables hosts to join and leave multicast groups identified by an IPv6 multicast address on a specific network interface. Windows Sockets enables an application to join and leave such groups on specific sockets. However, any IPv6 source address joined to the MLDv1 group can transmit to all members, potentially flooding the group and making it unusable for transmissions that require a primary source. The problem with MLDv1 is its inability to selectively choose a single IPv6 source address (or even a few sources), and its inability to block senders (such as rogue broadcasters or denial-of-service perpetrators) for a given multicast group. MLDv2 addresses those shortcomings.

With Windows Sockets and MLDv2, applications can select a particular multicast IPv6 source address and multicast group pair. In addition, Windows Sockets enables developers to selectively allow additional broadcasters in a given source/group pair, or enables applications to block specific broadcasters. MLDv2 is supported on Windows Vista and later.

There are two approaches an application programmer can take when developing multicast applications in Windows. The first approach is change-based; multicast sources are added or removed using socket options, even during the course of transmission, as required. The second approach is final-state based; source addresses and any included/excluded addresses are specified with an IOCTL. Each approach is a valid multicasting practice, but developers may find using socket options and the change-based approach more intuitive and flexible.

This section has the following pages: 

| Page title                                                                             | Description                                                                                                                                                                        |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MLD and IGMP Using Windows Sockets](igmp-and-windows-sockets.md)                     | Enumerates the multicast socket options available for use in Windows Sockets programming, using a change-based programming approach. Defines two multicast application categories. |
| [Multicast Socket Option Behavior](multicast-socket-option-behavior.md)               | Provides an extensive table to explain the implications and requirements of calling multicast socket options in particular order.                                                  |
| [Multicast Programming Sample](multicast-programming-sample.md)                       | Programming snippet that illustrates how to use socket options to enable multicast applications in Windows.                                                                        |
| [Final-State-based Multicast Programming](final-state-based-multicast-programming.md) | Explains final-state approach, and how to use IOCTLs for multicast programming with Windows Sockets.                                                                               |
| [Porting Broadcast Applications to IPv6](porting-broadcast-applications-to-ipv6.md)   | Provides guidelines for porting IPv4 broadcast applications to IPv6 multicast.                                                                                                     |



 

 

 



