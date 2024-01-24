---
title: Windows Event Log Reference
description: The following are the programming elements that you use to create an instrumentation manifest, create resources from the manifest that your provider uses, get instrumentation metadata at run time, and query events from channels and log files
ms.assetid: 7af07a43-62f6-412f-9f67-46ad08922daf
ms.topic: article
ms.date: 05/31/2018
---

# Windows Event Log Reference

The following are the programming elements that you use to create an instrumentation manifest, create resources from the manifest that your provider uses, get instrumentation metadata at run time, and query events from channels and log files:

-   [EventManifest Schema](eventmanifestschema-schema.md)
-   [Event Schema](eventschema-schema.md)
-   [Query Schema](queryschema-schema.md)
-   [Windows Event Log Constants](windows-event-log-constants.md)
-   [Windows Event Log Data Types](windows-event-log-data-types.md)
-   [Windows Event Log Enumerations](windows-event-log-enumerations.md)
-   [Windows Event Log Functions](windows-event-log-functions.md)
-   [Windows Event Log Structures](windows-event-log-structures.md)
-   [Windows Event Log Tools](windows-event-log-tools.md)

For applications written using a .NET language, such as C# or Visual Basic, see the following namespaces:

-   To write events, use the classes and methods defined in the [System.Diagnostics.Eventing](/dotnet/api/system.diagnostics.eventing?view=netframework-4.8&preserve-view=true) namespace.
-   To consume events from a Windows Event Log channel or log, use the classes and methods defined in the [System.Diagnostics.Eventing.Reader](/dotnet/api/system.diagnostics.eventing.reader) namespace.

As an alternative to using the [System.Diagnostics.Eventing](/dotnet/api/system.diagnostics.eventing) namespace to write events, you can use the **-cs** or **-css** argument to have the message compiler generate the code to write the events. For details, see [**Message Compiler**](message-compiler--mc-exe-.md).
