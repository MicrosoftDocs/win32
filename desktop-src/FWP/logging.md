---
title: Logging (Windows Filtering Platform)
description: Windows Filtering Platform (WFP) provides logging of packet drops and IKE/AuthIP failures.
ms.assetid: '607b7664-6be4-4ae6-991b-58ac9175405a'
ms.topic: article
ms.date: 05/31/2018
---

# Logging (Windows Filtering Platform)

The Windows Filtering Platform (WFP) provides logging of packet drops and IKE/AuthIP failures.

The logged events are defined in the [**FWPM\_NET\_EVENT\_TYPE**](/windows/desktop/api/Fwpmtypes/ne-fwpmtypes-fwpm_net_event_type) enumerated type and are as follows.

-   IKE/AuthIP main mode failures.
-   IKE/AuthIP quick mode failures.
-   AuthIP extended mode failures.
-   Packets dropped during classification.
-   Packets dropped by IPsec.

By default, logging for WFP is enabled for unicast inbound packets and for all outbound packets (unicast, multicast, and broadcast). Logging can be enabled for the rest of the packets, or disabled for all packets, through the [**FwpmEngineSetOptions0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginesetoption0) management function. Event settings persist across reboots.

Logged events are stored in a circular log, that is new events override old ones when the log reaches its maximum size, and can be analyzed using the [event management](fwp-mgmt-functions.md) functions provided by WFP. The event log has a maximum size of 128 KB and it can hold about 100 to 150 events.

Enumeration functions in general, and [**FwpmNetEventEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum0)/[**FwpmNetEventEnum1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventenum1) in particular, take a snapshot of the log at the time the enumeration handle is created. Subsequent calls using the same enumeration handle return the next set of items following those in the last output buffer.

When an application disables WFP logging (by calling [**FwpmEngineSetOptions0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginesetoption0)) all applications are affected. The event log is not cleaned up until an application re-enables WFP logging, but the event log cannot be queried before then.

The WFP event log is emptied after a reboot.

 

 




