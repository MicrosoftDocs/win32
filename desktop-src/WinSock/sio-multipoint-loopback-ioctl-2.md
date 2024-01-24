---
description: Using SIO\_MULTIPOINT\_LOOPBACK command code to enable or disable loopback of multipoint traffic.
ms.assetid: 7e11932b-ce9a-4500-888f-8a08ab67b46c
title: SIO_MULTIPOINT_LOOPBACK Ioctl
ms.topic: article
ms.date: 05/31/2018
---

# SIO\_MULTIPOINT\_LOOPBACK Ioctl

When d\_leaf sockets are used in a nonrooted data plane, it is generally desirable to be able to control whether traffic sent out is also received back on the same socket. The SIO\_MULTIPOINT\_LOOPBACK command code for [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)) is used to enable or disable loopback of multipoint traffic.

 

 
