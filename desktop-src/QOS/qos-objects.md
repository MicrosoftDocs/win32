---
title: QOS Objects
description: Applications that require specific or granular quality of service control, beyond that available in the QOS API, can use QOS objects.
ms.assetid: '4b152016-f2b6-46d6-99b4-d50c66757c0a'
keywords: ["Quality of Service QOS , reference, objects"]
---

# QOS Objects

Applications that require specific or granular quality of service control, beyond that available in the QOS API, can use QOS objects. QOS objects implement functionality specific to the Microsoft Windows, such as traffic control-related objects, as well as industry-wide functionality such as RSVP-related objects. QOS objects are implemented through the ProviderSpecific buffer in the [**FLOWSPEC**](flowspec.md) structure, which is a member of the [**QOS**](qos.md) structure.

QOS objects follow a stringent structure. They always include an information header that specifies the type and length of the QOS object to which it is attached, followed by the object itself.

The end of a list of QOS objects in a WSABUF buffer is indicated by a QOS\_OBJECT\_END\_OF\_LIST object, as defined in the Qos.h header file.

This section describes the following:

-   [The ProviderSpecific Buffer](the-providerspecific-buffer.md)
-   [**QOS\_OBJECT\_HDR**](qos-object-hdr.md)
-   [**QOS\_DESTADDR**](qos-destaddr.md)
-   [**QOS\_SD\_MODE**](qos-sd-mode.md)
-   [**QOS\_SHAPING\_RATE**](qos-shaping-rate.md)
-   [**QOS\_TCP\_TRAFFIC**](qos-tcp-traffic.md)
-   [**RSVP\_ADSPEC**](rsvp-adspec.md)
-   [**RSVP\_RESERVE\_INFO**](rsvp-reserve-info.md)
-   [**RSVP\_STATUS\_INFO**](rsvp-status-info.md)

 

 




