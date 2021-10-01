---
title: Windows Management Instrumentation
description: Windows Management Instrumentation (WMI) is the infrastructure for management data and operations on Windows-based operating systems.
ms.assetid: 4804152f-2042-4c6a-83c6-75c5e1ab7a04
ms.tgt_platform: multiple
ms.topic: article
ms.date: 09/10/2021
---

# Windows Management Instrumentation

## Purpose

Windows Management Instrumentation (WMI) is the infrastructure for management data and operations on Windows-based operating systems. You can write WMI scripts or applications to automate administrative tasks on remote computers, but WMI also supplies management data to other parts of the operating system and products&mdash;for example, System Center Operations Manager (formerly Microsoft Operations Manager (MOM)), or Windows Remote Management ([WinRM](/windows/win32/WinRM/portal)).

> [!NOTE]  
> This documentation is for developers and IT administrators. If you're an end-user who has experienced an error message concerning WMI, then you should go to [Microsoft Support](https://support.microsoft.com/), and search for the error code that you see in the error message. For more information about troubleshooting problems with WMI scripts and the WMI service, see [WMI isn't working!](/previous-versions/tn-archive/ff406382(v=msdn.10))

> [!NOTE]  
> WMI is fully supported by Microsoft. However, the latest version of administrative scripting and control is available through the Windows Management Infrastructure (MI). MI is fully compatible with previous versions of WMI, and it provides a host of features and benefits that make designing and developing providers and clients easier than ever. For more information, see [Windows Management Infrastructure (MI)](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure).

## Where is WMI applicable?

WMI can be used in all Windows-based applications, and is most useful in enterprise applications and administrative scripts.

System administrators can find information about using WMI in various books about WMI. For more information, see [Further information](further-information.md).

## Developer audience

WMI is designed for programmers who use C/C++, the Microsoft Visual Basic application, or a scripting language that has an engine on Windows and handles Microsoft ActiveX objects. While some familiarity with COM programming is helpful, C++ developers who are writing applications can find good examples for getting started at [Creating a WMI application using C++](creating-a-wmi-application-using-c-.md).

To develop managed code providers or applications in C# or Visual Basic .NET using the .NET Framework, see [WMI in .NET Framework](/previous-versions/dotnet/netframework-1.1/aa720264(v=vs.71)).

Many administrators and IT professionals access WMI through PowerShell. The `Get-WMI` cmdlet for PowerShell enables you to retrieve information for a local or remote WMI repository. As such, a number of topics and classes, especially in the [Creating WMI clients](creating-wmi-clients.md) section, contain PowerShell examples. For additional information on using PowerShell, see [Windows PowerShell](/powershell/).

## Run-time requirements

For more information about which operating system is required to use a specific API element or WMI class, see the Requirements section of each topic in the WMI documentation.

If an expected component appears to be missing, see [Operating System availability of WMI components](operating-system-availability-of-wmi-components.md).

You don't need to download or install a specific software development (SDK) in order to create scripts or applications for WMI. However, there are some WMI administrative tools that developers find useful. For more information, see the Downloads section in [Further information](further-information.md).

## In this section

| Topic | Description |
| - | - |
| [About WMI](about-wmi.md) | General information about WMI. |
| [Using WMI](using-wmi.md) | Information about how to develop applications to use WMI, which includes information about tools. |
| [WMI reference](wmi-reference.md) | Documentation about the WMI classes, WMI C++ classes, WMI COM API, scripting API, and other WMI reference material. |
| [WMI glossary](wmi-glossary.md) | Windows Management Instrumentation (WMI) uses its own collection of terms. Many of these terms are familiar to developers, but have new or altered definitions in the WMI environment. |
