---
description: Using SIO\_MULTICAST\_SCOPE command code to specify the scope over which the multicast should occur.
ms.assetid: 3acec987-9cb4-446c-af6e-ea0e6a96e70c
title: SIO_MULTICAST_SCOPE Ioctl
ms.topic: article
ms.date: 05/31/2018
---

# SIO\_MULTICAST\_SCOPE Ioctl

When multicasting is employed, it is usually necessary to specify the scope over which the multicast should occur. Here scope is defined to be the number of routed network segments to be covered. The SIO\_MULTICAST\_SCOPE command code for [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)) is used to control this. A scope of zero would indicate that the multicast transmission would not be placed on the wire but could be disseminated across sockets within the local host. A scope value of one (the default) indicates that the transmission will be placed on the wire, but will not cross any routers. Higher scope values determine the number of routers that may be crossed. Note that this corresponds to the time-to-live (TTL) parameter in IP multicasting.

 

 
