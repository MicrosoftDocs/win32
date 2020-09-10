---
title: Startup apps
description: Startup apps
ms.assetid: 3519CB52-A6EC-4819-87FE-C144801BDD9F
keywords:
- startup app
- background task
- Run key
- RunOnce
- startup folder
ms.topic: article
ms.date: 05/31/2018
---

# Startup apps

## Platform

**Clients**   Windows 8  


## Description

One of the big bets with Windows is the ability to light up various form factors, from the traditional desktops and laptops to low-powered tablets. To ensure that our mutual customers have a great experience on any form factor they choose with Windows, two key success metrics that need to be addressed are increased battery life and excellent PC responsiveness. In order to achieve these, improvements have been made in multiple areas of Windows including process life cycle, sleep states and startup apps (apps with automated launch after machine boot). This topic highlights some of the impacts that startup apps have on a Windows device, and provides guidance to developers (ISV/IHV) and OEMs to rethink the usage patterns of startup apps in order to improve battery life and responsiveness for our mutual customers. It also describes the changes in Windows that put users in control of determining which of the startup apps actually get to execute.

Windows Store apps are designed to adhere to new standards of battery consumption and responsiveness, and Windows manages their life cycle by suspending and/or terminating them. However, desktop apps designed for prior Windows versions have not necessarily been designed to preserve battery life or be sensitive to user activity, and can affect system responsiveness (for example, when an app sends a regular 1-second heartbeat to check for updates, or pre-allocates memory upfront in case it needs it later). This can create a poor experience for the user who buys a Windows tablet PC with a long battery life expectancy and weeks of standby, but discovers the tablet s battery life does not achieve these goals. Also, since startup apps run in the background, the number of apps running on the system can be significantly more than what the user is aware of and affect system responsiveness. Startup apps are classified to include those leveraging these mechanisms to start:

-   Run registry keys (HKLM, HKCU, wow64 nodes included)
-   RunOnce registry keys
-   Startup folders under the start menu for per user and public locations

New functionality has been added to Windows to ensure that end users are always in control of the apps that run on their systems. The Startup tab in Task Manager shows a list of startup apps, along with controls that allow users to disable startup apps. To help users determine what to disable, Task Manager displays a measure of each startup app s impact. Impact is assessed based on an app s CPU and disk usage at startup. Impact values are determined by applying these criteria:

-   **High impact**   Apps that use more than 1 second of CPU time or more than 3 MB of disk I/O at startup
-   **Medium impact**   Apps that use 300 ms - 1000 ms of CPU time or 300 KB - 3 MB of disk I/O
-   **Low impact**   Apps that use less than 300 ms of CPU time and less than 300 KB of disk I/O

Microsoft provides tools to help app developers assess, analyze and take steps to reduce their startup impact and improve the user experience. The Assessment and Deployment Kit provides the ability to run a boot performance assessment and measure the impact of apps that run at startup. The assessment results contain detailed analysis and remediation info where applicable, for the top-impacting components at Windows startup. Using the Windows Performance Analyzer, app developers can perform deep analysis to find the root cause of the performance impact and improve Windows startup performance. Install the Windows ADK from [here](/previous-versions/windows/hh825494(v=win.10)).

## Guidance

Startup apps span multiple categories as described in the table below. A set of recommendations for developers is mapped to the categories of startup apps to align with the Windows functional changes described above.



Startup Apps Categories

Description

Recommendation

**Updaters**

Monitor and update users for online updates

**Maintenance Task**

> [!Note]  
> All updates should be maintenance tasks, without any UI interaction requirements. Apps should just update themselves quietly, and rollback on failure

<br/>

${ROWSPAN2}$**Hardware Assistance**${REMOVE}$  

Alternative Access Points

Provide access to Windows features and apps that are accessible via other access points in Windows

**Remove**

> [!Note]  
> The key is to reduce duplicate features that exist in Windows

<br/>

Notifiers

Provide users with notifications regarding their devices

**Remove**

> [!Note]  
> Windows provides notifications to users about their devices

<br/>

**Pre-launchers**

Some of preliminary activities needed by apps is offloaded to a startup app during user login

**Remove**

> [!Note]  
> Windows 8 is optimized for a fast experience for app launches.

<br/>

${ROWSPAN4}$**Utility**${REMOVE}$  

PC Sync

Provide sync functionality across multiple systems

**Startup** (Potential updates in Beta)

Backup & Recovery

Entry point to save and restore the state of files, settings, or entire systems

**Windows Store app for interfacing with the users**

Telemetry

Collect and send info about the user experience and environment

**Maintenance Task**

PC Monitoring

Provide unsolicited system state monitoring and notifications that duplicate existing inbox functionality

**Remove**

> [!Note]  
> The key is to reduce duplicate features that exist in Windows

<br/>

${ROWSPAN2}$**Security**${REMOVE}$  

Parental Control & Filters

Enforce rules and restrictions established for Internet access and usage

**Startup**

Configuration & Management

Allow users to control diagnostic and remediation options for system security monitoring Notify users of findings and security actions

**Windows Store app for interfacing with the users**

**Communication & Internet** (IM & VoIP)

Send and receive messages and calls

**Windows Store app**

**Music & MP3**

Play, store, and manage music

**Windows Store app**

**Photo & Video**

Detect, record, render, store and manage photos and videos

**Windows Store app**

**PC Gaming**

Launch games across various domains

**Windows Store app**

**Upsell & Advertisement**

Draw attention to goods and services available for purchase

**Remove**



 

> [!Note]  
> Accessibility apps guidelines are covered by separate direct engagements with ISVs. See [*Programming for Ease of Access*](../winauto/ease-of-access---assistive-technology-registration.md) for details.

 

**Windows Store apps**

Windows Store apps enhance the user experience by introducing a Windows space with new coordinates: a new app model, a new user interface, and a Windows Store. These language and presentation framework options are available for developing Windows Store apps:

-   HTML/JavaScript/CSS
-   XAML/C#
-   XAML/C++

Aggregated info for developing Windows Store apps is available at the [Windows Dev Center](https://msdn.microsoft.com/windows/apps/).

Examples:

-   [Developing Windows Store games](/previous-versions/windows/apps/hh452744(v=win.10))
-   [Developing Windows Store app that use Media](/previous-versions/windows/apps/hh465132(v=win.10))

**Automatic maintenance tasks**

Periodic background activity should be designed as Automatic Maintenance tasks. These are scheduled at system idle time to increase the responsiveness and energy efficiency of Windows PCs. Maintenance tasks can be created and configured by a desktop app at install time, using the desktop SDK. See the Automatic Maintenance topic that follows for details.

## Resources

-   [Accessibility Guidelines](../winauto/ease-of-access---assistive-technology-registration.md)
-   [Windows Dev Center](https://msdn.microsoft.com/windows/apps/)
-   [Windows ADK](/previous-versions/windows/hh825494(v=win.10))

 

