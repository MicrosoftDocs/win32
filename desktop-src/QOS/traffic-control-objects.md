---
title: Traffic Control Objects
description: Applications that require specific or granular traffic control, beyond what is available in the TC API, can use traffic control objects. The use of traffic control objects with the TC API is similar to the use of QOS Objects with the QOS API.
ms.assetid: 0a68a6b0-591b-42d3-bdf4-292cd581b1d1
keywords:
- Quality of Service QOS , reference, traffic control objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Traffic Control Objects

Applications that require specific or granular traffic control, beyond what is available in the TC API, can use traffic control objects. The use of traffic control objects with the TC API is similar to the use of QOS Objects with the QOS API.

Like QOS objects, traffic control object follow a stringent structure. Traffic control objects always include an information header that specifies the type and length of the traffic control object to which it is attached, followed by the object itself.

Some objects are shared by QOS and traffic control. Those objects are defined in the [QOS Objects](qos-objects.md) section, and are the following:

-   [**QOS\_SD\_MODE**](/windows/previous-versions/Qos/ns-qos-_qos_sd_mode?branch=master)
-   [**QOS\_SHAPING\_RATE**](/windows/previous-versions/Qos/ns-qos-_qos_shaping_rate?branch=master)

This section describes the following traffic control objects:

-   [**QOS\_TRAFFIC\_CLASS**](/windows/previous-versions/QosObjs/ns-qosobjs-_qos_traffic_class?branch=master)
-   [**QOS\_DS\_CLASS**](/windows/previous-versions/QosObjs/ns-qosobjs-_qos_ds_class?branch=master)
-   [**QOS\_DIFFSERV**](/windows/previous-versions/QosObjs/ns-qosobjs-_qos_diffserv?branch=master)
-   [**QOS\_FRIENDLY\_NAME**](/windows/previous-versions/QosObjs/ns-qosobjs-_qos_friendly_name?branch=master)

As with QOS objects, traffic control objects begin each object with the [**QOS\_OBJECT\_HDR**](/windows/previous-versions/Qos/ns-qos-qos_object_hdr?branch=master), which is used by QOS components that interrogate QOS objects to ascertain the type of object that follows the header.

 

 




