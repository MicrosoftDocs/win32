---
title: QOS Objects
description: Applications that require specific or granular quality of service control, beyond that available in the QOS API, can use QOS objects.
ms.assetid: 4b152016-f2b6-46d6-99b4-d50c66757c0a
keywords:
- Quality of Service QOS , reference, objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QOS Objects

Applications that require specific or granular quality of service control, beyond that available in the QOS API, can use QOS objects. QOS objects implement functionality specific to the Microsoft Windows, such as traffic control-related objects, as well as industry-wide functionality such as RSVP-related objects. QOS objects are implemented through the ProviderSpecific buffer in the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure, which is a member of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure.

QOS objects follow a stringent structure. They always include an information header that specifies the type and length of the QOS object to which it is attached, followed by the object itself.

The end of a list of QOS objects in a WSABUF buffer is indicated by a QOS\_OBJECT\_END\_OF\_LIST object, as defined in the Qos.h header file.

This section describes the following:

-   [The ProviderSpecific Buffer](the-providerspecific-buffer.md)
-   [**QOS\_OBJECT\_HDR**](/previous-versions/windows/desktop/api/Qos/ns-qos-qos_object_hdr)
-   [**QOS\_DESTADDR**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_qos_destaddr)
-   [**QOS\_SD\_MODE**](/previous-versions/windows/desktop/api/Qos/ns-qos-_qos_sd_mode)
-   [**QOS\_SHAPING\_RATE**](/previous-versions/windows/desktop/api/Qos/ns-qos-_qos_shaping_rate)
-   [**QOS\_TCP\_TRAFFIC**](/previous-versions/windows/desktop/api/QosObjs/ns-qosobjs-_qos_tcp_traffic)
-   [**RSVP\_ADSPEC**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_adspec)
-   [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info)
-   [**RSVP\_STATUS\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_status_info)

 

 




