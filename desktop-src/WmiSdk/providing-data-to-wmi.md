---
description: WMI makes data about Windows manageable objects available through WMI providers.
ms.assetid: 74558c6e-28b6-479f-9de6-2fbad793ae26
ms.tgt_platform: multiple
title: Providing Data to WMI
ms.topic: article
ms.date: 05/31/2018
---

# Providing Data to WMI

WMI makes data about Windows manageable objects available through WMI [*providers*](gloss-p.md). A provider retrieves data from a system component, such as a process, or an instrumented application, such as SNMP or IIS, and passes that data through WMI to a management application. For example, when an application or script requests process information using the WMI [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) class, the data is obtained dynamically through a preinstalled provider.

The following sections are discussed in this topic:

-   [Creating a Model for a Manageable Object](#creating-a-model-for-a-manageable-object)
-   [Implementing a Model for a Manageable Object](#implementing-a-model-for-a-manageable-object)
-   [Determining a Provider Type to Implement](#determining-a-provider-type-to-implement)
-   [Determining a Hosting (Implementation) Model for a Provider](#determining-a-hosting-implementation-model-for-a-provider)
-   [Implementing a Provider](#implementing-a-provider)
-   [Registering a Provider with WMI and the System](#registering-a-provider-with-wmi-and-the-system)
-   [Testing a Provider](#testing-a-provider)
-   [Related topics](#related-topics)

## Creating a Model for a Manageable Object

Before developing a provider, create a data model to represent the manageable object to be exposed through WMI. You plan which data objects your provider will expose. For example, if you plan to manage the screen resolution of the desktop background, you must decide how to model the Desktop in a [*Managed Object Format (MOF)*](gloss-m.md) file.

To create a useful model:

-   Determine real world scenarios and model the information a customer may want to read and update (for example, changing the background image) for each manageable object. These are your class properties.
-   Determine which kind of actions a customer may want to perform with each manageable object. These are your methods.

## Implementing a Model for a Manageable Object

To implement a model for manageable objects, create a MOF file containing a WMI class that represents each object. For more information about creating a MOF file to define WMI classes, see [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md). The registration of the provider and its classes are usually included in the MOF file, although it is possible to use the [COM API](com-api-for-wmi.md) to create classes and methods. For more information, see [Developing a WMI Provider](developing-a-wmi-provider.md).

> [!Note]  
> To ensure that all your WMI class definitions for managed objects are restored to the [*WMI repository*](gloss-w.md) if WMI has a failure and restarts, use the [**\#pragma autorecover**](pragma-autorecover.md) preprocessor instruction in your [*Managed Object Format (MOF)*](gloss-m.md) file.

 

After you create the MOF file, compile it using the [**Mofcomp.exe**](mofcomp.md) tool. This notifies you of errors in your MOF file, and adds the WMI class defined in the MOF file to the [*WMI repository*](gloss-w.md) so that the class can be used by a provider.

## Determining a Provider Type to Implement

WMI supports a certain number of provider types, which determines the nature of the information delivered and operations supported by the providers.

The provider types are:

-   [*Instance provider*](gloss-i.md)
-   [*Method provider*](gloss-m.md)
-   [*Property provider*](gloss-p.md)
-   Class provider
-   [*Event provider*](gloss-e.md)
-   [*Event consumer provider*](gloss-e.md)
-   [*Association provider*](gloss-a.md)

The vast majority of providers are instance providers and method providers. An instance provider is the most common provider, and it supplies the instances of a given class. A method provider implements the methods of one or more classes. For more information about the types of providers, see [Developing a WMI Provider](developing-a-wmi-provider.md).

## Determining a Hosting (Implementation) Model for a Provider

WMI providers are binaries implemented as COM objects. This means that each provider has a DLL file which can be executed within a specific process and security context. This is what WMI refers to as the [*hosting model*](gloss-h.md). WMI offers various ways to host providers, but the most common approach is to use the coupled provider model (running under the WMI process) in the NetworkServiceHost security context. A WMI provider can be classified as either coupled or [*decoupled*](gloss-d.md).

The term coupled or decoupled provider determines under which host process the provider is running with respect to the WMI provided WMIPRVSE.EXE process. A best practice is to determine if the management data that the provider exposes and the API or application it relies on are always available in the system or not. If the API or application the provider relies on is always available (running on the system), then the provider should be a coupled provider, if not, it must be a decoupled provider. For more information about hosting models, see [Provider Hosting and Security](provider-hosting-and-security.md).

For more information about creating a coupled provider, see [Supplying Data to WMI by Writing a Provider](supplying-data-to-wmi-by-writing-a-provider.md), and for information about incorporating a decoupled provider in an application, see [Incorporating a Provider in an Application](incorporating-a-provider-in-an-application.md).

Coupled providers can be described as in-process (in-proc) or out-of-process (out-of-proc). When a coupled provider is an in-proc provider, it runs under a shared WMIPRVSE.EXE WMI hosting process and is implemented as a COM in-proc server (.dll). When a provider is an out-of-proc provider, it is started by WMI on request of a client or event, but it runs as a separated process and is implemented as an executable (.exe).

## Implementing a Provider

A provider can be implemented in the following ways:

-   Using the ATL Wizard in Visual Studio.

    The ATL Wizard generates provider code that implements a coupled provider. While using the ATL Wizard, you can specify that you want to create an in-proc (.dll) or out-of-proc (.exe) provider run-time model.

-   Defining a COM object to contain your provider.

    The provider code is written in C++. For more information, see [Supplying Data to WMI by Writing a Provider](supplying-data-to-wmi-by-writing-a-provider.md).

-   Using the classes in the [**Microsoft.Management.Infrastructure**](/previous-versions//hh872326(v=vs.85)) namespace in the .NET Framework to create a provider using managed code. (The **System.Management.Instrumentation** namespace is no longer supported.)

    This process creates a decoupled provider.

## Registering a Provider with WMI and the System

Before using the provider from a consumer, it is important to register it with the WMI system and the Windows COM subsystem.

A MOF file can contain multiple types of providers for the same classes. The same provider name is registered as, for example, an instance or a method provider. For more information, see [Registering a Provider](registering-a-provider.md).

## Testing a Provider

When the provider code is registered, it is important to properly test the provider by using the provider from different consumers (for example, scripts, .NET managed code, and C++ consumers).

Perform the following tasks to test your provider:

-   Ensure that your provider is loading properly by tracking the [**MSFT\_WmiProvider\_OperationEvent**](/previous-versions/windows/desktop/wmisystemprov/msft-wmiprovider-operationevent) event notifications. These events will inform you about any provider load failures. Other troubleshooting classes that may be helpful are [**Win32\_ProcessStartTrace**](/previous-versions/windows/desktop/krnlprov/win32-processstarttrace) and [**Win32\_ProcessStopTrace**](/previous-versions/windows/desktop/krnlprov/win32-processstoptrace). For more information about troubleshooting providers, see [Debugging Providers](debugging-providers.md) and [Provider Configuration and Troubleshooting Classes](provider-configuration-and-troubleshooting-classes.md).
-   If the provider is an instance or method provider, ensure you test each provider capability one-by-one to avoid confusion in following your code logic.
-   For an instance provider, create a client application or script that invokes every interface of the provider (enumeration, get, put, and delete). Even if the provider is not supposed to implement anything, it should return a "not supported" message. You can find the return values already defined in [WMI Return Codes](wmi-return-codes.md).
-   To ensure that the desired security context is working as planned, invoke the provider supported operations from a nonadministrator security context. The provider must support impersonation. If a user lacking the correct security credentials tries to update data or perform an operation that executes a method, your provider should deny access with the appropriate error message.
-   For more information about provider security, see [Securing Your Provider](securing-your-provider.md).

## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Provider Hosting and Security](provider-hosting-and-security.md)
</dt> <dt>

[Supplying Data to WMI by Writing a Provider](supplying-data-to-wmi-by-writing-a-provider.md)
</dt> <dt>

[Incorporating a Provider in an Application](incorporating-a-provider-in-an-application.md)
</dt> <dt>

[Registering a Provider](registering-a-provider.md)
</dt> <dt>

[Troubleshooting WMI Client Applications](troubleshooting-wmi-client-applications.md)
</dt> <dt>

[Securing Your Provider](securing-your-provider.md)
</dt> <dt>

[Getting and Providing Data on a 64-bit Platform](getting-and-providing-data-on-a-64-bit-computer.md)
</dt> </dl>

 

 
