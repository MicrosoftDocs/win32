---
title: Traffic Control and Differentiated Services
description: QOS is capable of providing differentiated services.
ms.assetid: d5c63d5e-b509-457a-a655-3bb36e288ef6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Traffic Control and Differentiated Services

QOS is capable of providing differentiated services. The traffic control functionality built into QOS on Microsoft Windows is also capable of operating in differentiated services mode. This capability is primarily used on routers, in which incoming IP packets are classified into generalized (differentiated) flows using the Diffserv code point (DSCP), rather than setting up and monitoring individual RSVP flows.

The packet scheduler component of TC can be put into differentiated services mode for a given interface by:

-   Using [**TcSetInterface**](/windows/previous-versions/Traffic/nf-traffic-tcsetinterface?branch=master). Set GUID\_QOS\_FLOW\_MODE to ADAPTER\_FLOW\_MODE\_DIFFSERV

The interface can be returned to its default mode of operation by setting the GUID to the default value of ADAPTER\_FLOW\_MODE\_STANDARD.

While operating in Diffserv mode, standard TC function calls, such as those found in the Traffic Control API (TC API) section are still used, but a special QOS object called [**QOS\_DIFFSERV**](/windows/previous-versions/QosObjs/ns-qosobjs-_qos_diffserv?branch=master) can be included with the [**TcAddFlow**](/windows/previous-versions/Traffic/nf-traffic-tcaddflow?branch=master) function call. This QOS object is used to specify the list of DSCPs that are used to classify incoming IP packets on a given flow. Hence the [**TcAddfilter**](/windows/previous-versions/Traffic/nf-traffic-tcaddfilter?branch=master) function and [**TcDeleteFilter**](/windows/previous-versions/Traffic/nf-traffic-tcdeletefilter?branch=master) function will not be used for classifying packets.

For more information about [**QOS\_DIFFSERV**](/windows/previous-versions/QosObjs/ns-qosobjs-_qos_diffserv?branch=master), see [QOS Objects](qos-objects.md).

 

 




