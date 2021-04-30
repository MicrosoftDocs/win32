---
description: The SystemTraceProvider is a kernel provider with a predefined sets of kernel events supported on Windows 7, Windows Server 2008 R2, and later.
ms.assetid: 6808EC45-C8C3-45D7-9E4C-337F6A4CF9C8
title: Configuring and Starting a SystemTraceProvider Session
ms.topic: article
ms.date: 05/31/2018
---

# Configuring and Starting a SystemTraceProvider Session

The SystemTraceProvider is a kernel provider with a predefined sets of kernel events supported on Windows 7, Windows Server 2008 R2, and later. On Windows 7 and Windows Server 2008 R2, the SystemTraceProvider could only be used for the NT Kernel Logger session.

On Windows 8, Windows Server 2012, and later, the SystemTraceProvider can be multiplexed for up to 8 logger sessions. The first two slots for logger sessions are reserved for the NT Kernel Logger and the Circular Kernel Context Logger .

For more information on using the NT Kernel Logger session as a trace provider, see [Configuring and Starting the NT Kernel Logger Session](configuring-and-starting-the-nt-kernel-logger-session.md).

To enable the SystemTraceProvider to start a session other than the NT Kernel Logger, execute the following command.

**tracelog -start MySession -f c:\\Kernel1.etl -eflag PROC\_THREAD+LOADER+CSWITCH**

To programmatically enable the SystemTraceProvider to start a session other than the NT Kernel Logger, use the following steps.

-   Define a private logger name.

    **\#define PRIVATE\_LOGGER\_NAME L”Some Private Trace Session”**

-   At the controller, set the following members of the [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure.

    Set **LogFileMode** to **EVENT\_TRACE\_SYSTEM\_LOGGER\_MODE**.

    Set **LoggerName** to private logger, instead of **KERNEL\_LOGGER\_NAME**.

    Make sure the **Wnode.Guid** member of the [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure is not set to **SystemTraceControlGuid**. You must assign a new **GUID** to this member.

-   At the consumer, set the **LoggerName** member of the [**EVENT\_TRACE\_LOGFILE**](/windows/win32/api/evntrace/ns-evntrace-event_trace_logfilea) structure to this private logger.

> [!Note]  
> If you want a non-administrators or a non-TCB process to be able to start a profiling trace session using the SystemTraceProvider on behalf of third party applications, then you need to grant the user profile privilege and then add this user to both the session **GUID** (created for the logger session) and the system trace provider **GUID** to enable the system trace provider. For more information, see the [**EventAccessControl**](/windows/desktop/api/Evntcons/nf-evntcons-eventaccesscontrol) function.

 

## Related topics

<dl> <dt>

[Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md)
</dt> <dt>

[Configuring and Starting an AutoLogger Session](configuring-and-starting-an-autologger-session.md)
</dt> <dt>

[Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md)
</dt> <dt>

[Configuring and Starting the NT Kernel Logger Session](configuring-and-starting-the-nt-kernel-logger-session.md)
</dt> <dt>

[Updating an Event Tracing Session](updating-an-event-tracing-session.md)
</dt> </dl>

 

 
