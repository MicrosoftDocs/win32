---
description: Any scripting language, such as VBScript, that works with ActiveX objects can access WMI data. Applications can access WMI in C++, using the COM API for WMI or in Visual Basic, using the Wbemdisp.tlb type library and the Scripting API for WMI. .
ms.assetid: c0d18827-6b36-4817-8cd9-06cd0f267b28
ms.tgt_platform: multiple
title: Creating a WMI Application or Script
ms.topic: article
ms.date: 05/31/2018
---

# Creating a WMI Application or Script

Any scripting language, such as VBScript, that works with ActiveX objects can access WMI data. Applications can access WMI in C++, using the [COM API for WMI](com-api-for-wmi.md) or in Visual Basic, using the Wbemdisp.tlb [type library](using-the-wmi-scripting-type-library.md) and the [Scripting API for WMI](scripting-api-for-wmi.md). . You can obtain data through WMI by writing a script, an Active Server Page (ASP), or an HTML application (HTA). You can also use Windows PowerShell to obtain data or write scripts. For more information, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script) and [Getting Started with Windows PowerShell](/powershell/scripting/getting-started/getting-started-with-windows-powershell?view=powershell-7&preserve-view=true). The TechNet ScriptCenter at [https://www.microsoft.com/technet](https://technet.microsoft.com/default.aspx) contains hundreds of scripting examples. For more information about print and online resources, see [Further Information](further-information.md).

The following procedure describes how to connect to the WMI service and data store.

**To connect to the WMI service and data store**

1.  Locate the WMI service on a specific machine.
2.  Connect to one or more WMI namespaces.

These operations are different in C++, Visual Basic, .NET Framework languages, or when using a script. Scripts and Visual Basic applications must access classes whose instances are supplied with data by existing providers. But applications written in C++ can do more. For example, an application written in C++ can send events, but a WMI script can only subscribe to receive events.

A WMI provider can be written only in C++ or using the .NET Framework. For more information about writing applications in C# or Visual Basic .NET, see [WMI .NET Overview](/previous-versions/bb404655(v=vs.90)).

For more information about creating applications and scripts for WMI, see:

-   [Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md)
-   [Creating a WMI Script](creating-a-wmi-script.md)
-   [Creating a Managed WMI Client](creating-a-managed-wmi-client.md)

To perform most tasks, use the preinstalled [WMI classes](wmi-classes.md).

## Related topics

<dl> <dt>

[Using WMI](using-wmi.md)
</dt> </dl>

 

 
