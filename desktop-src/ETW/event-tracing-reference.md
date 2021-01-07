---
description: Lists the elements used with event tracing.
ms.assetid: 8cb5907e-9006-45d1-9d48-13a43a631664
title: Event Tracing Reference
ms.topic: article
ms.date: 01/30/2020
---

# Event Tracing Reference

You use the following programming elements to write applications that incorporate event tracing:

-   [Event Tracing Enumerations](/windows/desktop/api/_etw/#enumerations)
-   [Event Tracing Functions](/windows/desktop/api/_etw/#functions)
-   [Event Tracing Interfaces](/windows/desktop/api/_etw/#interfaces)
-   [Event Tracing Structures](/windows/desktop/api/_etw/#structures)
-   [Event Tracing Constants](event-tracing-constants.md)

For details on samples that use these programming elements, see [Event Tracing Samples](event-tracing-samples.md).

This section also contains information on:

-   [Tools](event-tracing-tools.md) that ETW provides
-   [MOF class definitions](event-tracing-mof-classes.md) for kernel events
-   [MOF class qualifiers](event-tracing-mof-qualifiers.md) used when defining your event classes

## Process ETW traces in .NET code

You can also use the [.NET TraceProcessing API](https://www.nuget.org/packages/Microsoft.Windows.EventTracing.Processing.All) to analyze ETW traces for your applications and other software components. This API is used internally at Microsoft to analyze ETW data produced the Windows engineering system, and it is also used to power several tables in [Windows Performance Analyzer](/windows-hardware/test/wpt/windows-performance-analyzer). This API is available as a NuGet package.

For more information, see [this article](/windows/apps/trace-processing/overview).
