---
title: Controlling Devices
description: UPnP-based devices are controlled by the services they expose.
ms.assetid: 4edca439-f767-41e6-97bb-ead751930714
ms.topic: article
ms.date: 05/31/2018
---

# Controlling Devices

UPnP-based devices are controlled by the services they expose. A UPnP service is the smallest controllable entity in the UPnP architecture. Devices expose one service for each primary function they perform. Complex devices are typically composed of several simple services and other devices.

A service consists of a set of state variables and a set of actions an application can invoke that operate on those state variables. In the Control Point API with UPnP technology, services are represented by **Service** objects that expose the [**IUPnPService**](/windows/desktop/api/Upnp/nn-upnp-iupnpservice) interface.

A service type defines the state variables and actions supported by a particular service. For example, the service type for a clock service defines **GetTime** and **SetTime** actions, along with a **Time** state variable.

A service ID differentiates multiple common service types within a single device. For example, there can be two clock services in an alarm clock, one for the regular clock and the other for the alarm. There needs to be a way to differentiate between the two services, which have identical service types. The service ID provides a unique way of identifying an instance of a service type. Then, this service ID is used to access the correct service from the [**IUPnPServices**](/windows/desktop/api/Upnp/nn-upnp-iupnpservices) collection, because service type is not a unique identifier. The [**IUPnPService**](/windows/desktop/api/Upnp/nn-upnp-iupnpservice) interface also allows applications to register a callback function with the service object. When the value of a service's state variable changes, the service object invokes the registered callback to notify the application of the change. The UPnP framework also invokes this callback to notify applications when a service instance has become unavailable. The service can become unavailable for a variety of reasons, including transient network failure.

For more information, see the following topics:

-   [Obtaining Service Objects](obtaining-service-objects.md)
-   [Registering a Callback](registering-a-callback.md)
-   [Querying State Variables](querying-state-variables.md)
-   [Invoking Actions](invoking-actions.md)

 

 




