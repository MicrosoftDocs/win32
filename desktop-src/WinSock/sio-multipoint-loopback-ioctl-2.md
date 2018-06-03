---
Description: Using SIO\_MULTIPOINT\_LOOPBACK command code to enable or disable loopback of multipoint traffic.
ms.assetid: 7e11932b-ce9a-4500-888f-8a08ab67b46c
title: SIO\_MULTIPOINT\_LOOPBACK Ioctl
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SIO\_MULTIPOINT\_LOOPBACK Ioctl

When d\_leaf sockets are used in a nonrooted data plane, it is generally desirable to be able to control whether traffic sent out is also received back on the same socket. The SIO\_MULTIPOINT\_LOOPBACK command code for [**WSPIoctl**](/windows/desktop/api/Ws2spi/) is used to enable or disable loopback of multipoint traffic.

 

 



