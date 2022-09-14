---
description: You can use the WMI Component Object Model (COM) API to write management client applications or create a new WMI provider.
ms.assetid: 5fa8f1b5-fd19-4d45-9b53-bc7089eecdb1
ms.tgt_platform: multiple
title: COM API for WMI
ms.topic: article
ms.date: 05/31/2018
---

# COM API for WMI

You can use the WMI Component Object Model (COM) API to write management client applications or create a new WMI [*provider*](gloss-p.md). The COM API reference provides information for advanced system administrators, as well as developers who are writing client and provider applications.

For more information about writing WMI enterprise management applications, see [Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md). For more information about how to write a WMI provider, see [Providing Data to WMI](providing-data-to-wmi.md).

> [!Note]  
> WMI only supports C++ development using Microsoft Visual C++ version 6.0 and later development systems. However, you can also use other compilers such as those from Borland and Watcom.

 

Each of the different WMI objects inherit from an interface ultimately inherited from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. COM dictates how object implementers, or interfaces, handle tasks such as memory management, parameter management, and multithreading. By conforming to COM, the COM API for WMI ensures that it supports the functionality provided by the interfaces of each WMI object.

WMI is accessed through the following WMI-specific COM interfaces.



| Interface                                                                    | Description                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumWbemClassObject**](/windows/desktop/api/Wbemcli/nn-wbemcli-ienumwbemclassobject)                         | Enumerator that works with objects of type [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject). It is similar to standard COM enumerators, such as [**IEnumVariant**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant).                                                                                                      |
| [**IMofCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler)                                         | Implemented by Mofd.dll, this interface provides a COM interface that is used by the MOF compiler and any other applications that compile MOF files.                                                                                                                                                       |
| [**IUnsecuredApartment**](/windows/desktop/api/Wbemcli/nn-wbemcli-iunsecuredapartment)                           | Used to simplify the process of making asynchronous calls from a client process.                                                                                                                                                                                                                           |
| [**IWbemBackupRestore**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbembackuprestore)                             | Backs up and restores the contents of the WMI repository.                                                                                                                                                                                                                                                  |
| [**IWbemCallResult**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemcallresult)                                   | Used for [semisynchronous](making-a-semisynchronous-call-with-c--.md) calls of the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interface. When making such calls, the called **IWbemServices** method returns immediately, along with an [**IWbemCallResult**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemcallresult) object.                    |
| [**IWbemCausalityAnalysis**](iwbemcausalityaccess.md)                       | Tracks child requests that are generated from a parent request.                                                                                                                                                                                                                                            |
| [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject)                                 | Contains and manipulates both class definitions and class object instances. Developers need not implement this interface; WMI provides its implementation.                                                                                                                                                 |
| [**IWbemConfigureRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemconfigurerefresher)                   | Used by client code to add or remove enumerators, objects, and nested refreshers into a refresher.                                                                                                                                                                                                         |
| [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext)                                         | Optionally used to communicate additional context information to providers when submitting [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) calls to Windows Management.                                                                                                                                             |
| [**IWbemDecoupledBasicEventProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemdecoupledbasiceventprovider) | Registers decoupled providers with WMI.                                                                                                                                                                                                                                                                    |
| [**IWbemDecoupledRegistrar**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemdecoupledregistrar)                   | Associates decoupled providers with WMI. This interface allows a process-hosted provider to define the interoperability lifetime of the interface and coexist with other providers.                                                                                                                        |
| [**IWbemEventConsumerProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventconsumerprovider)             | Provides the primary interface for an event consumer provider. Through this interface and the [**FindConsumer**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventconsumerprovider-findconsumer) method, an event consumer provider can indicate which event consumers should receive a given event.                                          |
| [**IWbemEventProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventprovider)                             | Used to initiate communication with an event provider.                                                                                                                                                                                                                                                     |
| [**IWbemEventProviderQuerySink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventproviderquerysink)           | Optionally implemented by event providers who want to know what kinds of event query filters are currently active to optimize performance.                                                                                                                                                                 |
| [**IWbemEventProviderSecurity**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventprovidersecurity)             | Optionally implemented by event providers who want to restrict consumer access to their event.                                                                                                                                                                                                             |
| [**IWbemEventSink**](iwbemeventsink.md)                                     | Initiates communication with an event provider using a restricted set of queries. This interface extends [**IWbemObjectSink**](iwbemobjectsink.md), providing new methods dealing with security and performance.                                                                                          |
| [**IWbemHiPerfProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemhiperfprovider)                           | Enables providers to supply refreshable objects and enumerators.                                                                                                                                                                                                                                           |
| [**IWbemHiPerfEnum**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemhiperfenum)                                   | Used in refresher operations to provide rapid access to enumerations of instance objects.                                                                                                                                                                                                                  |
| [**IWbemLocator**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemlocator)                                         | Obtains the initial namespace pointer to the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interface for WMI on a specific host computer.                                                                                                                                                                         |
| [**IWbemObjectAccess**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjectaccess)                               | Provides access to the methods and properties of an object. An [**IWbemObjectAccess**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjectaccess) object is a container for an instance updated by a [*refresher*](gloss-r.md).                                                                                           |
| [**IWbemObjectSink**](iwbemobjectsink.md)                                   | Used to receive both the results of [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) and certain types of event notifications.                                                                                                                                                                                       |
| [**IWbemObjectTextSrc**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjecttextsrc)                             | Used to translate [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject) instances to and from differing text formats.                                                                                                                                                                                               |
| [**IWbemPropertyProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbempropertyprovider)                       | Supports retrieving and updating individual properties in an instance of a WMI class.                                                                                                                                                                                                                      |
| [**IWbemProviderIdentity**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemprovideridentity)                       | Implemented by an event provider if the provider registers itself using more than one **Name** (multiple instances of [**\_\_Win32Provider**](--win32provider.md)) with the same [CLSID](../com/clsid.md) value. The class provides a mechanism for distinguishing which named provider should be used. |
| [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit)                               | Used to initialize providers.                                                                                                                                                                                                                                                                              |
| [**IWbemProviderInitSink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinitsink)                       | Implemented by WMI and called by providers to report initialization status.                                                                                                                                                                                                                                |
| [**IWbemQualifierSet**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemqualifierset)                               | Acts as a container for the entire set of named qualifiers for a single property or entire object (a class or instance).                                                                                                                                                                                   |
| [**IWbemQuery**](/windows/desktop/api/Wmiutils/nn-wmiutils-iwbemquery)                                             | Provides an entry point through which a [*WMI Query Language*](gloss-w.md) (WQL) query can be parsed.                                                                                                                                                                        |
| [**IWbemRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemrefresher)                                     | Provides an entry point through which refreshable objects such as enumerators or refresher objects, can be refreshed.                                                                                                                                                                                      |
| [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices)                                       | Used by clients and providers to access WMI services. The interface is implemented only by WMI and is the primary WMI interface.                                                                                                                                                                           |
| [**IWbemStatusCodeText**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemstatuscodetext)                           | Extracts text string descriptions of error codes or the name of the subsystem where the error occurred.                                                                                                                                                                                                    |
| [**IWbemUnboundObjectSink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemunboundobjectsink)                     | Implemented by all logical event consumers. It is a simple sink interface that accepts delivery of event objects.                                                                                                                                                                                          |



 

> [!Note]  
> Many of the WMI COM functions return numeric error codes that are documented as named constants. These constants are defined in Wbemcli.h in the PSDK WMI\\Include folder. For more information, see [WMI Return Codes](wmi-return-codes.md).

 

For more information about the following topics for COM programming, see [Component Development]( /previous-versions//ee663263(v=vs.85)):

-   Interfaces and object design.
-   Implementing [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown).
-   Memory management
-   Handling reference counting.

## Related topics

<dl> <dt>

[WMI Reference](wmi-reference.md)
</dt> </dl>

 

 
