---
description: Roadmap to using WMI to obtain data for client scripts and applications or to provide data to WMI from an application.
ms.assetid: d9a3741c-313f-4b63-8588-696a10d370f5
ms.tgt_platform: multiple
title: Using WMI
ms.topic: article
ms.date: 05/31/2018
---

# Using WMI

You can use WMI from client applications and scripts. It provides an infrastructure that makes it easy to both discover and perform management tasks. In addition, you can add to the set of possible management tasks by creating your own WMI providers.

> [!Note]  
> The next-generation version of WMI for writing applications and scripts is available through the Windows Management Infrastructure (MI). For more information, see [MI Providers and Clients](/previous-versions/windows/desktop/wmi_v2/mi-providers-and-clients-node-page).

 

The following topics are discussed in this section:

-   [Obtaining Data from WMI](#obtaining-data-from-wmi)
-   [Providing Data to WMI](#providing-data-to-wmi)
-   [Important Tasks for WMI](#important-tasks-for-wmi)

## Obtaining Data from WMI

The following procedure describes how to obtain data from WMI by writing a script or application.

**To obtain data from WMI by writing a script or application**

1.  Decide which language to use. For more information about scripting, see [Creating a WMI Script](creating-a-wmi-script.md). For more information about C++, see [Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md). For using more information about C# or WMI .NET, see [WMI .NET Overview](/previous-versions/).

    You can view or manipulate WMI data in many languages. The following table lists the topics that describe how to use the scripting and application languages to obtain data.

    

    
| Application language | Topic | 
|----------------------|-------|
| Scripts written in Microsoft ActiveX script hosting, including Visual Basic Scripting Edition (VBScript) and Perl<br /> | <a href="scripting-api-for-wmi.md">Scripting API for WMI</a>.<br /> Start with <a href="creating-a-wmi-script.md">Creating a WMI Script</a>.<br /> For script code examples, see <a href="wmi-tasks-for-scripts-and-applications.md">WMI Tasks for Scripts and Applications</a> and the TechNet <a href="https://www.microsoft.com/technet/scriptcenter">ScriptCenter</a> Script Repository.<br /> | 
| Windows PowerShell<br /> | <a href="/powershell/scripting/getting-started/getting-started-with-windows-powershell?view=powershell-7">Getting Started with Windows PowerShell</a><br /> WMI PowerShell Cmdlets, such as <a href="/previous-versions//dd315295(v=technet.10)">Get-WmiObject</a>.<br /> | 
| Visual Basic applications<br /> | <a href="scripting-api-for-wmi.md">Scripting API for WMI</a>.<br /> | 
| Active Server Pages<br /> | <a href="scripting-api-for-wmi.md">Scripting API for WMI</a>.<br /> Start with <a href="creating-active-server-pages-for-wmi.md">Creating Active Server Pages for WMI</a>.<br /> | 
| C++ applications<br /> | <a href="com-api-for-wmi.md">COM API for WMI</a>.<br /> Start with <a href="creating-a-wmi-application-using-c-.md">Creating a WMI Application Using C++</a> and <a href="wmi-c---application-examples.md">WMI C++ Application Examples</a> (contains examples).<br /> | 
| .NET Framework applications written in C#, Visual Basic .NET, or J#<br /> | Classes in the <a href="/previous-versions//hh872326(v=vs.85)"><strong>Microsoft.Management.Infrastructure</strong></a> namespace.<br /><blockquote>    [!Note]<br /><strong>System.Management</strong> was the original namespace that covered managed code for WMI. However, the underlying technology for <strong>System.Management</strong> is generally slower than, and does not scale as well as, <a href="/previous-versions//hh872326(v=vs.85)"><strong>Microsoft.Management.Infrastructure</strong></a>. As such, it is not recommended that you use <strong>System.Management</strong> for new projects. (For more information on <strong>System.Management</strong>, see <a href="/previous-versions/bb404655(v=vs.90)">WMI .NET Overview</a>.)    </blockquote><br /> | 


    

     

2.  Ensure that your connections to remote computers work.

    For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

3.  Connecting to WMI on remote computers requires the correct security settings, as explained in [Maintaining WMI Security](maintaining-wmi-security.md). The following table lists the topics that describe how to configure security settings with the scripting and application languages.

    

    | Language                                                      | Topic                                                                                                                                                                                                                                                 |
    |---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Scripts in any language, Visual Basic applications<br/> | [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md)<br/>                                                                                                                 |
    | Active Server Pages<br/>                                | [Configuring IIS 5 and Later for WMI ASP Scripting](configuring-iis-5-for-wmi-asp-scripting.md)<br/>                                                                                                                                           |
    | C++<br/>                                                | [Setting the Default Process Security Level Using C++](setting-the-default-process-security-level-using-c-.md) and [Setting the Security on IWbemServices and Other Proxies](setting-the-security-on-iwbemservices-and-other-proxies.md)<br/> |

    

     

4.  After connecting to WMI, you can obtain data through queries and enumerations.

    For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md) and [Querying with WQL](querying-with-wql.md).

5.  Registry data is available through WMI and you can create new keys and values or modify existing ones.

    For more information, see [Modifying the System Registry](modifying-the-system-registry.md).

6.  You can subscribe to event notifications through WMI, either temporarily between system reboots or permanently.

    For more information, see [Monitoring Events](monitoring-events.md) and [Receiving a WMI Event](receiving-a-wmi-event.md).

7.  Performance counter data for a system is available through WMI.

    The system performance library counters are converted to WMI classes. For more information, see [Monitoring Performance Data](monitoring-performance-data.md).

8.  [WMI Tasks for Scripts and Applications](wmi-tasks-for-scripts-and-applications.md) describes how to do many administrative tasks with WMI.

## Providing Data to WMI

The following procedure describes how to supply data to WMI by writing a provider.

**To supply data to WMI by writing a provider**

-   Decide on the type of provider to write.

    You cannot write a WMI provider in VBScript. However, you can take several other approaches to writing a WMI COM provider:

    -   Using the WMI ATL Wizard in Visual Studio.

        This approach creates an unmanaged COM provider. For more information, see [Adding a WMI Instance Provider](./writing-an-instance-provider.md) and [Adding a WMI Event Provider](./writing-an-event-provider.md).

    -   Using COM directly in any integrated development environment.

        This approach creates an unmanaged COM provider.

    -   Using WMI in the .NET Framework to create a managed code provider.

        This approach creates a managed code provider. Managed code providers can be written in any .NET Framework language, are simpler to write than WMI COM providers, and can obtain data from the WMI [*CIM*](gloss-c.md)-based classes such as [Win32 Classes](/windows/desktop/CIMWin32Prov/win32-provider). However, the .NET Framework WMI provider has some limitations. For more information, see [Managing Applications Using WMI](/previous-versions/dotnet/netframework-1.1/aa720264(v=vs.71)).

    -   Using the [provider framework classes](wmi-c-classes.md) is not recommended.

        The provider framework has been superseded by the WMI ATL wizards, using COM directly, or .NET Framework providers. Creating a WMI COM provider with the provider framework classes is no longer recommended. The following table lists the topics that describe how to use COM or .NET Framework providers.

    

    | Provider                                                      | Topic                                                                                                   |
    |---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
    | COM provider in the same process as WMI<br/>            | [Providing Data to WMI](providing-data-to-wmi.md)<br/>                                           |
    | COM decoupled provider<br/>                             | [Incorporating a Provider in an Application](incorporating-a-provider-in-an-application.md)<br/> |
    | .NET Framework provider in C# or Visual Basic.NET<br/> | [Managing Applications Using WMI](/previous-versions/dotnet/netframework-1.1/aa720264(v=vs.71))<br/>            |

    

     

## Important Tasks for WMI

The following topics provide information about using WMI to monitor and control enterprise components.



| Topic                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WMI Tasks for Scripts and Applications](wmi-tasks-for-scripts-and-applications.md)<br/>                                                 | Describes how to find the correct WMI class and procedures to use in scripts and applications that perform common computer and network administration tasks, such as adding a new printer connection for a remote computer or finding all the installed hotfixes on a computer.<br/>                                                                            |
| [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md)<br/>                                                     | Any scripting language, such as VBScript or Perl, that works with ActiveX objects can access WMI data. Applications can access WMI in C++, using the [COM API for WMI](com-api-for-wmi.md) or in Visual Basic, using the Wbemdisp.tlb[type library](using-the-wmi-scripting-type-library.md) and the [Scripting API for WMI](scripting-api-for-wmi.md).<br/> |
| [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)<br/>                                                 | Describes how scripts, applications, and providers can establish connections to WMI on remote computers to obtain data or control hardware and software.<br/>                                                                                                                                                                                                   |
| [Connecting to WMI on a Remote Computer by Using Windows PowerShell](connecting-to-wmi-on-a-remote-computer-by-using-powershell.md)<br/> | Describes how to use Windows PowerShell to establish connections to WMI on remote computers to obtain data or to control hardware and software.<br/>                                                                                                                                                                                                            |
| [Monitoring Events](monitoring-events.md)<br/>                                                                                           | Describes how to get event notifications by creating temporary or permanent WMI event consumers.<br/>                                                                                                                                                                                                                                                           |
| [Providing Data to WMI](providing-data-to-wmi.md)<br/>                                                                                   | WMI supplies dynamic management data to client scripts and applications by obtaining it from providers.<br/>                                                                                                                                                                                                                                                    |
| [Getting and Providing Data on a 64-bit Computer](getting-and-providing-data-on-a-64-bit-computer.md)<br/>                               | Describes how to access nondefault providers and considerations for provider writers on 64-bit systems.<br/>                                                                                                                                                                                                                                                    |



