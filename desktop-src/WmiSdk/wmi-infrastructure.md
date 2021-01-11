---
description: In the WMI infrastructure, the WMI service (Winmgmt) is the operating system component that acts as the mediator between management applications and WMI data providers. The WMI repository is a storage area for WMI-related static data.
ms.assetid: 6ef157be-fb75-4453-bc20-4568a3dc18c0
ms.tgt_platform: multiple
title: WMI Infrastructure
ms.topic: article
ms.date: 05/31/2018
---

# WMI Infrastructure

In the WMI infrastructure, the WMI service (Winmgmt) is the operating system component that acts as the mediator between management applications and WMI data [*providers*](gloss-p.md). The [*WMI repository*](gloss-w.md) is a storage area for WMI-related static data.

The WMI service is implemented as a service process within a shared service host process (SVCHOST). For more information, see [Provider Hosting and Security](provider-hosting-and-security.md).

The WMI service starts when the first management application or script makes a call to connect to a WMI namespace. Depending on the setup, the WMI service may shut down or go into a low memory profile when not being called by a management application.

The WMI service interacts with management applications through the COM interface. When an application makes a request through the interface, WMI determines whether the request is for static or dynamic data. If the request involves static data, such as the name of a managed object, WMI retrieves the data from the repository. If the request involves dynamic data, such as the amount of memory a managed object is currently using, WMI passes the request on to a provider.

Providers register their location with the WMI service, which allows WMI to route data requests. A provider also registers support for particular operations, such as data retrieval, modification, deletion, enumeration, or query processing. The WMI service uses the provider registration information to match application requests with the appropriate provider. WMI also uses the registration information to load and unload providers, as necessary. When a provider finishes processing a request, the provider returns the result back to the WMI service. WMI then forwards the result on to the application through the COM interface. For more information, see [Providing Data to WMI](providing-data-to-wmi.md).

WMI uses [Event Tracing](/windows/desktop/ETW/event-tracing-portal) (ETW) to record WMI service activity.

Because the infrastructure handles all traffic between the providers and the management applications, the infrastructure provides the following features:

-   Event Notification Support

    For more information, see [Monitoring Events](monitoring-events.md).

-   Query Language Support

    For more information, see [Querying with WQL](querying-with-wql.md).

-   Security Support

    For more information, see [Maintaining WMI Security](maintaining-wmi-security.md).

-   Scripting Access to Performance Counter Data

    For more information, see [Monitoring Performance Data](monitoring-performance-data.md).

## Related topics

<dl> <dt>

[WMI Architecture](wmi-architecture.md)
</dt> </dl>

 

 
