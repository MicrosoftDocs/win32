---
description: Microsoft Windows networking components have been developed for performance and scalability.
ms.assetid: 2160b93e-c126-4592-972c-d9cc14eec745
title: High-performance Windows Sockets Applications
ms.topic: article
ms.date: 05/31/2018
---

# High-performance Windows Sockets Applications

Microsoft Windows networking components have been developed for performance and scalability. This enables applications to maximize available network bandwidth. Windows Sockets and the Windows TCP/IP protocol stack have been tuned and streamlined. As a result, properly written Windows applications can achieve exceptional throughput and performance, as the following facts illustrate:

-   Windows is capable of servicing over 200,000 simultaneous TCP connections.
-   In a test conducted by SPECWeb96, Internet Information Server on Windows serviced over 25,000 HTTP requests per second.
-   Windows set a transmission record of over 750Mbps on a transcontinental gigabit network consisting of 10 hops.

These achievements illustrate that Windows TCP/IP processes data very quickly. Many applications, however, do not take advantage of the Windows, TCP/IP, and Windows Sockets performance capabilities because they unknowingly implement performance-hampering techniques.

In this guide, you will learn to identify common programming mistakes and how to avoid them. Then, you will learn techniques that enable Windows Sockets applications to perform optimally. This guide is presented in six sections. The order of the sections is intentional; to get the most out of this guide, read it in order. The following table provides links to each section, as well as a brief description of each topic.



| Topic                                                                                            | Description                                                                                                                                         |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [Network Terminology](network-terminology-2.md)                                                 | Defines networking terminology and metrics necessary to understanding the performance of a network application.                                     |
| [Performance Dimensions](performance-dimensions-2.md)                                           | Discusses performance dimensions that affect the perceived and actual network performance of an application.                                        |
| [TCP/IP Characteristics](tcp-ip-characteristics-2.md)                                           | Defines TCP/IP protocol characteristics that can result in performance issues for a poorly written application.                                     |
| [Application Behavior](application-behavior-2.md)                                               | Explains how to recognize the signs of a poorly performing network application.                                                                     |
| [Improving a Slow Application](improving-a-slow-application-2.md)                               | Provides samples of application design issues that contribute to a poorly performing application, and makes changes to code to improve performance. |
| [Best Practices for Interactive Applications](best-practices-for-interactive-applications-2.md) | Lists the best practices to employ for developing optimal interactive network applications.                                                         |



 

 

 



