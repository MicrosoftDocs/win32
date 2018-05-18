---
title: MSCluster\_Service class
description: A dynamic WMI class that represents the Cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '25a9e7c0-5d9a-4459-ae1d-ed0a938ec5e1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_Service class", "MSCluster_Service class, described"]
topic_type:
- apiref
api_name:
- MSCluster_Service
- MSCluster_Service.Caption
- MSCluster_Service.Description
- MSCluster_Service.InstallDate
- MSCluster_Service.Status
- MSCluster_Service.CreationClassName
- MSCluster_Service.Name
- MSCluster_Service.StartMode
- MSCluster_Service.Started
- MSCluster_Service.SystemCreationClassName
- MSCluster_Service.SystemName
- MSCluster_Service.NodeHighestVersion
- MSCluster_Service.NodeLowestVersion
- MSCluster_Service.State
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_Service class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [Cluster service](https://msdn.microsoft.com/library/aa369163).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{8F9030D0-9149-4113-9ADD-6F2101285E5D}"), AMENDMENT]
class MSCluster_Service : CIM_ClusteringService
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Status;
  string   CreationClassName;
  string   Name;
  string   StartMode;
  boolean  Started;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   NodeHighestVersion;
  uint32   NodeLowestVersion;
  string   State;
};
```

## Members

The **MSCluster\_Service** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_Service** class has these methods.



| Method                                   | Description                                             |
|:-----------------------------------------|:--------------------------------------------------------|
| [**Start**](mscluster-service-start.md) | Starts the cluster service.<br/>                  |
| [**Stop**](mscluster-service-stop.md)   | Sends a stop request to the cluster service.<br/> |



 

### Properties

The **MSCluster\_Service** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the service.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_KEY**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Indicates the name of the class or the subclass used in the creation of an instance.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a textual description of the service.

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

Indicates when the service was installed. A lack of a value does not indicate that the service is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Uniquely identifies the Service and provides an indication of the functionality that is managed. This functionality is described in more detail in the Description property.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**NodeHighestVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the highest possible version of Clustering Service with which the node hosting this service can join or communicate.

</dd> <dt>

**NodeLowestVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the lowest possible version of Clustering Service with which the node hosting this service can join or communicate.

</dd> <dt>

**Started**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the service has been started (**TRUE**), or stopped (**FALSE**).

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

A string value indicating whether the Service is automatically started by a System, Operating System, etc. or only started upon request.

This property is inherited from [**CIM\_Service**](cim-service.md).

<dt>



 ("Automatic")


</dt> <dd></dd> <dt>



 ("Manual")


</dt> <dd></dd> </dl>

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of this service.

Values include the following:

"Continue Pending"

"Pause Pending"

"Paused"

"Running"

"Start Pending"

"Stop Pending"

"Stopped"

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the service.

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


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).CreationClassName"), [**CIM\_KEY**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping System's creation class name.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).Name"), [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping system's name.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> </dl>

## Remarks

The **MSCluster\_Service** class is derived from the [**CIM\_ClusteringService**](https://msdn.microsoft.com/library/aa387210) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ClusteringService**](cim-clusteringservice.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





