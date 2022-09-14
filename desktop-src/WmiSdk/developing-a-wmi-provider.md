---
description: A provider is a Component Object Model (COM) object that acts as an intermediary between WMI and a managed object.
ms.assetid: a4f537ba-9081-43b4-acff-4d206de3d9d7
ms.tgt_platform: multiple
title: Developing a WMI Provider
ms.topic: article
ms.date: 05/31/2018
---

# Developing a WMI Provider

A provider is a Component Object Model (COM) object that acts as an intermediary between WMI and a managed object. For example, when an application or script requests disk data using the WMI [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class, the data is obtained dynamically through the preinstalled [Win32 provider](/windows/desktop/CIMWin32Prov/win32-provider).

If you want to supply data through WMI to other applications, you can create an unmanaged code provider by writing a COM server or through the **WMI ATL wizards** in Visual Studio. You can write a managed code provider by using WMI in the .NET Framework. The topics in this section describe the process of writing an unmanaged COM provider.

> [!Note]  
> To ensure that all of your WMI class definitions for managed objects are restored to the [*WMI repository*](gloss-w.md) if WMI has a failure and restarts, use the [**\#pragma autorecover**](pragma-autorecover.md) preprocessor instruction in your Managed Object Format (MOF) file.

 

A provider consists of classes defined in the [*Managed Object Format (MOF)*](gloss-m.md) schema and a DLL file which carries out the functions of the provider. For example, the MOF that defines the classes of the Win32 provider is CIMWin32.mof and the DLL is CIMWin32.dll, both are found in %windir%\\System32\\Wbem.

The MOF schema for the provider may contain several provider types. For example, the [Event Log Provider](/previous-versions/windows/desktop/eventlogprov/event-log-provider) has instance, method, and event provider types in one MOF file named Ntevt.mof. It is recommended that all of the classes and registration schema for related providers be assembled in one file, rather than creating one file per class.

In addition to using preinstalled providers, you can create your own provider to supply information about a hardware device or the operations of software.

The following table lists the basic tasks that create a provider.



| Task                                                                                                                                                            | Description                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md)                                                              | Develop a model for the entities you want to manage through WMI and create a Managed Object Format (MOF) file to describe the schema.<br/> |
| [Supplying Data to WMI by Writing a Provider](supplying-data-to-wmi-by-writing-a-provider.md)                                                                  | Create the most basic provider that is coupled to WMI.<br/>                                                                                |
| [Incorporating a Provider in an Application](incorporating-a-provider-in-an-application.md)                                                                    | Include the provider as a component within an application if it does not run all of the time.<br/>                                         |
| [Registering a Provider](registering-a-provider.md)                                                                                                            | Register the provider with COM and WMI.<br/>                                                                                               |
| [Initializing a Provider](initializing-a-provider.md)                                                                                                          | Implement the [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) and [**IWbemProviderInitSink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinitsink) interfaces.<br/>   |
| [Making Calls to WMI](making-calls-to-wmi.md)                                                                                                                  | Call WMI interfaces from a provider.<br/>                                                                                                  |
| [Impersonating a Client](impersonating-a-client.md)                                                                                                            | Set security to access a client application.<br/>                                                                                          |
| [Updating a Provider](updating-a-provider.md)                                                                                                                  | Improve the provider as needed.<br/>                                                                                                       |
| [Unloading a Provider](unloading-a-provider.md)                                                                                                                | Remove the provider from memory during shutdown or when the provider is idle.<br/>                                                         |
| [Debugging Providers](debugging-providers.md) and [Provider Configuration and Troubleshooting Classes](provider-configuration-and-troubleshooting-classes.md) | Debug your provider using facilities supplied by WMI.<br/>                                                                                 |
| [Getting and Providing Data on a 64-bit Computer](getting-and-providing-data-on-a-64-bit-computer.md)                                                          | Evaluate whether you need a 32-bit application compatibility provider or if the 64-bit provider can supply data to both clients.<br/>      |



 

The following topics discuss the steps needed to write different types of providers:

-   [Writing an Instance Provider](writing-an-instance-provider.md)
-   [Writing a Method Provider](writing-a-method-provider.md)
-   [Writing an Event Provider](writing-an-event-provider.md)
-   [Writing an Event Consumer Provider](writing-an-event-consumer-provider.md)
-   [Writing a Class Provider](writing-a-class-provider.md)
-   [Writing a Property Provider](writing-a-property-provider.md)
-   [Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md)

 

