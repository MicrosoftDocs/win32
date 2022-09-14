---
description: You can use the methods of an SWbemServices object to perform operations against a namespace on either a local host or a remote host. This object cannot be created by the VBScript CreateObject call.
ms.assetid: 7fcfa404-2fe6-42e5-85ac-64536f6d2a44
ms.tgt_platform: multiple
title: SWbemServices object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices
- ISWbemServices
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices object

You can use the methods of an **SWbemServices** object to perform operations against a namespace on either a local host or a remote host. This object cannot be created by the VBScript **CreateObject** call.

## Members

The **SWbemServices** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemServices** object has these methods.



| Method                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AssociatorsOf**](swbemservices-associatorsof.md)                           | Retrieves the instances of managed resources that are associated with a specified resource through one or more association classes. You provide the object path for the originating endpoint, and [**AssociatorsOf**](swbemservices-associatorsof.md) returns the managed resources at the opposite endpoint. The **AssociatorsOf** method performs the same function that the "ASSOCIATORS OF" WQL query performs.<br/>                                                                           |
| [**AssociatorsOfAsync**](swbemservices-associatorsofasync.md)                 | Asynchronously returns a collection of objects (classes or instances) that are associated with a specified object.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| [**Delete**](swbemservices-delete.md)                                         | Deletes an instance of a managed resource (or a class definition from the CIM repository).<br/>                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**DeleteAsync**](swbemservices-deleteasync.md)                               | Asynchronously deletes the class or instance that is specified in the object path.<br/>                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**ExecMethod**](swbemservices-execmethod.md)                                 | Provides an alternative way to execute a method defined by a managed resource class definition. Primarily used in situations in which the scripting language does not support out parameters. For example, JScript does not support out parameters.<br/>                                                                                                                                                                                                                                            |
| [**ExecMethodAsync**](swbemservices-execmethodasync.md)                       | Asynchronously executes a method that is exported by a method provider.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**ExecNotificationQuery**](swbemservices-execnotificationquery.md)           | Executes an event subscription query to receive events. An event subscription query is a query that defines a change to the managed environment that you want to monitor. When the change occurs, the WMI infrastructure delivers an event describing the change to the calling script.<br/>                                                                                                                                                                                                        |
| [**ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md) | Asynchronously executes a query to receive events.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**ExecQuery**](swbemservices-execquery.md)                                   | Executes a query to retrieve a collection of instances of WMI-managed resources (or class definitions). [**ExecQuery**](swbemservices-execquery.md) can be used to retrieve a filtered collection of instances that match criteria you define in the query passed to **ExecQuery**.<br/>                                                                                                                                                                                                           |
| [**ExecQueryAsync**](swbemservices-execqueryasync.md)                         | Asynchronously executes a query to retrieve objects.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**Get**](swbemservices-get.md)                                               | Retrieves a single instance of a managed resource (or class definition) based on an object path.<br/>                                                                                                                                                                                                                                                                                                                                                                                               |
| [**GetAsync**](swbemservices-getasync.md)                                     | Asynchronously retrieves an object, that is either a class definition or an instance, based on the object path.<br/>                                                                                                                                                                                                                                                                                                                                                                                |
| [**InstancesOf**](swbemservices-instancesof.md)                               | Retrieves all the instances of a managed resource based on a class name. By default, [**InstancesOf**](swbemservices-instancesof.md) performs a deep retrieval. That is, **InstancesOf** retrieves the instances of the resource identified by the class name passed to the method and also retrieves all the instances of all the resources that are subclasses (defined beneath) of the target class.<br/>                                                                                       |
| [**InstancesOfAsync**](swbemservices-instancesofasync.md)                     | Asynchronously returns the instances of a specified class according to the user-specified selection criteria.<br/>                                                                                                                                                                                                                                                                                                                                                                                  |
| [**ReferencesTo**](swbemservices-referencesto.md)                             | Returns all of the associations that reference a specified resource. The best way to understand [**ReferencesTo**](swbemservices-referencesto.md) is to compare it with the [**AssociatorsOf**](swbemservices-associatorsof.md) method. **AssociatorsOf** returns the dynamic resources that are at the opposite end of an association. **ReferencesTo** returns the association itself. The **ReferencesTo** method performs the same function that the "REFERENCES OF" WQL query performs.<br/> |
| [**ReferencesToAsync**](swbemservices-referencesto.md)                        | Asynchronously returns a collection of all association classes or instances that refer to a specific class or instance.<br/>                                                                                                                                                                                                                                                                                                                                                                        |
| [**SubclassesOf**](swbemservices-subclassesof.md)                             | Retrieves all the subclasses of a specified class from the CIM repository.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**SubclassesOfAsync**](swbemservices-subclassesofasync.md)                   | Asynchronously returns a collection of subclasses for a specified class.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |



 

### Properties

The **SWbemServices** object has these properties.



| Property                                                 | Access type          | Description                                                                          |
|:---------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------|
| [**Security\_**](swbemservices-security-.md)<br/> | Read-only<br/> | Used to get or set the security settings for an **SWbemServices** object.<br/> |



 

## Remarks

The methods can be called in either the synchronous mode, the asynchronous mode, or the semisynchronous mode. For more information see [Calling a Method](calling-a-method.md).

**Overview**

