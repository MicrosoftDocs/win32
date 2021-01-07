---
description: Event tracing sessions record events from one or more providers.
ms.assetid: 43841d2f-5a4c-493d-9531-21941311ffbc
title: Controlling Event Tracing Sessions
ms.topic: article
ms.date: 05/31/2018
---

# Controlling Event Tracing Sessions

Event tracing sessions record events from one or more [providers](providing-events.md). The controller defines the session and enables the providers. Defining the session typically includes specifying the session and log file name, type of log file to use, and the resolution of the time stamp used to record the events. Controllers can also update and query event tracing sessions.

The following topics demonstrate how to define and update a session, and enable event trace providers:

-   [Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md)
-   [Configuring and Starting a SystemTraceProvider Session](configuring-and-starting-a-systemtraceprovider-session.md)
-   [Configuring and Starting an AutoLogger Session](configuring-and-starting-an-autologger-session.md)
-   [Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md)
-   [Updating an Event Tracing Session](updating-an-event-tracing-session.md)
-   [Retrieving Additional Event Tracing Data](retrieving-additional-event-tracing-data.md)

For information on flushing and querying sessions, see [**ControlTrace**](/windows/win32/api/evntrace/nf-evntrace-controltracea) and [**QueryAllTraces**](/windows/win32/api/evntrace/nf-evntrace-queryalltracesa), respectively.

Only users running with elevated administrative privileges, users in the Performance Log Users group, and applications running as LocalSystem, LocalService or NetworkService can control event tracing sessions. To grant a restricted user the ability to control trace sessions, add them to the Performance Log Users group.

**Windows XP and Windows 2000:** Anyone can control a trace session.

 

 
