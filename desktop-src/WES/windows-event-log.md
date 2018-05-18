---
title: Windows Event Log
description: The Windows Event Log API defines the schema that you use to write an instrumentation manifest.
ms.assetid: 'c2855190-584b-406d-acff-5ffbf10dbb5e'
---

# Windows Event Log

## Purpose

The Windows Event Log API defines the schema that you use to write an instrumentation manifest. An instrumentation manifest identifies your event provider and the events that it logs. The API also includes the functions that an event consumer, such as the [Event Viewer](http://go.microsoft.com/fwlink/p/?linkid=146293), would use to read and render the events. To write the events defined in the manifest, use the functions included in the [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) (ETW) API.

Windows Event Log supersedes the [Event Logging](https://msdn.microsoft.com/library/windows/desktop/aa363652) API beginning with the Windows Vista operating system.

## Developer audience

Windows Event Log is designed for C/C++ programmers.

## Run-time requirements

Windows Event Log is included in the operating system beginning with Windows Vista and Windows Server 2008.

For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

For complete version history, see [What's New](what-s-new.md).

## In this section



| Topic                                                                     | Description                                                                                                   |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [Using Windows Event Log](using-windows-event-log.md)<br/>         | Procedural guide that shows how to use the Windows Event Log API.<br/>                                  |
| [Windows Event Log Reference](windows-event-log-reference.md)<br/> | The data types, functions, enumerations, structures, constants, and schemas that the API includes.<br/> |



 

## Additional resources

To get answers to your questions and to find out how other people are using Windows Event Log, visit the [Windows Events](http://go.microsoft.com/fwlink/p/?linkid=150901) forum on MSDN.

 

 





