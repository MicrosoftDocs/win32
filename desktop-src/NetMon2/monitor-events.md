---
description: Monitors are designed to use Windows Management Instrumentation (WMI) to fire events to local or remote computers.
ms.assetid: b20746dd-d8d9-49b6-95b7-5151ee02901d
title: Monitor Events
ms.topic: article
ms.date: 05/31/2018
---

# Monitor Events

Monitors are designed to use [Windows Management Instrumentation](/windows/desktop/WmiSdk/wmi-start-page) (WMI) to fire events to local or remote computers.

> [!Note]  
> Because monitors use a real-time capture they can only capture data at the local computer. This is a limitation of the network packet provider's **IRTC** interface. However, by using WMI events, the captured data can be examined locally while events can be sent to local or remote computers.

 

Monitors do not communicate directly with WMI. The [*Monitor Control Service*](m.md) (MCSVC) provides an interface (called [IMonitorEventer](imonitoreventer.md)), which the monitor can use to obtain an event data structure and fill it with the relevant information. The MCSVC can then send the event data structure to WMI, which in turn fires the event.

 

 
