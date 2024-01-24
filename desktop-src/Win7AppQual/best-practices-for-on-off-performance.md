---
description: Best Practices for On/Off Performance
ms.assetid: 872c2a33-327e-41a8-81db-905c46673f13
title: Best Practices for On/Off Performance
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices for On/Off Performance

## Platform

**Clients -** Windows Vista \| Windows 7  
**Servers -** Windows Server 2008 \| Windows Server 2008 R2  

## Description

The system power states (or S-states), as defined in the Advanced Computer Power Interface (ACPI) specification, are colloquially called on/off states since the most common S-state transition is a computer turning on and off. The different on/off state transitions on a system running Windows Vista or Windows 7 are boot, sleep (ACPI S3), hibernate (ACPI S4), and shutdown.

Good performance during these on/off transitions not only improves the perceived quality of a computer, but also greatly affects daily computer usage patterns and system reliability. Customers can become frustrated by systems that take too long to boot or to shut down. Mobile systems that have lengthy sleep and hibernation transitions can unnecessarily deplete battery life. Longer shutdown times can also adversely affect the reliability of mobile systems. For example, they increase the risk of unexpected power cut-offs.

System extensions like drivers, applications, and services can have a significant impact on on/off transition times. This section discusses some of the best practices that application and service developers can follow to avoid delays during boot, standby, and shutdown, and to ensure a responsive post-boot and post-resume user experience. For more details on how to identify on/off performance issues using the Windows Performance Toolkit and implement the below recommendations for your application or service, please refer to the whitepapers in the 'Links to other Resources' section.

## Best Practices

-   Use the Windows Performance Toolkit to measure performance during all on/off transitions.
-   Perform testing in a controlled way, and make comparisons against a valid baseline:
    -   Obtain a baseline measurement on a system with as few system extensions as possible
    -   Add applications and services one at a time
    -   Test for unacceptable regressions in on/off transition times
-   Avoid using managed code for applications on the critical boot path.
-   Ensure that all applications respond quickly to shutdown notifications (WM\_QUERYENDSESSION and WM\_ENDSESSION messages).
-   Reduce delays in the shutdown path of services and applications by minimizing CPU, disk, and network activity in response to shutdown notifications.
-   Avoid delays in processing the suspend notification (WM\_POWERBROADCAST message).
-   Respond quickly to resume events and minimize post-resume CPU, disk, and network usage.
-   Reduce application resource consumption post-boot.
-   Do not start applications from the RunOnce key on every boot.
-   Convert all nonessential services to demand start or trigger start in order to make system resources available during boot.
-   Avoid using load order groups to express service dependencies.
-   Ensure that all running services report this status as soon as possible during boot to avoid blocking the Service Control Manager (SCM).
-   Avoid using managed code for services on the startup path.
-   Do not allow services to opt in to receive pre-shutdown and shutdown notifications (SERVICE\_CONTROL\_PRESHUTDOWN and SERVICE\_CONTROL\_SHUTDOWN control codes) unless absolutely required.
-   Ensure that all services that have opted to receive shutdown notifications respond quickly to the SCM.
-   Verify that services do not opt in to receive suspend notifications unless absolutely required.
-   Ensure that all services respond quickly to resume events and minimize post-resume CPU, disk, and network usage.

## Links to Other Resources

-   -   [Windows On/Off Transitions Solutions Guide](/windows-hardware/test/assessments/onoff-transition-performance)
-   [On/Off Transition Performance Analysis of Windows Vista](/windows-hardware/test/assessments/onoff-transition-performance)
-   [Windows Performance Analysis](https://msdn.microsoft.com/performance/default.aspx)
-   [Windows Performance Toolkit documentation on MSDN](/previous-versions/windows/desktop/xperf/windows-performance-analyzer--wpa-)
-   [Windows Performance Analysis forum](https://social.msdn.microsoft.com/Forums/wptk_v4/threads/)
-   [Event Tracing for Windows on MSDN](../etw/event-tracing-portal.md)

 

 
