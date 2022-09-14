---
description: A monitor is a dynamic-link library (DLL) that examines real-time captures of network traffic.
ms.assetid: 96d04352-5f1c-4964-94d2-692c6b642cb8
title: Monitors
ms.topic: article
ms.date: 05/31/2018
---

# Monitors

A monitor is a dynamic-link library (DLL) that examines real-time captures of network traffic. It searches for pre-defined conditions and then generates events when those conditions are detected. For example, an event may be fired when a network break-in is attempted, when a rogue workstation is handing out IP addresses, or when a router fails.

> [!Note]  
> If you need to perform detailed analyses on network data that requires a post-capture analysis, you must use [*expert*](e.md) and [*parser*](p.md) applications.

 

The [*Monitor Control Service*](m.md) (MCSVC) provides the framework for managing your monitors. It provides functions to load the monitor DLLs, and a communications interface to the Monitor Control Tool so that you can create, configure, start, stop, and disable multiple instances of your monitors.

Monitors run in two threads of execution. The MCSVC provides the first thread, which provides direct control of the monitor. The second thread is provided by the [*network packet provider*](n.md) (NPP), which provides a way to pass the captured network data, statistics, and the status of the capture from the NPP back to the monitor.

More than one instance of the same monitor can exist for each run-time NPP interface used to capture data.

 

 



