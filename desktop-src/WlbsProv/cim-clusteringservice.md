---
title: CIM\_ClusteringService class
description: CIM\_ClusteringService represents the functionality provided by a cluster. For example, failover functionality may be modeled as a service of a failover cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ad2707e6-1dc4-4055-89da-e5be40c75f58
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ClusteringService class
- CIM_ClusteringService class, described
topic_type:
- apiref
api_name:
- CIM_ClusteringService
- CIM_ClusteringService.Caption
- CIM_ClusteringService.Description
- CIM_ClusteringService.InstallDate
- CIM_ClusteringService.Status
- CIM_ClusteringService.CreationClassName
- CIM_ClusteringService.Name
- CIM_ClusteringService.StartMode
- CIM_ClusteringService.Started
- CIM_ClusteringService.SystemCreationClassName
- CIM_ClusteringService.SystemName
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ClusteringService class

**CIM\_ClusteringService** represents the functionality provided by a cluster. For example, failover functionality may be modeled as a service of a failover cluster.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class CIM_ClusteringService : CIM_Service
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Status;
  string   CreationClassName;
  string   Name;
  string   StartMode;
  boolean  Started;
  string   SystemCreationClassName;
  string   SystemName;
};
```

## Members

The **CIM\_ClusteringService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_ClusteringService** class has these methods.



| Method                                                     | Description                                                                                                                                                                                                                                                                                                      |
|:-----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddNode**](cim-clusteringservice-addnode.md)           | AddNode brings a new computer system into a cluster. The node to be added is specified as a parameter to the method. The return value should be 0 if the computer system is successfully added, 1 if the method is not supported and any other number if an error occurred.<br/>                           |
| [**EvictNode**](cim-clusteringservice-evictnode.md)       | EvictNode removes a computer system from a cluster. The node to be evicted is specified as a parameter to the method. The return value should be 0 if the computer system is successfully evicted, 1 if the method is not supported and any other number if an error occurred.<br/>                        |
| [**StartService**](cim-clusteringservice-startservice.md) | The StartService method places the service in the started state. It returns an integer value of 0 if the service was successfully started, 1 if the request is not supported and any other number to indicate an error.<br/> This method is inherited from [**CIM\_Service**](cim-service.md).<br/> |
| [**StopService**](cim-clusteringservice-stopservice.md)   | The StopService method places the service in the stopped state. It returns an integer value of 0 if the service was successfully stopped, 1 if the request is not supported and any other number to indicate an error.<br/> This method is inherited from [**CIM\_Service**](cim-service.md).<br/>  |



 

### Properties

The **CIM\_ClusteringService** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The InstallDate property is a datetime value indicating when the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name"), [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The Name property uniquely identifies the service and provides an indication of the functionality that is managed. This functionality is described in more detail in the object's Description property.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**Started**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Started is a boolean indicating whether the service has been started (TRUE), or stopped (FALSE).

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**StartMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

StartMode is a string value indicating whether the service is automatically started by a operating system, or only started upon request.

This property is inherited from [**CIM\_Service**](cim-service.md).

<dt>



 ("Automatic")


</dt> <dd></dd> <dt>



 ("Manual")


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

The Status property is a string indicating the current status of the object. Various operational and non-operational statuses can be defined. Operational statuses are "OK", "Degraded" and "Pred Fail". "Pred Fail" indicates that an element may be functioning properly but predicting a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses can also be specified. These are "Error", "Starting", "Stopping" and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.CreationClassName"), [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping System's CreationClassName.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.Name"), [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the system that hosts this service

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 





