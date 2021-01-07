---
description: Use the following functions to ensure that an application receives notification of certain network events.
ms.assetid: e1ca5abf-83c2-44f0-8049-ddf1b81ef088
title: Receiving Notification of Network Events
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Notification of Network Events

Use the following functions to ensure that an application receives notification of certain network events.

Use the [**NotifyAddrChange**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-notifyaddrchange) function to request notification of any change that occurs in the mapping between IP addresses and interfaces on the local computer.

Similarly, the [**NotifyRouteChange**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-notifyroutechange) function enables an application to request notification of any change that occurs in the IP routing table.

The notifications provided by these functions do not specify what changed; they simply specify that something changed. Use other IP Helper functions, such as [**GetIPAddrTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipaddrtable) and [**GetBestRoute**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getbestroute), to determine the exact nature of the change.

 

 



