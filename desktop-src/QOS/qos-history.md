---
title: QOS History
description: QOS mechanisms in Windows operating systems have evolved to meet network performance needs arising from the trend toward bandwidth-intensive applications.
ms.assetid: c176819e-a095-4306-9431-b9b3e9ca11f0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QOS History

QOS mechanisms in Windows operating systems have evolved to meet network performance needs arising from the trend toward bandwidth-intensive applications.

Windows 2000 introduced the Generic QOS (GQOS) application programming interface (API) as a framework for QOS. The GQOS API provided access to QOS mechanisms that were available as part of the networking stack, including the Resource Reservation Protocol (RSVP) for signaling and reserving resources on the network; traffic shaping and filtering mechanisms; and Layer 2 and Layer 3 priority-marking mechanisms. Windows 2000 also provided tools, such as Subnet Bandwidth Manager (SBM) and QOS policy control.

In Windows XP, the focus was on prioritization and traffic shaping mechanisms. Although GQOS continued to be the application interface for accessing prioritized QOS, the reservation mechanisms had been removed. The kernel component that implemented prioritization and traffic shaping was the QOS Packet Scheduler, accessible through the GQOS API and through a lower-level application interface called the Traffic Control (TC) API. The TC API provided control of QOS mechanisms (such as prioritization and shaping) at the host level rather than at the application level, but it required administrative privileges to be invoked. The QOS mechanisms provided in Windows XP supported enterprise QOS needs for wired networks. In Windows XP Service Pack 2 (SP2), the GQOS mechanisms allowed the application to set Layer 3 priorities only. Applications that set Layer 2 priorities for their traffic had to implement an independent service with administrative privileges to set Layer 2 priorities using TC APIs.

In Windows Vista, two features were introduced: Quality Windows Audio Video Experience (qWAVE) and policy-based QOS. qWAVE is designed to estimate the network bandwidth, intelligently mark the application packets (with proper DSCP values), and interact with the application in the event of network congestion or bandwidth fluctuations (informing the application to take appropriate actions). Policy-based QOS allows IT administrators to apply QOS to applications (which do not need to have native support for QOS), computers, and users in their enterprise network.

In Windows 7, enhancements were made to allow policies to be created based on the URL of an HTTP server (rather than just on an application name), source and/or destination IP addresses, source and/or destination ports, and protocol). Support for changing outgoing DSCP values through the [**QOS\_SET\_FLOW**](/previous-versions/windows/desktop/api/Qos2/ne-qos2-_qos_set_flow) enumeration was also added.

 

 




