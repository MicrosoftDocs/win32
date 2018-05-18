---
title: Traffic Control and Differentiated Services
description: QOS is capable of providing differentiated services.
ms.assetid: 'd5c63d5e-b509-457a-a655-3bb36e288ef6'
---

# Traffic Control and Differentiated Services

QOS is capable of providing differentiated services. The traffic control functionality built into QOS on Microsoft Windows is also capable of operating in differentiated services mode. This capability is primarily used on routers, in which incoming IP packets are classified into generalized (differentiated) flows using the Diffserv code point (DSCP), rather than setting up and monitoring individual RSVP flows.

The packet scheduler component of TC can be put into differentiated services mode for a given interface by:

-   Using [**TcSetInterface**](tcsetinterface.md). Set GUID\_QOS\_FLOW\_MODE to ADAPTER\_FLOW\_MODE\_DIFFSERV

The interface can be returned to its default mode of operation by setting the GUID to the default value of ADAPTER\_FLOW\_MODE\_STANDARD.

While operating in Diffserv mode, standard TC function calls, such as those found in the Traffic Control API (TC API) section are still used, but a special QOS object called [**QOS\_DIFFSERV**](qos-diffserv.md) can be included with the [**TcAddFlow**](tcaddflow.md) function call. This QOS object is used to specify the list of DSCPs that are used to classify incoming IP packets on a given flow. Hence the [**TcAddfilter**](tcaddfilter.md) function and [**TcDeleteFilter**](tcdeletefilter.md) function will not be used for classifying packets.

For more information about [**QOS\_DIFFSERV**](qos-diffserv.md), see [QOS Objects](qos-objects.md).

 

 




