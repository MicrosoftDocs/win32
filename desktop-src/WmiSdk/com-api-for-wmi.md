---
Description: You can use the WMI Component Object Model (COM) API to write management client applications or create a new WMI provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5fa8f1b5-fd19-4d45-9b53-bc7089eecdb1
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: COM API for WMI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# COM API for WMI

You can use the WMI Component Object Model (COM) API to write management client applications or create a new WMI [*provider*](gloss-p.md#wmi-gloss-provider). The COM API reference provides information for advanced system administrators, as well as developers who are writing client and provider applications.

For more information about writing WMI enterprise management applications, see [Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md). For more information about how to write a WMI provider, see [Providing Data to WMI](providing-data-to-wmi.md).

> [!Note]  
> WMI only supports C++ development using Microsoft Visual C++ version 6.0 and later development systems. However, you can also use other compilers such as those from Borland and Watcom.

 

Each of the different WMI objects inherit from an interface ultimately inherited from the [**IUnknown**](_com_iunknown) interface. COM dictates how object implementers, or interfaces, handle tasks such as memory management, parameter management, and multithreading. By conforming to COM, the COM API for WMI ensures that it supports the functionality provided by the interfaces of each WMI object.

WMI is accessed through the following WMI-specific COM interfaces.



| Interface                                                                    | Description                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumWbemClassObject**](/windows/win32/Wbemcli/nn-wbemcli-ienumwbemclassobject?branch=master)                         | Enumerator that works with objects of type [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master). It is similar to standard COM enumerators, such as [**IEnumVariant**](139e3c93-faef-4003-9079-e0e94494db3e).                                                                                                      |
| [**IMofCompiler**](/windows/win32/Wbemcli/nn-wbemcli-imofcompiler?branch=master)                                         | Implemented by Mofd.dll, this interface provides a COM interface that is used by the MOF compiler and any other applications that compile MOF files.                                                                                                                                                       |
| [**IUnsecuredApartment**](/windows/win32/Wbemcli/nn-wbemcli-iunsecuredapartment?branch=master)                           | Used to simplify the process of making asynchronous calls from a client process.                                                                                                                                                                                                                           |
| [**IWbemBackupRestore**](/windows/win32/Wbemcli/nn-wbemcli-iwbembackuprestore?branch=master)                             | Backs up and restores the contents of the WMI repository.                                                                                                                                                                                                                                                  |
| [**IWbemCallResult**](/windows/win32/Wbemcli/nn-wbemcli-iwbemcallresult?branch=master)                                   | Used for [semisynchronous](making-a-semisynchronous-call-with-c--.md) calls of the [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) interface. When making such calls, the called **IWbemServices** method returns immediately, along with an [**IWbemCallResult**](/windows/win32/Wbemcli/nn-wbemcli-iwbemcallresult?branch=master) object.                    |
| [**IWbemCausalityAnalysis**](iwbemcausalityaccess.md)                       | Tracks child requests that are generated from a parent request.                                                                                                                                                                                                                                            |
| [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master)                                 | Contains and manipulates both class definitions and class object instances. Developers need not implement this interface; WMI provides its implementation.                                                                                                                                                 |
| [**IWbemConfigureRefresher**](/windows/win32/Wbemcli/nn-wbemcli-iwbemconfigurerefresher?branch=master)                   | Used by client code to add or remove enumerators, objects, and nested refreshers into a refresher.                                                                                                                                                                                                         |
| [**IWbemContext**](/windows/win32/WbemCli/nn-wbemcli-iwbemcontext?branch=master)                                         | Optionally used to communicate additional context information to providers when submitting [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) calls to Windows Management.                                                                                                                                             |
| [**IWbemDecoupledBasicEventProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbemdecoupledbasiceventprovider?branch=master) | Registers decoupled providers with WMI.                                                                                                                                                                                                                                                                    |
| [**IWbemDecoupledRegistrar**](/windows/win32/Wbemprov/nn-wbemprov-iwbemdecoupledregistrar?branch=master)                   | Associates decoupled providers with WMI. This interface allows a process-hosted provider to define the interoperability lifetime of the interface and coexist with other providers.                                                                                                                        |
| [**IWbemEventConsumerProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbemeventconsumerprovider?branch=master)             | Provides the primary interface for an event consumer provider. Through this interface and the [**FindConsumer**](/windows/win32/Wbemprov/nf-wbemprov-iwbemeventconsumerprovider-findconsumer?branch=master) method, an event consumer provider can indicate which event consumers should receive a given event.                                          |
| [**IWbemEventProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbemeventprovider?branch=master)                             | Used to initiate communication with an event provider.                                                                                                                                                                                                                                                     |
| [**IWbemEventProviderQuerySink**](/windows/win32/Wbemprov/nn-wbemprov-iwbemeventproviderquerysink?branch=master)           | Optionally implemented by event providers who want to know what kinds of event query filters are currently active to optimize performance.                                                                                                                                                                 |
| [**IWbemEventProviderSecurity**](/windows/win32/Wbemprov/nn-wbemprov-iwbemeventprovidersecurity?branch=master)             | Optionally implemented by event providers who want to restrict consumer access to their event.                                                                                                                                                                                                             |
| [**IWbemEventSink**](iwbemeventsink.md)                                     | Initiates communication with an event provider using a restricted set of queries. This interface extends [**IWbemObjectSink**](iwbemobjectsink.md), providing new methods dealing with security and performance.                                                                                          |
| [**IWbemHiPerfProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbemhiperfprovider?branch=master)                           | Enables providers to supply refreshable objects and enumerators.                                                                                                                                                                                                                                           |
| [**IWbemHiPerfEnum**](/windows/win32/Wbemcli/nn-wbemcli-iwbemhiperfenum?branch=master)                                   | Used in refresher operations to provide rapid access to enumerations of instance objects.                                                                                                                                                                                                                  |
| [**IWbemLocator**](/windows/win32/Wbemcli/nn-wbemcli-iwbemlocator?branch=master)                                         | Obtains the initial namespace pointer to the [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) interface for WMI on a specific host computer.                                                                                                                                                                         |
| [**IWbemObjectAccess**](/windows/win32/Wbemcli/nn-wbemcli-iwbemobjectaccess?branch=master)                               | Provides access to the methods and properties of an object. An [**IWbemObjectAccess**](/windows/win32/Wbemcli/nn-wbemcli-iwbemobjectaccess?branch=master) object is a container for an instance updated by a [*refresher*](gloss-r.md#wmi-gloss-refresher).                                                                                           |
| [**IWbemObjectSink**](iwbemobjectsink.md)                                   | Used to receive both the results of [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) and certain types of event notifications.                                                                                                                                                                                       |
| [**IWbemObjectTextSrc**](/windows/win32/Wbemcli/nn-wbemcli-iwbemobjecttextsrc?branch=master)                             | Used to translate [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) instances to and from differing text formats.                                                                                                                                                                                               |
| [**IWbemPropertyProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbempropertyprovider?branch=master)                       | Supports retrieving and updating individual properties in an instance of a WMI class.                                                                                                                                                                                                                      |
| [**IWbemProviderIdentity**](/windows/win32/Wbemprov/nn-wbemprov-iwbemprovideridentity?branch=master)                       | Implemented by an event provider if the provider registers itself using more than one **Name** (multiple instances of [**\_\_Win32Provider**](--win32provider.md)) with the same [CLSID](_com_clsid_progid) value. The class provides a mechanism for distinguishing which named provider should be used. |
| [**IWbemProviderInit**](/windows/win32/Wbemprov/nn-wbemprov-iwbemproviderinit?branch=master)                               | Used to initialize providers.                                                                                                                                                                                                                                                                              |
| [**IWbemProviderInitSink**](/windows/win32/Wbemprov/nn-wbemprov-iwbemproviderinitsink?branch=master)                       | Implemented by WMI and called by providers to report initialization status.                                                                                                                                                                                                                                |
| [**IWbemQualifierSet**](/windows/win32/Wbemcli/nn-wbemcli-iwbemqualifierset?branch=master)                               | Acts as a container for the entire set of named qualifiers for a single property or entire object (a class or instance).                                                                                                                                                                                   |
| [**IWbemQuery**](/windows/win32/Wmiutils/nn-wmiutils-iwbemquery?branch=master)                                             | Provides an entry point through which a [*WMI Query Language*](gloss-w.md#wmi-gloss-wmi-query-language) (WQL) query can be parsed.                                                                                                                                                                        |
| [**IWbemRefresher**](/windows/win32/Wbemcli/nn-wbemcli-iwbemrefresher?branch=master)                                     | Provides an entry point through which refreshable objects such as enumerators or refresher objects, can be refreshed.                                                                                                                                                                                      |
| [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master)                                       | Used by clients and providers to access WMI services. The interface is implemented only by WMI and is the primary WMI interface.                                                                                                                                                                           |
| [**IWbemStatusCodeText**](/windows/win32/Wbemcli/nn-wbemcli-iwbemstatuscodetext?branch=master)                           | Extracts text string descriptions of error codes or the name of the subsystem where the error occurred.                                                                                                                                                                                                    |
| [**IWbemUnboundObjectSink**](/windows/win32/Wbemprov/nn-wbemprov-iwbemunboundobjectsink?branch=master)                     | Implemented by all logical event consumers. It is a simple sink interface that accepts delivery of event objects.                                                                                                                                                                                          |



 

> [!Note]  
> Many of the WMI COM functions return numeric error codes that are documented as named constants. These constants are defined in Wbemcli.h in the PSDK WMI\\Include folder. For more information, see [WMI Return Codes](wmi-return-codes.md).

 

For more information about the following topics for COM programming, see [Component Development]( http://go.microsoft.com/fwlink/p/?linkid=195008):

-   Interfaces and object design.
-   Implementing [**IUnknown**](_com_iunknown).
-   Memory management
-   Handling reference counting.

## Related topics

<dl> <dt>

[WMI Reference](wmi-reference.md)
</dt> </dl>

 

 



