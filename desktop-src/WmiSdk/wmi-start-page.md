---
description: Windows Management Instrumentation (WMI) is the infrastructure for management data and operations on Windows-based operating systems.
ms.assetid: 4804152f-2042-4c6a-83c6-75c5e1ab7a04
ms.tgt_platform: multiple
title: Windows Management Instrumentation
ms.topic: article
ms.date: 05/31/2018
---

# Windows Management Instrumentation

## Purpose

Windows Management Instrumentation (WMI) is the infrastructure for management data and operations on Windows-based operating systems. You can write WMI scripts or applications to automate administrative tasks on remote computers but WMI also supplies management data to other parts of the operating system and products, for example System Center Operations Manager, formerly Microsoft Operations Manager (MOM), or Windows Remote Management ([WinRM](/windows/desktop/WinRM/portal)).

> [!Note]  
> The following documentation is targeted for developers and IT administrators. If you are an end-user that has experienced an error message concerning WMI, you should go to [Microsoft Support](https://support.microsoft.com/) and search for the error code you see on the error message. For more information about troubleshooting problems with WMI scripts and the WMI service, see [WMI Isn't Working!](/previous-versions/tn-archive/ff406382(v=msdn.10))

 

> [!Note]  
> WMI is fully supported by Microsoft; however, the latest version of administrative scripting and control is available through the Windows Management Infrastructure (MI). MI is fully compatible with previous versions of WMI, and provides a host of features and benefits that make designing and developing providers and clients easier than ever. For more information, see [Windows Management Infrastructure (MI)](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure).

 

## Where applicable

WMI can be used in all Windows-based applications, and is most useful in enterprise applications and administrative scripts.

System administrators can find information about using WMI at the TechNet [ScriptCenter](https://www.microsoft.com/technet/scriptcenter/default.mspx), and in various books about WMI. For more information, see [Further Information](further-information.md).

## Developer audience

WMI is designed for programmers who use C/C++, the Microsoft Visual Basic application, or a scripting language that has an engine on Windows and handles Microsoft ActiveX objects. While some familiarity with COM programming is helpful, C++ developers who are writing applications can find good examples for getting started at [Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md).

To develop managed code providers or applications in C# or Visual Basic .NET using the .NET Framework, see [WMI in .NET Framework](/previous-versions/dotnet/netframework-1.1/aa720264(v=vs.71)).

Many administrators and IT professionals access WMI through PowerShell. The Get-WMI cmdlet for PowerShell enables you to retrieve information for a local or remote WMI repository. As such, a number of topics and classes, especially in the [Creating WMI Clients](creating-wmi-clients.md) section, contain PowerShell examples. For additional information on using PowerShell, see [Windows PowerShell](https://msdn.microsoft.com/library/dd835506.aspx) and [Scripting with Windows PowerShell](https://technet.microsoft.com/library/bb978526.aspx).

## Run-time requirements

For more information about which operating system is required to use a specific API element or WMI class, see the Requirements section of each topic in the WMI documentation.

If an expected component appears to be missing, see [Operating System Availability of WMI Components](operating-system-availability-of-wmi-components.md).

You do not need to download or install a specific software development (SDK) in order to create scripts or applications for WMI. However, there are some WMI administrative tools that developers find useful. For more information, see the Downloads section in [Further Information](further-information.md).

## In this section

<dl> <dt>

[About WMI](about-wmi.md)
</dt> <dd>

General information about WMI.

</dd> <dt>

[Using WMI](using-wmi.md)
</dt> <dd>

Information about how to develop applications to use WMI, which includes information about tools.

</dd> <dt>

[WMI Reference](wmi-reference.md)
</dt> <dd>

Documentation about the WMI classes, WMI C++ classes, WMI COM API, Scripting API, and other WMI reference material.

</dd> </dl>

 

 
