---
title: Traffic Control Objects
description: Applications that require specific or granular traffic control, beyond what is available in the TC API, can use traffic control objects. The use of traffic control objects with the TC API is similar to the use of QOS Objects with the QOS API.
ms.assetid: 0a68a6b0-591b-42d3-bdf4-292cd581b1d1
keywords:
- Quality of Service QOS , reference, traffic control objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Traffic Control Objects

Applications that require specific or granular traffic control, beyond what is available in the TC API, can use traffic control objects. The use of traffic control objects with the TC API is similar to the use of QOS Objects with the QOS API.

Like QOS objects, traffic control object follow a stringent structure. Traffic control objects always include an information header that specifies the type and length of the traffic control object to which it is attached, followed by the object itself.

Some objects are shared by QOS and traffic control. Those objects are defined in the [QOS Objects](qos-objects.md) section, and are the following:

-   [**QOS\_SD\_MODE**](/previous-versions/windows/desktop/api/Qos/ns-qos-_qos_sd_mode)
-   [**QOS\_SHAPING\_RATE**](/previous-versions/windows/desktop/api/Qos/ns-qos-_qos_shaping_rate)

This section describes the following traffic control objects:

-   [**QOS\_TRAFFIC\_CLASS**](/previous-versions/windows/desktop/api/QosObjs/ns-qosobjs-_qos_traffic_class)
-   [**QOS\_DS\_CLASS**](/previous-versions/windows/desktop/api/QosObjs/ns-qosobjs-_qos_ds_class)
-   [**QOS\_DIFFSERV**](/previous-versions/windows/desktop/api/QosObjs/ns-qosobjs-_qos_diffserv)
-   [**QOS\_FRIENDLY\_NAME**](/previous-versions/windows/desktop/api/QosObjs/ns-qosobjs-_qos_friendly_name)

As with QOS objects, traffic control objects begin each object with the [**QOS\_OBJECT\_HDR**](/previous-versions/windows/desktop/api/Qos/ns-qos-qos_object_hdr), which is used by QOS components that interrogate QOS objects to ascertain the type of object that follows the header.

 

 




