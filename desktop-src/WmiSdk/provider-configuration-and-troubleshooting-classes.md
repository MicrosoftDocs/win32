---
description: The MSFT\_Providers class and the WMI troubleshooting classes are a group of the MSFT event classes coupled to WMI provider events.
ms.assetid: 5eaf7026-87bf-416b-9a6d-7f92f85b0882
ms.tgt_platform: multiple
title: Provider Configuration and Troubleshooting Classes
ms.topic: article
ms.date: 05/31/2018
---

# Provider Configuration and Troubleshooting Classes

The [**MSFT\_Providers**](/previous-versions/windows/desktop/wmisystemprov/msft-providers) class and the WMI troubleshooting classes are a group of the [MSFT event classes](msft-classes.md) coupled to WMI provider events.

The [**MSFT\_Providers**](/previous-versions/windows/desktop/wmisystemprov/msft-providers) class contains configuration information for providers and includes the following methods that allow you to load and unload providers, or suspend and resume provider operations:

-   [**Load Method of the MSFT\_Providers Class**](/previous-versions/windows/desktop/wmisystemprov/load-method-in-class-msft-providers)
-   [**UnLoad Method of the MSFT\_Providers Class**](/previous-versions/windows/desktop/wmisystemprov/unload-method-in-class-msft-providers)
-   [**Resume Method of the MSFT\_Providers Class**](/previous-versions/windows/desktop/wmisystemprov/resume-method-in-class-msft-providers)
-   [**Suspend Method of the MSFT\_Providers Class**](/previous-versions/windows/desktop/wmisystemprov/suspend-method-in-class-msft-providers)

The [WMI troubleshooting classes](wmi-troubleshooting-classes.md) are named to indicate whether the event is fired before or after a provider event. For example, the [**MSFT\_WmiProvider\_AccessCheck\_Pre**](/previous-versions/windows/desktop/wmisystemprov/msft-wmiprovider-accesscheck-pre) object is generated immediately before calling the provider's implementation of **IWbemEventSecurity::AccessCheck**, while the [**MSFT\_WmiProvider\_AccessCheck\_Post**](/previous-versions/windows/desktop/wmisystemprov/msft-wmiprovider-accesscheck-post) object is called immediately after.

## Related topics

<dl> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> <dt>

[WMI Troubleshooting Classes](wmi-troubleshooting-classes.md)
</dt> </dl>

 

 
