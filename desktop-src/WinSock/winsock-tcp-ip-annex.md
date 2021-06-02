---
description: This section describes Transmission Control Protocol/Internet Protocol (TCP/IP) functions, data structures, and controls.
ms.assetid: ff92750b-453e-4328-821c-1098de8e6125
title: Winsock TCP/IP Annex
ms.topic: article
ms.date: 05/31/2018
---

# Winsock TCP/IP Annex

This section describes Transmission Control Protocol/Internet Protocol (TCP/IP) functions, data structures, and controls.



| Element          | Description                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Protocol name(s) | TCP, UDP                                                                                                                                    |
| Description      | Provides transport services over the IP networking layer: UDP for unreliable datagrams, TCP for reliable, connection-oriented byte streams. |
| Address family   | **AF\_INET**, **AF\_INET6**                                                                                                                 |
| Header file      | *Ws2tcpip.h*                                                                                                                                |



 

Two basic types of transport services are offered: unreliable datagrams (UDP), and reliable connection oriented–byte streams (TCP). In addition, a raw socket is optionally supported. Raw sockets allow an application to communicate through protocols other than TCP and UDP such as ICMP. Raw sockets are supported on the **AF\_INET** and **AF\_INET6** address families with some limitations.

This section covers extensions to Winsock that are specific to TCP/IP protocols. It also describes aspects of base Winsock functions that require special consideration or that may exhibit unique behavior when using TCP/IP.

 

 



