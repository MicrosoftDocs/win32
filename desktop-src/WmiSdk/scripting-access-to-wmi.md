---
description: Scripts can access all WMI classes for hardware and software objects.
ms.assetid: dbb29bc8-a675-4538-99f4-00613c83eeaa
ms.tgt_platform: multiple
title: Scripting Access to WMI
ms.topic: article
ms.date: 05/31/2018
---

# Scripting Access to WMI

Scripts can access all WMI classes for hardware and software objects. Windows Script Host (WSH) scripts can perform operations on file system objects, manipulate network printers, or change environment variables. You can find a variety of administrator tasks and brief guidance on how to accomplish them in WMI at [WMI Tasks for Scripts and Applications](wmi-tasks-for-scripts-and-applications.md). For more information and examples, see the TechNet ScriptCenter [Script Repository](https://www.microsoft.com/technet/scriptcenter/scripts/default.mspx).

If you are new to scripting or to WMI-specific scripting, see the TechNet ScriptCenter section [Getting Started](https://www.microsoft.com/technet/scriptcenter/hubs/start.mspx).

With the [Scripting API for WMI](scripting-api-for-wmi.md), you can develop quick, simple scripts or complex applications. Scripting gives you the same capability of getting information or of configuring most objects in an enterprise as you would have through a C++ or C# application. For more information, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

You cannot write a [*WMI provider*](gloss-p.md) in script. For more information, see [Providing Data to WMI](providing-data-to-wmi.md).

WMI scripts can be written in any scripting language that can interact with ActiveX objects.

Windows PowerShell provides a simple environment for WMI administration and scripting. For more information about PowerShell, see [Getting Started with Windows PowerShell](/powershell/scripting/getting-started/getting-started-with-windows-powershell?view=powershell-7&preserve-view=true).

Active Directory Service Interfaces (ADSI) scripts provides access to Active Directory Domain Services (AD DS) objects. Both WSH and ADSI scripts access objects and allow procedures not available through batch files.

## Related topics

<dl> <dt>

[About WMI](about-wmi.md)
</dt> <dt>

[Scripting API for WMI](scripting-api-for-wmi.md)
</dt> </dl>

 

 
