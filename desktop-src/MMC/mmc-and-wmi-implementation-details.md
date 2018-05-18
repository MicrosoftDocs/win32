---
title: MMC 2.0 and WMI Implementation Details
description: The procedures outlined in this section describe how to connect to a WMI namespace, retrieve and display information, and receive asynchronous event notifications when the underlying data in the namespace changes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '04b0daab-5843-4390-ae76-3d83df90d067'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMC 2.0 and WMI MMC , implementation details"]
---

# MMC 2.0 and WMI: Implementation Details

The procedures outlined in this section describe how to connect to a WMI namespace, retrieve and display information, and receive asynchronous event notifications when the underlying data in the namespace changes.

Be aware that this discussion does not cover how to implement WMI-related interfaces and methods.

**To connect to a WMI namespace**

1.  Connect to the desired WMI namespace on the desired host computer. To simplify the connection process, use the [**IWbemLocator**](https://msdn.microsoft.com/library/aa391768) interface and its [**ConnectServer**](https://msdn.microsoft.com/library/aa391769) method. This method allows WMI client applications (snap-ins) to obtain a pointer to an [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) object bound to the desired namespace on the desired target computer.
2.  To use the [**IWbemLocator**](https://msdn.microsoft.com/library/aa391768) interface:
    -   Use the COM API function [**CoCreateInstance**](_com_cocreateinstance) to create an instance of the [**IWbemLocator**](https://msdn.microsoft.com/library/aa391768) interface in-process. **CoCreateInstance** returns an **IWbemLocator** interface pointer, which you can use to call the [**ConnectServer**](https://msdn.microsoft.com/library/aa391769) method.
    -   Call the [**ConnectServer**](https://msdn.microsoft.com/library/aa391769) method to specify the WMI namespace that the snap-in connects to. The method returns a pointer to an [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) object bound to the desired namespace. This is the "services pointer" that the snap-in uses to access WMI services for the namespace.

Most information in WMI is represented as instances of a particular WMI class. The class is the definition of what an object looks like, while the instance is an actual occurrence of the class that contains specific properties. It is possible to enumerate all instances of a given class, request a subset of the instances that match the criteria of a query or retrieve a specific instance based on a unique set of key values.

**To retrieve information from WMI**

1.  To enumerate all instances of a known class, call [**CreateInstanceEnum**](https://msdn.microsoft.com/library/aa392097) on the snap-in's [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) pointer. The **CreateInstanceEnum** method returns an [**IEnumWbemClassObject**](https://msdn.microsoft.com/library/aa390857) pointer.
2.  Call the Next method on this [**IEnumWbemClassObject**](https://msdn.microsoft.com/library/aa390857) pointer to get each successive [**IWbemClassObject**](https://msdn.microsoft.com/library/aa391433) pointer.
3.  For smarter filtering, call the [**ExecQuery**](https://msdn.microsoft.com/library/aa392107) method on the [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) pointer, which enables you to use WQL, a subset of the SQL query language, to narrow down the results of the query to the items of interest.
4.  To retrieve a specific instance of a class, call the [**GetObject**](https://msdn.microsoft.com/library/aa392109) method on the [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) pointer, which retrieves that desired instance directly using the keys specified.
5.  Use the various methods of [**IWbemClassObject**](https://msdn.microsoft.com/library/aa391433) to retrieve property, method and qualifier information as desired.

Methods are actions or operations that can be executed against a class or instances of a class. Most methods are defined to operate on an instance of a class. An example of this would be a "compress" method that can be run on instances of a data file class instance. When run, the method would attempt to use a compression algorithm to reduce the size of the file stored on the system.

**To invoke a WMI Method**

1.  Prepare the input and output parameters by calling the [**GetMethod**](https://msdn.microsoft.com/library/aa391443) method on the [**IWbemClassObject**](https://msdn.microsoft.com/library/aa391433) pointer. The input parameter is an **IWbemClassObject** object populated with the required properties. It is not necessary to retrieve the output parameter object before invoking the method. The method will populate the output class as required. Be aware that **GetMethod** must be called on a CIM Class Definition type of **IWbemClassObject**; not on a CIM Instance type.
2.  Use the appropriate methods on [**IWbemClassObject**](https://msdn.microsoft.com/library/aa391433) to fill in the input parameter's properties.
3.  Call [**ExecMethod**](https://msdn.microsoft.com/library/aa392103) on the [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) pointer to invoke the method.
4.  Examine the error codes from [**ExecMethod**](https://msdn.microsoft.com/library/aa392103) itself and the output parameter's properties as appropriate for the particular method.

The Steps outlined in this procedure address the fact that WMI events are received on a WMI-owned thread. By using a snap-in-defined window message, the snap-in can transfer flow control to the main MMC thread where MMC interfaces can be called in response to the WMI event. Be aware that MMC-defined COM interfaces cannot be marshaled.

**To receive asynchronous event notifications**

1.  Implement the WMI interface [**IWbemObjectSink**](https://msdn.microsoft.com/library/aa391787).
2.  For security reasons (see "Asynchronous Event Notification and Security Issues" in the " [MMC and WMI](mmc-and-wmi.md)" topic) snap-ins must use the [**IUnsecuredApartment**](https://msdn.microsoft.com/library/aa391415) interface to bind the snap-in's local object sink (an instance of its [**IWbemObjectSink**](https://msdn.microsoft.com/library/aa391787) implementation) to an unsecured object sink that receives the event notifications. The **IUnsecuredApartment** interface contains the [**CreateObjectStub**](https://msdn.microsoft.com/library/aa391416) method, which the snap-in can use to create the unsecured object sink.
3.  Using the [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) services pointer obtained in the call to [**IWbemLocator::ConnectServer**](https://msdn.microsoft.com/library/aa391769), call the [**IWbemServices::ExecNotificationQueryAsync**](https://msdn.microsoft.com/library/aa392106) method to register for "temporary" WMI events of interest. In the call to **ExecNotificationQueryAsync**, verify that the pResponseHandler parameter contains a pointer to the unsecured object sink created in the call to [**IUnsecuredApartment::CreateObjectStub**](https://msdn.microsoft.com/library/aa391416).

    As registered events become available, WMI calls the [**Indicate**](https://msdn.microsoft.com/library/aa391788) method on the [**IWbemObjectSink**](https://msdn.microsoft.com/library/aa391787) object supplied in the call to [**ExecNotificationQueryAsync**](https://msdn.microsoft.com/library/aa392106).

4.  Handle calls to the snap-in's [**IWbemObjectSink::Indicate**](https://msdn.microsoft.com/library/aa391788) method.

 

 