**SWbemServices** serves two primary roles. First, the **SWbemServices** object represents an authenticated connection to a WMI namespace on a target computer. Second, **SWbemServices** is the Automation object you use to retrieve WMI-managed resources. You can obtain a reference to an **SWbemServices** object in either of two ways:

-   As demonstrated in most of the WMI scripts presented thus far, you can use the VBScript [**GetObject**](https://msdn.microsoft.com/library/e9waz863(v=VS.71).aspx) function in combination with the WMI moniker "winmgmts:". The following example is the simplest form of a WMI connection. The example connects to the default namespace (typically "Root\\CIMv2") on the local computer:

    `Set objSWbemServices = GetObject("winmgmts:")`

-   You can also use the [**SWbemLocator**](swbemlocator.md) object [**ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver) method to obtain a reference to an **SWbemServices** object.

After you obtain a reference to an **SWbemServices** object, you use the object reference to call 1 of 18 methods available using **SWbemServices**. **SWbemServices** can return one of three different WMI scripting library objects ([**SWbemObjectSet**](swbemobjectset.md), [**SWbemObject**](swbemobject.md), or [**SWbemEventSource**](swbemeventsource.md)), depending on the method you call. Knowing the type of object each method returns will help you determine the next step your script must take. For example, if you get back an **SWbemObjectSet**, you must enumerate the collection to access each **SWbemObject** in the collection. If you get back an **SWbemObject**, you can immediately access the object methods and properties without enumerating the collection first.

**Modes of Operation**

**SWbemServices** supports three modes of operation: synchronous, asynchronous, and semisynchronous.

-   **Synchronous**. In synchronous mode, your script blocks (pauses) until the **SWbemServices** method completes. Not only does your script wait, but in cases in which WMI retrieves instances of managed resources, WMI builds the entire [**SWbemObjectSet**](swbemobjectset.md) in memory before the first byte of data is returned to the calling script. This can have an adverse effect on the script performance and on the computer running the script. For example, synchronously retrieving thousands of events from the Windows Event Logs can take a long time and use a lot of memory. For these reasons, synchronous operations are not recommended except for the three methods ([**Delete**](swbemservices-delete.md), [**ExecMethod**](swbemservices-execmethod.md), and [**Get**](swbemservices-get.md)) that are synchronous by default. These methods do not return large data sets, so semisynchronous operation is not required.
-   **Asynchronous**. In asynchronous mode, your script calls one of the nine asynchronous methods and returns immediately. That is, as soon as the asynchronous method is called, your script resumes running the next line of code. To use an asynchronous method, your script must first create an [**SWbemSink**](swbemsink.md) object and a special subroutine called an event handler. WMI performs the asynchronous operation and notifies the script by calling the event handler subroutine when the operation is complete.
-   **Semisynchronous**. Semisynchronous mode is a compromise between synchronous and asynchronous. Semisynchronous operations offer better performance than synchronous operations, yet they do not require the extra knowledge and scripting steps necessary to handle asynchronous operations. This is the default operation type for most WMI queries.

    In semisynchronous mode, your script calls one of the six data retrieval methods and returns immediately. WMI retrieves the managed resources in the background as your script continues to run. As the resources are retrieved, they are immediately returned to your script by way of an SWbemObjectSet. You can begin to access the managed resources without waiting for the entire collection to be assembled.

    There is a caveat to semisynchronous operations when you are working with managed resources that have many instances (many meaning greater than 1,000), such as [**CIM\_DataFile**](/windows/desktop/CIMWin32Prov/cim-datafile) and [**Win32\_NTLogEvent**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogevent). The caveat is a result of how WMI handles instances of managed resources. For each instance of a managed resource, WMI creates and caches an [**SWbemObject**](swbemobject.md) object. When a large number of instances exist for a managed resource, instance retrieval can monopolize available resources, reducing the performance of both the script and the computer.

    To work around the problem, you can optimize semisynchronous method calls using the **wbemFlagForwardOnly** flag. The **wbemFlagForwardOnly** flag, combined with the **wbemFlagReturnImmediately** flag (the default semisynchronous flag), tells WMI to return a forward-only [**SWbemObjectSet**](swbemobjectset.md), which eliminates the large data set performance problem. However, using the **wbemFlagForwardOnly** flag comes with a cost. A forward-only **SWbemObjectSet** can be enumerated only once. After each [**SWbemObject**](swbemobject.md) in a forward-only **SWbemObjectSet** is accessed, the memory allocated to the instance is released.

With the exception of the [**Delete**](swbemservices-delete.md), [**ExecMethod**](swbemservices-execmethod.md), [**Get**](swbemservices-get.md), and nine asynchronous methods, semisynchronous is the default and recommended mode of operation.

**Commonly-used Methods**

The methods most often used in system administration scripts are [**InstancesOf**](swbemservices-instancesof.md), [**ExecQuery**](swbemservices-execquery.md), [**Get**](swbemservices-get.md), and [**ExecNotificationQuery**](swbemservices-execnotificationquery.md). Although often used, **InstancesOf** is not necessarily the recommended way to retrieve information (although it is arguably the easiest way).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemServices<br/>                                                         |
| IID<br/>                      | IID\_ISWbemServices<br/>                                                          |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> <dt>

[Calling a Method](calling-a-method.md)
</dt> </dl>

 

