---
description: The COM+ instrumentation service enables you to build your own COM+ event management and logging programs when you want to display various performance metrics for your COM+ components.
ms.assetid: 07f68734-a382-4fe5-86af-90805f61c68d
title: COM+ Instrumentation Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Instrumentation Concepts

The COM+ instrumentation service enables you to build your own COM+ event management and logging programs when you want to display various performance metrics for your COM+ components. COM+ instrumentation can also be used to configure user-defined events and to convert COM+ events to Visual Studio Analyzer (VSA) format when you are upgrading MTS packages that are receiving MTS events.

> [!Note]  
> As of Windows Server 2003, only administrators have read access privileges to the trace logs for system events.

 

By subscribing to the events published by the system events publisher, clients can implement the [COM+ instrumentation interfaces](com--instrumentation-interfaces.md) to receive notifications for a variety of COM+ performance metrics, such as information about specific COM+ objects, COM+ applications, and COM+ services. The metrics are published to the client by using the [COM+ events service](com--events.md), a loosely coupled events (LCE) system that stores event information from different publishers in an event store in the COM+ catalog.

> [!Note]  
> COM+ instrumentation does not guarantee the delivery of an event.

 

Every metric has a timestamp that indicates the time when the metric was generated, not the time that it was dispatched or received. The client can correlate the timestamp and find out the cost of running a COM+ application, the cost of a transaction executed inside a COM+ application, or the cost of a method call inside of a COM+ application.

You can also use the COM+ Instrumentation service to filter for the specific performance metrics information that you want to see. For example, when you subscribe to a COM+ instrumentation interface or method, you can specify properties for the subscription in the [**COMSVCSEVENTINFO**](/windows/win32/api/comsvcs/ns-comsvcs-comsvcseventinfo) structure, such as the application ID (**guidApp** member) or the process ID (**dwPid** member).

When the application ID is specified, you receive only the metrics from the specified application. When the process ID is specified, you receive metrics from the specified server application and library applications that are loaded in that process. The user can specify both the application ID and the process ID, but the application ID has to be that of the server application running in the process with the specified process ID. If neither is specified, the user receives metrics from all the server and library applications.

The COM+ instrumentation metrics provide enough information for the monitoring application to correlate them with the operating system metrics for performance analysis, capacity planning, and for modeling and prediction.

## Related topics

<dl> <dt>

[COM+ Instrumentation Interfaces](com--instrumentation-interfaces.md)
</dt> </dl>

 

 



