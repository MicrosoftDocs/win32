---
title: About NDF
description: The Network Diagnostics Framework (NDF) reduces the involvement of network administrators and computer users by handling common network issues as they occur.
ms.assetid: ac4ef38e-2818-4df4-b9f9-28326b974698
ms.topic: article
ms.date: 05/31/2018
---

# About NDF

The Network Diagnostics Framework (NDF) reduces the involvement of network administrators and computer users by handling common network issues as they occur. By using NDF's diagnostic and repair capabilities, users and administrators do not need additional tools in order to handle some relatively common problems. NDF ships as part of Windows Vista, Windows Server 2008, and later. It is available whenever a system is booted (but cannot run in Safe Mode).

## NDF Helper Classes

NDF includes helper classes that diagnose networking issues as they occur. Each of these helper classes contains the logic required to troubleshoot at least one component or application.

Individual NDF helper classes perform the primary tasks of the diagnostics session. Each helper class is a unit of code designed to evaluate one health aspect of its respective network component. The helper class also understands what possible repair options are available to restore the health of the component, as well as the cost and risk of any particular repair option.

Each helper class plugs into the overall Network Diagnostics Framework. If a third-party network component includes an NDF helper class, problems with that component can be resolved by other applications using NDF, without requiring them to have any specific knowledge of that component.

The helper classes developed by Microsoft provide software developers with the primary diagnostic and repair functionality. There is also a small set of APIs that developers can use to diagnose network problems using NDF. For more information, see [NDF Functions](ndf-functions.md) and [NDF Diagnostics Example](ndf-diagnostics-example.md).

## Extensible Helper Classes

In some cases, more specific diagnostic and repair functionality can be provided by application developers.

Some of Microsoft's NDF helper classes are designed to be extended to provide additional diagnostic and repair capabilities. This means that developers can include functionality to use NDF diagnostic and repair capabilities to troubleshoot issues specific to their software or hardware.

For example, the wireless team at Microsoft provides an extensible helper class that allows any third party wireless vendors to add specific troubleshooting logic for their specific hardware and/or software. They can do this by developing an NDF helper class extension. For more information, see [802.11 Wireless Diagnostics Extensible Helper Classes](802-11-wireless-diagnostics-extensible-helper-classes.md).

An NDF helper class extension, by definition, extends the functionality of an existing extensible helper class. If a helper class is not extensible, no one can write an extension for that helper class.

## Benefits of Helper Class Extensions

NDF offers several distinct advantages to encourage its use by network component developers. At the top of the list is that customers of vendor software will free up some of their own troubleshooting resources and reduce the total cost of ownership. A well-written helper class extension also provides the following benefits:

-   Allows a team to determine when their component is not the cause of a connectivity issue. For example, networking is often blamed for connectivity problems that are not actually the result of a networking component failure. By writing a helper class extension, a team can more easily rule out a particular component as the cause of a connectivity failure.
-   Allows a team to quickly diagnose and debug a problem within the component. Time spent debugging and troubleshooting can be eliminated if a helper class is written to perform all of the standard diagnostic steps that would be required anyway.
-   Eliminates the need to write and support one-off tools to diagnose problems. A helper class can be the central repository for a component's diagnostic capabilities and information gathering techniques.
-   Makes component-specific diagnostics available to applications, without requiring them to have any direct knowledge about the component.

 

 




