---
Description: 'You can use the WMI Component Object Model (COM) API to write management client applications or create a new WMI provider.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '5fa8f1b5-fd19-4d45-9b53-bc7089eecdb1'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: COM API for WMI
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
| [**IEnumWbemClassObject**](ienumwbemclassobject.md)                         | Enumerator that works with objects of type [**IWbemClassObject**](iwbemclassobject.md). It is similar to standard COM enumerators, such as [**IEnumVariant**](139e3c93-faef-4003-9079-e0e94494db3e).                                                                                                      |
| [**IMofCompiler**](imofcompiler.md)                                         | Implemented by Mofd.dll, this interface provides a COM interface that is used by the MOF compiler and any other applications that compile MOF files.                                                                                                                                                       |
| [**IUnsecuredApartment**](iunsecuredapartment.md)                           | Used to simplify the process of making asynchronous calls from a client process.                                                                                                                                                                                                                           |
| [**IWbemBackupRestore**](iwbembackuprestore.md)                             | Backs up and restores the contents of the WMI repository.                                                                                                                                                                                                                                                  |
| [**IWbemCallResult**](iwbemcallresult.md)                                   | Used for [semisynchronous](making-a-semisynchronous-call-with-c--.md) calls of the [**IWbemServices**](iwbemservices.md) interface. When making such calls, the called **IWbemServices** method returns immediately, along with an [**IWbemCallResult**](iwbemcallresult.md) object.                    |
| [**IWbemCausalityAnalysis**](iwbemcausalityaccess.md)                       | Tracks child requests that are generated from a parent request.                                                                                                                                                                                                                                            |
| [**IWbemClassObject**](iwbemclassobject.md)                                 | Contains and manipulates both class definitions and class object instances. Developers need not implement this interface; WMI provides its implementation.                                                                                                                                                 |
| [**IWbemConfigureRefresher**](iwbemconfigurerefresher.md)                   | Used by client code to add or remove enumerators, objects, and nested refreshers into a refresher.                                                                                                                                                                                                         |
| [**IWbemContext**](iwbemcontext.md)                                         | Optionally used to communicate additional context information to providers when submitting [**IWbemServices**](iwbemservices.md) calls to Windows Management.                                                                                                                                             |
| [**IWbemDecoupledBasicEventProvider**](iwbemdecoupledbasiceventprovider.md) | Registers decoupled providers with WMI.                                                                                                                                                                                                                                                                    |
| [**IWbemDecoupledRegistrar**](iwbemdecoupledregistrar.md)                   | Associates decoupled providers with WMI. This interface allows a process-hosted provider to define the interoperability lifetime of the interface and coexist with other providers.                                                                                                                        |
| [**IWbemEventConsumerProvider**](iwbemeventconsumerprovider.md)             | Provides the primary interface for an event consumer provider. Through this interface and the [**FindConsumer**](iwbemeventconsumerprovider-findconsumer.md) method, an event consumer provider can indicate which event consumers should receive a given event.                                          |
| [**IWbemEventProvider**](iwbemeventprovider.md)                             | Used to initiate communication with an event provider.                                                                                                                                                                                                                                                     |
| [**IWbemEventProviderQuerySink**](iwbemeventproviderquerysink.md)           | Optionally implemented by event providers who want to know what kinds of event query filters are currently active to optimize performance.                                                                                                                                                                 |
| [**IWbemEventProviderSecurity**](iwbemeventprovidersecurity.md)             | Optionally implemented by event providers who want to restrict consumer access to their event.                                                                                                                                                                                                             |
| [**IWbemEventSink**](iwbemeventsink.md)                                     | Initiates communication with an event provider using a restricted set of queries. This interface extends [**IWbemObjectSink**](iwbemobjectsink.md), providing new methods dealing with security and performance.                                                                                          |
| [**IWbemHiPerfProvider**](iwbemhiperfprovider.md)                           | Enables providers to supply refreshable objects and enumerators.                                                                                                                                                                                                                                           |
| [**IWbemHiPerfEnum**](iwbemhiperfenum.md)                                   | Used in refresher operations to provide rapid access to enumerations of instance objects.                                                                                                                                                                                                                  |
| [**IWbemLocator**](iwbemlocator.md)                                         | Obtains the initial namespace pointer to the [**IWbemServices**](iwbemservices.md) interface for WMI on a specific host computer.                                                                                                                                                                         |
| [**IWbemObjectAccess**](iwbemobjectaccess.md)                               | Provides access to the methods and properties of an object. An [**IWbemObjectAccess**](iwbemobjectaccess.md) object is a container for an instance updated by a [*refresher*](gloss-r.md#wmi-gloss-refresher).                                                                                           |
| [**IWbemObjectSink**](iwbemobjectsink.md)                                   | Used to receive both the results of [**IWbemServices**](iwbemservices.md) and certain types of event notifications.                                                                                                                                                                                       |
| [**IWbemObjectTextSrc**](iwbemobjecttextsrc.md)                             | Used to translate [**IWbemClassObject**](iwbemclassobject.md) instances to and from differing text formats.                                                                                                                                                                                               |
| [**IWbemPropertyProvider**](iwbempropertyprovider.md)                       | Supports retrieving and updating individual properties in an instance of a WMI class.                                                                                                                                                                                                                      |
| [**IWbemProviderIdentity**](iwbemprovideridentity.md)                       | Implemented by an event provider if the provider registers itself using more than one **Name** (multiple instances of [**\_\_Win32Provider**](--win32provider.md)) with the same [CLSID](_com_clsid_progid) value. The class provides a mechanism for distinguishing which named provider should be used. |
| [**IWbemProviderInit**](iwbemproviderinit.md)                               | Used to initialize providers.                                                                                                                                                                                                                                                                              |
| [**IWbemProviderInitSink**](iwbemproviderinitsink.md)                       | Implemented by WMI and called by providers to report initialization status.                                                                                                                                                                                                                                |
| [**IWbemQualifierSet**](iwbemqualifierset.md)                               | Acts as a container for the entire set of named qualifiers for a single property or entire object (a class or instance).                                                                                                                                                                                   |
| [**IWbemQuery**](iwbemquery.md)                                             | Provides an entry point through which a [*WMI Query Language*](gloss-w.md#wmi-gloss-wmi-query-language) (WQL) query can be parsed.                                                                                                                                                                        |
| [**IWbemRefresher**](iwbemrefresher.md)                                     | Provides an entry point through which refreshable objects such as enumerators or refresher objects, can be refreshed.                                                                                                                                                                                      |
| [**IWbemServices**](iwbemservices.md)                                       | Used by clients and providers to access WMI services. The interface is implemented only by WMI and is the primary WMI interface.                                                                                                                                                                           |
| [**IWbemStatusCodeText**](iwbemstatuscodetext.md)                           | Extracts text string descriptions of error codes or the name of the subsystem where the error occurred.                                                                                                                                                                                                    |
| [**IWbemUnboundObjectSink**](iwbemunboundobjectsink.md)                     | Implemented by all logical event consumers. It is a simple sink interface that accepts delivery of event objects.                                                                                                                                                                                          |



 

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

 

 



