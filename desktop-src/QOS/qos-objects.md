---
title: QOS Objects
description: Applications that require specific or granular quality of service control, beyond that available in the QOS API, can use QOS objects.
ms.assetid: 4b152016-f2b6-46d6-99b4-d50c66757c0a
keywords:
- Quality of Service QOS , reference, objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# QOS Objects

Applications that require specific or granular quality of service control, beyond that available in the QOS API, can use QOS objects. QOS objects implement functionality specific to the Microsoft Windows, such as traffic control-related objects, as well as industry-wide functionality such as RSVP-related objects. QOS objects are implemented through the ProviderSpecific buffer in the [**FLOWSPEC**](/windows/previous-versions/Qos/ns-qos-_flowspec?branch=master) structure, which is a member of the [**QOS**](/windows/win32/Winsock2/ns-winsock2-_qualityofservice?branch=master) structure.

QOS objects follow a stringent structure. They always include an information header that specifies the type and length of the QOS object to which it is attached, followed by the object itself.

The end of a list of QOS objects in a WSABUF buffer is indicated by a QOS\_OBJECT\_END\_OF\_LIST object, as defined in the Qos.h header file.

This section describes the following:

-   [The ProviderSpecific Buffer](the-providerspecific-buffer.md)
-   [**QOS\_OBJECT\_HDR**](/windows/previous-versions/Qos/ns-qos-qos_object_hdr?branch=master)
-   [**QOS\_DESTADDR**](/windows/previous-versions/Qossp/ns-qossp-_qos_destaddr?branch=master)
-   [**QOS\_SD\_MODE**](/windows/previous-versions/Qos/ns-qos-_qos_sd_mode?branch=master)
-   [**QOS\_SHAPING\_RATE**](/windows/previous-versions/Qos/ns-qos-_qos_shaping_rate?branch=master)
-   [**QOS\_TCP\_TRAFFIC**](/windows/previous-versions/QosObjs/ns-qosobjs-_qos_tcp_traffic?branch=master)
-   [**RSVP\_ADSPEC**](/windows/previous-versions/Qossp/ns-qossp-_rsvp_adspec?branch=master)
-   [**RSVP\_RESERVE\_INFO**](/windows/previous-versions/Qossp/ns-qossp-_rsvp_reserve_info?branch=master)
-   [**RSVP\_STATUS\_INFO**](/windows/previous-versions/Qossp/ns-qossp-_rsvp_status_info?branch=master)

 

 




