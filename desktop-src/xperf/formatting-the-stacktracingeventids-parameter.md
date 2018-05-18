---
title: Formatting the StackTracingEventIds Parameter
description: Formatting the StackTracingEventIds Parameter
ms.assetid: '8dd0bccd-405e-4f6c-b3c1-75ab7d195171'
---

# Formatting the StackTracingEventIds Parameter

The *StackTracingEventIds* of the [**StartKernelTrace**](startkerneltrace.md) function is an array of [**STACK\_TRACING\_EVENT\_ID**](stack-tracing-event-id.md) entries, where each entry specifies the type of events on which to enable stack walking. Each **STACK\_TRACING\_EVENT\_ID** entry in *StackTracingEventIds* must be formatted in the following way:

-   The **EventGuid** member is set to the GUID for a specific kernel event that has been enabled to generate call stacks.

    For more information on GUID values for the **EventGuid** member, see the [NT Kernel Logger Constants](http://go.microsoft.com/fwlink/p/?linkid=141503) discussion of NT Kernel Logger Constants. Additionally, **EventGuid** GUID values are listed in evntrace.h.

-   The **Type** member is set to the event type for a specific kernel event configured to generate call stacks.

For example, to collect a stack on every new process event, follow these steps:

1.  Set **EventGuid** to the GUID for the [**Process\_V2**](https://msdn.microsoft.com/library/windows/desktop/dd765155) class, {3d6fa8d0-fe05-11d0-9dda-00c04fd7ba7c}.

2.  Set **Type** to EVENT\_TRACE\_TYPE\_START (1).

> [!Note]  
> If *StackTracingEventIds* contains [**STACK\_TRACING\_EVENT\_ID**](stack-tracing-event-id.md) entries that are not enabled in the **EVENT\_TRACE\_PROPERTIES.EnableFlags** member or could not be decoded by Kernel Trace Control, those flags are ignored and no error code is returned. For more information, see [EVENT\_TRACE\_PROPERTIES Structure.](http://go.microsoft.com/fwlink/p/?linkid=141500)

 

 

 




