---
description: Winsock Tracing
ms.assetid: '0c430fc2-28e7-4537-a887-4c36d24fedee'
title: Winsock Tracing
ms.topic: article
ms.date: 05/31/2018
---

# Winsock Tracing

## Introduction

Winsock tracing is a troubleshooting feature that can be enabled in retail binaries to trace certain Windows socket events with minimal overhead. The goal of adding retail tracing to Windows Sockets is to allow for better diagnostic capabilities for developers and product support. Winsock network event tracing supports tracing socket operations for IPv4 and IPv6 applications. Winsock catalog change tracing supports tracing changes made to the Winsock catalog by layered service providers (LSPs). Winsock tracing is supported on Windows Vista and later.

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).

 

When an unexpected error occurs on a socket, the main clue to diagnose the problem is the error code returned. Very often, the returned error code does not explain why the error happened, especially when the error is initiated by the underlying network transport. Winsock tracing provides a more verbose tracing level which can log additional information to catch buffer corruption and poorly written applications.

Winsock tracing uses Event Tracing for Windows (ETW), a general-purpose, high-speed tracing facility provided by the operating system. Using a buffering and logging mechanism implemented in the kernel, ETW provides a tracing mechanism for events raised by both user-mode applications and kernel-mode device drivers. Additionally, ETW gives you the ability to enable and disable logging dynamically, making it easy to perform detailed tracing in production environments without requiring reboots or application restarts. The logging mechanism uses buffers that are written to disk by an asynchronous writer thread. This allows large-scale server applications to write events with minimum disturbance. ETW was first introduced on Windows 2000. Support for Winsock tracing using ETW was added on Windows Vista and later. For general information on ETW, see [Improve Debugging And Performance Tuning With ETW](/archive/msdn-magazine/2007/april/event-tracing-improve-debugging-and-performance-tuning-with-etw).

Winsock tracing can only be enabled at the operating system level for all processes and threads running on a computer. Winsock tracing currently cannot be enabled for just a single process or thread. When Winsock network event tracing is enabled, all socket applications (both IPv4 and IPv6) on a computer are traced.

The following topics describe Winsock tracing in more detail:

-   [Winsock Tracing Levels](winsock-tracing-levels.md)
-   [Control of Winsock Tracing](control-of-winsock-tracing.md)
-   [Winsock Network Event Tracing Details](winsock-tracing-event-details.md)
-   [Winsock Catalog Change Tracing Details](winsock-layered-service-provider-tracing-event-details.md)

## Related topics

<dl> <dt>

[Improve Debugging And Performance Tuning With ETW](/archive/msdn-magazine/2007/april/event-tracing-improve-debugging-and-performance-tuning-with-etw)
</dt> <dt>

[Debug and Trace Facilities](debug-and-trace-facilities-2.md)
</dt> </dl>

 

 
