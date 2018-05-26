---
title: CIM class overview
description: This topic introduces the core CIM class definition concepts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: CD929AC6-4D25-4786-9230-E2F6587EFC8E
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM class overview

This topic introduces the core CIM class definition concepts.

## Overview of a CIM class

> \[!Important\]  
> This section provides an overview of CIM class declaration concepts for declarations that are references in CDXML. For a more detailed explanation, refer to the WMI provider development documentation.

 

A CIM class is an object oriented abstraction of the entity being managed through a CIMOM infrastructure like WMI. A class can have zero or more properties and methods that are either defined in the class itself or in one of its parent classes. The CIM class methods can be grouped along two dimensions.

-   Intrinsic versus extrinsic methods - Intrinsic methods are the predefined methods that each class should implement. Extrinsic methods are user-defined methods that the class implements in addition to the intrinsic methods.
-   Instance versus static methods - Instance methods are called on an instance of a managed entity and therefore, always get that instance as one of its arguments. Static methods are called on the class and may or may not get a managed entity instance as an argument.

Class declarations are written in the Managed Object File, or MOF, specification language. Below is a simplified example declaration of the Win32\_Process class that represents the Windows processes. The class has a number of Windows-specific properties in addition to the properties it inherits from the standard CIM\_Process class. The class declaration also defines one static method called Create and four instance methods Terminate, GetOwner, GetOwnerSid, and SetPriority.


```mof
class Win32_Process : CIM_Process
{
 [Override("KernelModeTime")] uint64 KernelModeTime = NULL;
 unt32 Priority = NULL;
 [Override("UserModeTime")] uint64 UserModeTime = NULL;
 string ExecutablePath;
 uint32 MaximumWorkingSetSize;
 uint32 MinimumWorkingSetSize;
 uint32 PageFaults;
 PageFileUsage;
 uint32 PeakPageFileUsage;
 uint32 PeakWorkingSetSize;
 uint32 ProcessId;
 uint32 QuotaNonPagedPoolUsage;
 uint32 QuotaPagedPoolUsage;
 uint32 QuotaPeakNonPagedPoolUsage;
 uint32 QuotaPeakPagedPoolUsage;
 string WindowsVersion;
 uint32 ThreadCount;
 uint32 HandleCount;
 uint32 ParentProcessId;
 uint32 SessionId;
 uint64 PrivatePageCount;
 ToSubClass] uint64 PeakVirtualSize;
 uint64 VirtualSize;
 uint64 ReadOperationCount;
 uint64 WriteOperationCount;
 uint64 OtherOperationCount;
 uint64 ReadTransferCount;
 uint64 WriteTransferCount;
 uint64 OtherTransferCount;
 string CommandLine;

 [Static] uint32 Create ([In] string CommandLine, [In] string CurrentDirectory, [In] Win32_ProcessStartup ProcessStartupInformation, [Out] uint32 ProcessId);
 uint32 Terminate ([In] uint32 Reason);
 uint32 GetOwner ([Out] string User, [Out] string Domain);
 uint32 GetOwnerSid ([Out] string Sid);
 uint32 SetPriority ([In] sint32 Priority);
};
```



## Overview of CIM operations

The table below lists the operations that a client can perform on a CIM class. The first five operations (GetInstance, EnumerateInstance, CreateInstance, ModifyInstance, and DeleteInstance) are the intrinsic class methods, and the QueryInstance operation is like an enumeration with a filter. The InvokeMethod operation is a generic mechanism to invoke the extrinsic methods by passing the method name and the method arguments in the invocation payload.



| Operation                    | Description                                                                                                                                                                                                           |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GetInstance                  | Gets a specific instance of a CIM class.                                                                                                                                                                              |
| EnumerateInstances           | Enumerates all instances of a CIM class.                                                                                                                                                                              |
| QueryInstances               | Returns the object instances that match a query. WMI servers support WQL (WMI Query Language) queries only. For more information about WQL, see [Querying with WQL](http://go.microsoft.com/fwlink/p/?linkid=257801). |
| EnumerateAssociatedInstances | Enumerates instances related to a given instance through association.                                                                                                                                                 |
| CreateInstances              | Creates a new instance of CIM class on the server. This method returns the newly created instance.                                                                                                                    |
| ModifyInstance               | Modifies an instance that exists on the server. If the instance does not exist, an error is returned.                                                                                                                 |
| DeleteInstance               | Deletes an existing instance.                                                                                                                                                                                         |
| InvokeMethod                 | Invokes an extrinsic method on the class. This can be an instance or a static method.                                                                                                                                 |



 

In most cases, one PowerShell cmdlet corresponds to one CIM class method. The following table shows a typical mapping between common PowerShell verbs and CIM operations.

> \[!Tip\]  
> This table is only a recommendation. You can implement a cmdlet to call a static method for cmdlets like Get, Set, or Remove as well.

 



| PowerShell verb | CIM operation                                                                 |
|-----------------|-------------------------------------------------------------------------------|
| Get             | GetInstance, EnumerateInstances, QueryInstances, EnumerateAssociatedInstances |
| Set/Update      | ModifyInstance                                                                |
| Remove          | DeleteInstance                                                                |
| New/Add         | CreateInstance                                                                |
| Other verbs     | Extrinsic methods (may be static or instance)                                 |



 

 

 




