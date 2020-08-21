---
title: UI Automation
description: Microsoft UI Automation is an accessibility framework that enables Windows applications to provide and consume programmatic information about user interfaces (UIs).
ms.assetid: 700ca38d-ff40-472b-a95a-11fa94c3bc1d
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation

Microsoft UI Automation is an accessibility framework that enables Windows applications to provide and consume programmatic information about user interfaces (UIs). It provides programmatic access to most UI elements on the desktop. It enables assistive technology products, such as screen readers, to provide information about the UI to end users and to manipulate the UI by means other than standard input. UI Automation also allows automated test scripts to interact with the UI.

-   [Where Applicable](#where-applicable)
-   [Developer Audience](#developer-audience)
-   [Run-Time Requirements](#run-time-requirements)
-   [Support for Down-level Operating Systems](#support-for-down-level-operating-systems)

## Where Applicable

By using UI Automation and following accessible design practices, developers can make applications running on Windows more accessible to many people with vision, hearing, or motion disabilities. Also, UI Automation is specifically designed to provide robust functionality for automated testing scenarios.

## Developer Audience

UI Automation is designed for experienced C/C++ developers. In general, developers need a moderate level of understanding about Component Object Model (COM) objects and interfaces, Unicode, and Windows API programming.

For information about UI Automation for managed code, please see [Accessibility](/dotnet/framework/ui-automation/) in the .NET Framework Developer's Guide section of MSDN.

## Run-Time Requirements

UI Automation is supported on the following operating systems: Windows XP, Windows Server 2003, Windows Server 2003 R2, Windows Vista, Windows 7, Windows 10, Windows Server 2008, Windows Server 2008 R2, Windows Server 2012, Windows Server 2012 R2, Windows Server 2016, and Windows Server 2019.

> [!Note]  
> Windows XP and Windows Server 2003 also require Microsoft .NET Framework 3.0.

 

## Support for Down-level Operating Systems

The Platform Update for Windows Vista is a set of run-time libraries that enables developers to target applications to both Windows 7 and down-level operating systems. The Platform Update for Windows Server 2008 is a set of run-time libraries that enables developers to target applications to both Windows Server 2008 R2 and previous versions of Windows Server. The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 will be available to all Windows Vista and Windows Server 2008 customers through Windows Update. Third-party applications that require Platform Update for Windows Vista or Platform Update for Windows Server 2008 can have Windows Update detect whether it is installed; if it is not, Windows Update will download and install it in the background.

The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 both support the entire Windows Automation API 3.0 feature set on the following operating systems.

-   Windows XP (English) <dl> Windows XP Home SP3 x86  
    Windows XP Professional SP3 x86  
    </dl>
-   Windows Server 2003 (English) <dl> Windows Server 2003 SP2 (x86 and x64)  
    </dl>
-   Windows Vista (English) <dl> Starter SP2 (x86 and x64)  
    Home Premium SP2 (x86 and x64)  
    Business SP2 (x86 and x64)  
    Enterprise SP2 (x86 and x64)  
    Ultimate SP2 (x86 and x64)  
    </dl>
-   Windows Server 2008 (English) <dl> Windows Server 2008 SP2 (x86 and x64)  
    </dl>

For more information about both updates, see [Platform Update for Windows Vista](../win7ip/platform-update-for-windows-vista-portal.md).

## In this section

-   [UI Automation Fundamentals](entry-uiautocore-overview.md)
-   [UI Automation Provider Programmer's Guide](uiauto-providerportal.md)
-   [UI Automation Client Programmer's Guide](uiauto-clientportal.md)
-   [Reference](entry-uiautocore-ref.md)
-   [Samples](samples-entry.md)
-   [Appendixes](appendix-entry.md)

 

 