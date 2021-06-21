---
description: Microsoft Message Queuing (MSMQ) - Improved Queue Handling
ms.assetid: 49bdfdfa-c77e-4a57-8079-bf4ff6b5010b
title: Microsoft Message Queuing (MSMQ) - Improved Queue Handling
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Message Queuing (MSMQ) - Improved Queue Handling

## Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

MSMQ Service does not put a hard limit on the number of queues that can be created on a system. However, the performance of the system is impacted when a large number of queues is created. Specifically, when there are more than a few thousand queues, the start-up time of the MSMQ Service increases exponentially resulting in a visible impact.

Microsoft has optimized the MSMQ Service start-up in Windows 7 to reduce the lookup overhead for loading the queues into memory. This optimization has led to a dramatic improvement of the start-up time of the MSMQ Service even when several thousand queues are created in the system.

## Manifestation of Impact

This performance improvement does not impact the functionality of any existing application.

## Leveraging the Changed Feature

Application developers using MSMQ on Windows 7 can now architect their solutions without limiting the number of queues. Note that the number of queues still affects overall performance of the MSMQ Server, but the performance impact is now on a linear rather than exponential scale.

## Compatibility, Performance, Reliability, and Usability Tests

If you use a large number of queues, simulate the production environment on a test bed, monitor performance, and analyze the service start-up time and the message throughput with a large number of queues and messages present in the test system.

 

 



