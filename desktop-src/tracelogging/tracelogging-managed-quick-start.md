---
title: TraceLogging Managed Quick Start
description:
  The following section describes the basic steps required to add TraceLogging
  to managed code.
ms.assetid: E144214D-8DCC-4263-8232-9F468C1A3CC0
ms.topic: article
ms.date: 06/06/2022
topic_type:
  - kbSyntax
api_name:
api_type:
api_location:
---

# TraceLogging Managed Quick Start

The following section describes the basic steps required to add TraceLogging to
.NET code.

## Prerequisites

- .NET 4.6 or later.

### SimpleTraceLoggingExample.cs

This example demonstrates how to log TraceLogging events without the need to
manually create a separate instrumentation manifest XML file.

```CSharp
using System;
using System.Diagnostics.Tracing;

namespace SimpleTraceLoggingExample
{
    class Program
    {
        private static EventSource log = new EventSource("SimpleTraceLoggingProvider");
        static void Main(string[] args)
        {
            log.Write("Event 1"); // write an event with no fields
            log.Write("Event 2", new { someEventData = DateTime.Now }); // Sending an anonymous type as event data

            ExampleStructuredData EventData = new ExampleStructuredData() { TransactionID = 1234, TransactionDate = DateTime.Now };
            log.Write("Event 3", EventData); // Sending a class decorated with [EventData] as event data
        }
    }

    [EventData] // [EventData] makes it possible to pass an instance of the class as an argument to EventSource.Write()
    public sealed class ExampleStructuredData
    {
        public int TransactionID { get; set; }
        public DateTime TransactionDate { get; set; }
    }
}
```

### Create the EventSource

Before you can log events you must create an instance of the EventSource class.
The first constructor parameter identifies the name of this provider. The
provider is automatically registered for you as illustrated in the example.

```CSharp
private static EventSource log = new EventSource("SimpleTraceLoggingProvider");
```

The instance is static because there should only be one instance of a specific
provider in your application at a time.

### Log TraceLogging events

After the provider is created, the following code from the example above logs a
simple event.

```CSharp
log.Write("Event 1"); // write an event with no fields
```

### Log structured event payload data

You can define structured payload data that is logged with the event. Provide
structured payload data either as an anonymous type or as an instance of a class
that has been annotated with the `[EventData]` attribute as shown in the
following example.

```CSharp
log.Write("Event 2", new { someEventData = DateTime.Now }); // Sending an anonymous type as event data

ExampleStructuredData EventData = new ExampleStructuredData() { TransactionID = 1234, TransactionDate = DateTime.Now };
log.Write("Event 3", EventData); // Sending a class decorated with [EventData] as event data
```

You must add the `[EventData]` attribute to event payload classes that you
define as shown below.

```CSharp
[EventData] // [EventData] makes it possible to pass an instance of the class as an argument to EventSource.Write()
public sealed class ExampleStructuredData
{
    public int TransactionID { get; set; }
    public DateTime TransactionDate { get; set; }
}
```

The attribute replaces the need to manually create a manifest file to describe
the event data. Now all you have to do is pass an instance of the class to the
EventSource.Write() method to log the event and corresponding payload data.

## Summary and next steps

See
[Record and Display TraceLogging Events](tracelogging-record-and-display-tracelogging-events.md)
for information about how to capture and view TraceLogging data using the latest
internal versions of the Windows Performance Tools (WPT).

See [.NET TraceLogging Examples](tracelogging-net-examples.md) for more managed
TraceLogging examples.
