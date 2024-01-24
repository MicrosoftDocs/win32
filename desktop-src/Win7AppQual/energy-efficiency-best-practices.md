---
description: Best Practices for Energy Efficiency
ms.assetid: 355abd0e-928e-442e-a724-855d9dd946fc
title: Best Practices for Energy Efficiency
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices for Energy Efficiency

## Platform

 **Clients** – Windows XP \| Windows Vista \| Windows 7  

## Description

Windows-based laptops must meet energy efficiency regulatory requirements such as those of the United States Environmental Protection Agency (EPA) Energy Star program. Furthermore, surveys have shown that longer battery life continues to be what consumers most want and need in laptops. To meet consumer demands, Windows laptops must continually advance in the following areas:

-   Energy efficiency in all usage scenarios, including idle, productivity workloads, DVD and media playback, and industry benchmarks
-   Mobile PC battery life—for hardware platforms and for Windows

The Windows platform is highly reliable and enables fast on-and-off performance. However, extensions provided with mobile PC systems, such as services, system tray applets, drivers, and other software, can significantly affect performance, reliability, and energy efficiency.

Energy efficiency is a complex problem, with factors affected by and affecting all elements of the PC ecosystem. Small enhancements across multiple scenarios can improve energy efficiency, but a single poorly performing application, device, or system feature can increase energy consumption significantly.

Hardware and devices form the foundation for energy efficiency. However, application and service software must also be efficient to allow the system to achieve optimal battery life. Each software component on the system, including the operating system and value-added applications and services, must conform to basic efficiency guidelines. A single misbehaving application or service can eliminate any energy efficiency gains that the latest processor, devices, or platform hardware achieved. For more detailed information regarding battery life and energy efficiency please refer to the [Battery Life Solutions Guide](/windows-hardware/design/component-guidelines/battery-and-charging#).

The principle issues and components that affect battery life in a mobile PC are:

**Battery Characteristics**

-   Size, type, and quality of battery capacity affect battery life
-   The larger the battery, the greater the power supply
-   Larger batteries are more expensive and heavier; users prefer lighter systems

**Hardware Components**

-   Frequency and depth to which hardware can enter lower power states
-   Hardware support of lower power states
-   Driver optimization for energy efficiency

**Operating System–Directed Power Management**

-   Efficiency of Windows code while under a load versus while idle
-   Cooperation level of all components with Windows-directed power management
-   Proper configuration of the operating system to optimize for power management through power policy settings

**Application Software and Services**

-   Efficiency of applications, drivers, and services while under a load versus while idle
-   Cooperation level of applications with Windows–directed power management
-   Software allowance of the system or devices to enter into low-power idle states

A single application or service component can prevent a system from realizing optimal battery life. Although Windows provides many power configuration options, preinstalled software or power policy settings on many systems are not optimized for the host hardware platform.

A common method for evaluating the battery-life impact of preinstalled software is to compare the power consumption of the system with a clean installation of Windows versus a Windows installation that includes value-added software and services. Although a clean installation does not represent the typical platform that OEMs ship to customers, the power consumption comparison can provide insight into the energy-efficiency of preinstalled software.

## Best Practices

To ensure that your application is optimized on Windows platforms, follow these best practices when you design applications or services:

-   **Avoid use of high-resolution periodic timers**

<dl> Using high-resolution periodic timers (<10 ms) reduces the efficiency of processor power-management technologies.  
</dl>

-   **Invest in performance optimizations**

<dl> Every performance optimization is a battery life optimization. Reductions in required resources, such as using less processor time or batching/clustering disk reads, allow system hardware to become idle and enter low-power modes.  
</dl>

-   **Adjust to user power policy**

<dl> Windows Vista and later make it easy for the user to choose the overall power-savings or performance behavior of the system. Your application should respond to changes in power policy and reduce resource usage or increase performance accordingly. For example, an application should disable background activity such as indexing or system scanning when the user has selected a Power Saver power plan.  
</dl>

-   **Reduce resource usage when the system is on battery power**

<dl> Your application should reduce its resource usage - such as background update frequency - when the system is on battery power.  
</dl>

-   **Do not render to the display when it is off**

<dl> The system display might be off for power savings. Your application should not perform unnecessary graphics rendering when the display is off because this wastes system resources and power.  
</dl>

-   **Avoid polling and spinning in tight loops**

<dl> Heavy processor usage reduces the effectiveness of processor power-management technologies such as processor idle states and processor performance states.  
</dl>

-   **Do not prevent the system from turning off the display or idling to sleep**

<dl> Your application should make judicious power requests with the SetThreadExecutionState API. The system should make these requests only when critical operations must delay the system from powering off the display or automatically entering sleep.  
</dl>

-   **Respond to common power-management events**

<dl> Your application should register for and respond to common power-management events, such as system power-source changes and power-on and power-off notifications for the display.  
</dl>

-   **Do not enable debug logging by default; use Event Tracing for Windows instead**

<dl> Periodic debug logging can prevent disk spin-down.  
</dl>

## Links to Other Resources

-   [Battery Life Solutions Guide](/windows-hardware/design/component-guidelines/battery-and-charging#)
-   [Energy Efficiency Portal](https://www.microsoft.com/whdc/system/pnppwr/mobilepwr.mspx)
-   [Windows Performance Toolkit](https://www.microsoft.com/whdc/system/sysperf/perftools.mspx)
