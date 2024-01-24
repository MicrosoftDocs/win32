---
description: Providers are applications that contain event tracing instrumentation.
ms.assetid: b522f16d-8d61-4db3-9194-d965b6d859ec
title: Providing Events
ms.topic: article
ms.date: 05/31/2018
---

# Providing Events

Providers are applications that contain event tracing instrumentation. After a provider registers itself, a controller can then enable or disable event tracing in the provider. The provider defines its interpretation of being enabled or disabled. Generally, an enabled provider generates events, and a disabled provider does not. This lets you add event tracing to your application without requiring that it generate events all the time.

This section shows you how to:

-   [Write events](writing-events.md)
-   [Write related events](writing-related-events-in-an-end-to-end-scenario.md)
-   [Publish your event schema to share with consumers](publishing-your-event-schema.md)

For information about controlling event tracing sessions, see [Controlling Event Tracing Sessions](controlling-event-tracing-sessions.md). For information about consuming events from an event trace provider, see [Consuming Events](consuming-events.md).

 

 



