---
description: ETW provides a way to group related events from more than one component.
ms.assetid: 2a85e4af-a1fe-4c28-8ce2-14d15deaa820
title: Writing Related Events in an End-to-End Scenario
ms.topic: article
ms.date: 05/31/2018
---

# Writing Related Events in an End-to-End Scenario

ETW provides a way to group related events from more than one component. For example, if several components (either on the same computer or on different computers) are involved in processing the same data, and each component logs events for their portion of the activity, you can group all of the related events together. This will allow a consumer to consume all of the events, from the beginning of the process to the end of the process.

To write related events in a [manifest-based](about-event-tracing.md) provider, see [Writing Related Events in a Manifest-based Provider](writing-related-events-in-a-manifest-base-provider.md).

To write related events in a [classic](about-event-tracing.md) provider, see [Writing Related Events in a Classic Provider](tracing-event-instances.md).

 

 



