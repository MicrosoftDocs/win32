---
title: Traffic Control Objects
description: Applications that require specific or granular traffic control, beyond what is available in the TC API, can use traffic control objects. The use of traffic control objects with the TC API is similar to the use of QOS Objects with the QOS API.
ms.assetid: '0a68a6b0-591b-42d3-bdf4-292cd581b1d1'
keywords: ["Quality of Service QOS , reference, traffic control objects"]
---

# Traffic Control Objects

Applications that require specific or granular traffic control, beyond what is available in the TC API, can use traffic control objects. The use of traffic control objects with the TC API is similar to the use of QOS Objects with the QOS API.

Like QOS objects, traffic control object follow a stringent structure. Traffic control objects always include an information header that specifies the type and length of the traffic control object to which it is attached, followed by the object itself.

Some objects are shared by QOS and traffic control. Those objects are defined in the [QOS Objects](qos-objects.md) section, and are the following:

-   [**QOS\_SD\_MODE**](qos-sd-mode.md)
-   [**QOS\_SHAPING\_RATE**](qos-shaping-rate.md)

This section describes the following traffic control objects:

-   [**QOS\_TRAFFIC\_CLASS**](qos-traffic-class.md)
-   [**QOS\_DS\_CLASS**](qos-ds-class.md)
-   [**QOS\_DIFFSERV**](qos-diffserv.md)
-   [**QOS\_FRIENDLY\_NAME**](qos-friendly-name.md)

As with QOS objects, traffic control objects begin each object with the [**QOS\_OBJECT\_HDR**](qos-object-hdr.md), which is used by QOS components that interrogate QOS objects to ascertain the type of object that follows the header.

 

 




