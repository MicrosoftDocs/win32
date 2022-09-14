---
title: Windows Event Log
description: The Windows Event Log API defines the schema that you use to write an instrumentation manifest.
ms.assetid: '738c8afa-4714-4d4f-9231-b8fbdb5159c5'
ms.topic: article
ms.date: 05/31/2018
---

# Windows Event Log

## Purpose

The Windows Event Log API defines the schema that you use to write an instrumentation manifest. An instrumentation manifest identifies your event provider and the events that it logs. The API also includes the functions that an event consumer, such as the [Event Viewer](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc766042(v=ws.11)), would use to read and render the events. To write the events defined in the manifest, use the functions included in the [Event Tracing](/windows/desktop/ETW/event-tracing-portal) (ETW) API.

Windows Event Log supersedes the [Event Logging](/windows/desktop/EventLog/event-logging) API beginning with the Windows Vista operating system.

## Developer audience

Windows Event Log is designed for C/C++ programmers.

## Run-time requirements

Windows Event Log is included in the operating system beginning with Windows Vista and Windows Server 2008.

For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

For complete version history, see [What's New](what-s-new.md).

## In this section


| Topic                                                        | Description                                                                                       |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [Using Windows Event Log](using-windows-event-log.md)        | Procedural guide that shows how to use the Windows Event Log API.                                 |
| [Windows Event Log Reference](windows-event-log-reference.md)| The data types, functions, enumerations, structures, constants, and schemas that the API includes.|