---
description: WMI supplies a set of troubleshooting classes that scripts and applications can use to get information about WMI internal state during WMI core and provider operations.
ms.assetid: 631e0cce-0e83-42e5-a381-e96b1f70d6f9
ms.tgt_platform: multiple
title: WMI Troubleshooting Classes
ms.topic: article
ms.date: 05/31/2018
---

# WMI Troubleshooting Classes

WMI supplies a set of troubleshooting classes that scripts and applications can use to get information about WMI internal state during WMI core and provider operations. For more information about WMI troubleshooting, see [WMI Troubleshooting](wmi-troubleshooting.md) and [Provider Configuration and Troubleshooting Classes](provider-configuration-and-troubleshooting-classes.md).

WMI has several basic troubleshooting classes for WMI core and provider operations:

-   [**MSFT\_WmiProvider\_Counters**](/previous-versions/windows/desktop/wmisystemprov/msft-wmiprovider-counters)

    Only one of these classes is found on each computer system. It provides counts of various kind of provider operations on that system.

-   [**MSFT\_WmiSelfEvent**](/previous-versions/windows/desktop/wmisystemprov/msft-wmiselfevent)

    The event troubleshooting classes derive from [**MSFT\_WmiSelfEvent**](/previous-versions/windows/desktop/wmisystemprov/msft-wmiselfevent). Queries of this class return instances of event classes such as [**MSFT\_WmiThreadPoolCreated**](/previous-versions/windows/desktop/wmisystemprov/msft-wmithreadpoolcreated) or [**MSFT\_WmiProvider\_CreateInstanceEnumAsyncEvent\_Post**](/previous-versions/windows/desktop/wmisystemprov/msft-wmiprovider-createinstanceenumasyncevent-post).

    The following list provides links to different categories of event classes derived from [**MSFT\_WmiSelfEvent**](/previous-versions/windows/desktop/wmisystemprov/msft-wmiselfevent):

    -   [Provider Event Troubleshooting Classes](provider-event-troubleshooting-classes.md)
    -   [ConsumerProvider Troubleshooting Classes](consumerprovider-troubleshooting-classes.md)
    -   [WMI Service Event Troubleshooting Classes](wmi-service-event-troubleshooting-classes.md)

## Related topics

<dl> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> <dt>

[Receiving a WMI Event](receiving-a-wmi-event.md)
</dt> </dl>

 

 
