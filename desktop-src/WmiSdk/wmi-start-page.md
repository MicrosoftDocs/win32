---
title: Windows Management Instrumentation
description: Windows Management Instrumentation (WMI) is the infrastructure for management data and operations on Windows-based operating systems.
ms.assetid: 4804152f-2042-4c6a-83c6-75c5e1ab7a04
ms.tgt_platform: multiple
ms.topic: article
ms.date: 02/03/2023
---

# Windows Management Instrumentation

Windows Management Instrumentation (WMI) is the infrastructure for management data and operations on Windows-based operating systems. Although you can write WMI scripts or applications to automate administrative tasks on remote computers, WMI also supplies management data to other parts of the operating system and products. For example, System Center Operations Manager or [Windows Remote Management](/windows/win32/WinRM/portal).

> [!NOTE]  
> This documentation is for developers and IT administrators only. If you're an end-user who has experienced a WMI error message, search for the error code in [Microsoft Support](https://support.microsoft.com/). For more information about troubleshooting problems with WMI scripts and the WMI service, see [WMI isn't working](/previous-versions/tn-archive/ff406382(v=msdn.10)).

WMI is fully supported by Microsoft. The latest version of administrative scripting and control is available through the Windows Management Infrastructure (MI). MI is fully compatible with previous versions of WMI, and provides a host of features and benefits that make designing and developing providers and clients easy. For more information, see [Windows Management Infrastructure](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure).

## Where is WMI applicable?

Although system administrators can use WMI in all Windows-based applications, it's most useful in enterprise applications and administrative scripts. For more information about WMI, see [Further information for WMI](further-information.md).

## Developer audience

WMI is designed for programmers who create C, C++, and Visual Basic applications, or use a scripting language that has a Windows engine and handles Microsoft ActiveX objects. Although some familiarity with COM programming is helpful, it's not required. C++ developers can find examples for getting started at [Create a WMI application using C++](creating-a-wmi-application-using-c-.md).

To develop managed-code providers or applications in C# or Visual Basic using the .NET Framework, see [Use WMI with the .NET Framework](/previous-versions/dotnet/netframework-1.1/aa310909(v=vs.71)).

Many administrators and IT professionals access WMI through Windows PowerShell. The `Get-WMI` cmdlet for PowerShell enables you to retrieve information for a local or remote WMI repository. As such, several WMI articles, especially [Create WMI clients](creating-wmi-clients.md), contain PowerShell examples. For more information about using PowerShell, see [PowerShell](/powershell/).

## Run-time requirements

For more information about which operating system is required to use a specific API element or WMI class, see the Requirements section of each article in the WMI documentation.

If an expected component appears to be missing, see [Operating system availability of WMI components](operating-system-availability-of-wmi-components.md).

To create scripts or applications for WMI, developers don't need to download or install a specific software development kit (SDK). However, certain WMI administrative tools might be useful to use. For more information, see [Downloads](further-information.md#downloads).

## In this section

| Article | Description |
| - | - |
| [About WMI](about-wmi.md) | General information about WMI. |
| [Using WMI](using-wmi.md) | Information about how to develop applications to use WMI, which includes information about tools. |
| [WMI reference](wmi-reference.md) | Documentation about the WMI classes, WMI C++ classes, WMI COM API, scripting API, and other WMI reference material. |
| [WMI glossary](wmi-glossary.md) | A list of WMI terms. Many of these terms are familiar to developers, but have new or altered definitions in the WMI environment. |
