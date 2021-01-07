---
description: Classic providers use the TraceEventInstance function to trace events that are part of a single transaction. You can also use this function to trace parent/child events.
ms.assetid: 246e9443-3120-49bf-a6e3-64dddba348fa
title: Writing Related Events in a Classic Provider
ms.topic: article
ms.date: 05/31/2018
---

# Writing Related Events in a Classic Provider

[Classic](about-event-tracing.md) providers use the [**TraceEventInstance**](/windows/win32/api/evntrace/nf-evntrace-traceeventinstance) function to trace events that are part of a single transaction. You can also use this function to trace parent/child events.

Before calling the [**TraceEventInstance**](/windows/win32/api/evntrace/nf-evntrace-traceeventinstance) function, you must first call the [**CreateTraceInstanceId**](/windows/win32/api/evntrace/nf-evntrace-createtraceinstanceid) function to obtain a transaction identifier. This function generates a unique transaction identifier, and maps it to a registered class GUID handle. The handles for registered class GUIDs are available in the **RegHandle** members of [**TRACE\_GUID\_REGISTRATION**](/windows/win32/api/evntrace/ns-evntrace-trace_guid_registration) structures, after calling the [**RegisterTraceGuids**](/windows/win32/api/evntrace/nf-evntrace-registertraceguidsa) function. The transaction identifier is placed in the **InstanceId** member of an [**EVENT\_INSTANCE\_INFO**](/windows/win32/api/evntrace/ns-evntrace-event_instance_info) structure that you pass to the **CreateTraceInstanceId** function.

The [**EVENT\_INSTANCE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_instance_header) structure that is passed to the [**TraceEventInstance**](/windows/win32/api/evntrace/nf-evntrace-traceeventinstance) function is similar to the [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) structure (see [Tracing Events](tracing-events.md)), except that it contains additional information relating to instances, and does not contain a **Guid** member.

Event instances can be used to establish a hierarchical relationship between events. The [**TraceEventInstance**](/windows/win32/api/evntrace/nf-evntrace-traceeventinstance) function accepts instance-specific information from two event instances. The *pInstInfo* parameter points to the [**EVENT\_INSTANCE\_INFO**](/windows/win32/api/evntrace/ns-evntrace-event_instance_info) structure of the event instance, and the *pParentInstInfo* parameter points to the **EVENT\_INSTANCE\_INFO** structure of a parent event instance. The definition of a "parent" event instance is application-defined; the parent can be any instance that has already been generated.

 

 
