---
description: Notifying CBasePin of Filter State Changes
ms.assetid: 521ba95b-1f2d-4ad0-ab9b-4f1e3343a2d3
title: Notifying CBasePin of Filter State Changes
ms.topic: article
ms.date: 05/31/2018
---

# Notifying CBasePin of Filter State Changes

The **CBasePin** class is notified whenever the state of the owning filter changes. For each state transition, the filter calls a corresponding method on the pin, as shown in the following table.



| New Filter State | CBasePin Method                                 |
|------------------|-------------------------------------------------|
| Stopped          | [**CBasePin::Inactive**](cbasepin-inactive.md) |
| Paused           | [**CBasePin::Active**](cbasepin-active.md)     |
| Running          | [**CBasePin::Run**](cbasepin-run.md)           |



 

The derived class should override these methods to respond to the state change. Depending on the filter, the pin might start a worker thread that delivers samples, commit or decommit its memory allocator, and so forth.

 

 



