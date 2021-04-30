---
description: Winsock Tracing Events details.
ms.assetid: 246AE0BE-E8E2-4291-8BF4-577F889F055B
title: Winsock Tracing Events
ms.topic: article
ms.date: 05/31/2018
---

# Winsock Tracing Events

This section describes detailed information on specific Winsock Tracing Events details.

Winsock tracing is a troubleshooting feature that can be enabled in retail binaries to trace certain Windows socket events with minimal overhead. This feature allows for better diagnostic capabilities for developers and product support. Winsock network event tracing supports tracing socket operations for IPv4 and IPv6 applications. Winsock catalog change tracing supports tracing changes made to the Winsock catalog by layered service providers (LSPs).

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).

 

Winsock tracing uses Event Tracing for Windows (ETW), a general-purpose, high-speed tracing facility provided by the operating system. ETW provides a tracing mechanism for events raised by both user-mode applications and kernel-mode device drivers. ETW can enable and disable logging dynamically, making it easy to perform detailed tracing in production environments without requiring reboots or application restarts. Support for Winsock tracing using ETW was added on Windows Vista and later. For general information on ETW, see [Improve Debugging And Performance Tuning With ETW](/archive/msdn-magazine/2007/april/event-tracing-improve-debugging-and-performance-tuning-with-etw).

The following list provides detailed information for each Winsock tracing event. For additional information on any event, click the event name.



| Event Name                                                            | Description                                                                               |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**AFD\_EVENT\_CREATE**](afd-event-create.md)                        | Winsock network tracing event for a socket creation operation.                            |
| [**AFD\_EVENT\_CLOSE**](afd-event-close.md)                          | Winsock network tracing event for socket close operation.                                 |
| [**WINSOCK\_WS2HELP\_LSP\_INSTALL**](winsock-ws2help-lsp-install.md) | Winsock catalog change event for a layered service provider (LSP) installation operation. |
| [**WINSOCK\_WS2HELP\_LSP\_REMOVE**](winsock-ws2help-lsp-remove.md)   | Winsock catalog change event for a layered service provider (LSP) removal operation.      |
| [**WINSOCK\_WS2HELP\_LSP\_DISABLE**](winsock-ws2help-lsp-disable.md) | Winsock catalog change event for a layered service provider (LSP) disable operation.      |
| [**WINSOCK\_WS2HELP\_LSP\_RESET**](winsock-ws2help-lsp-reset.md)     | Winsock catalog change event for a Winsock catalog reset operation.                       |



 

## Related topics

<dl> <dt>

[Improve Debugging And Performance Tuning With ETW](/archive/msdn-magazine/2007/april/event-tracing-improve-debugging-and-performance-tuning-with-etw)
</dt> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> <dt>

[Winsock Tracing Levels](winsock-tracing-levels.md)
</dt> <dt>

[Control of Winsock Tracing](control-of-winsock-tracing.md)
</dt> <dt>

[Winsock Network Event Tracing Details](winsock-tracing-event-details.md)
</dt> <dt>

[Winsock Catalog Change Tracing Details](winsock-layered-service-provider-tracing-event-details.md)
</dt> </dl>

 

 
