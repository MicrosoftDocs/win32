---
title: MSCluster\_ResourceType class
description: A dynamic WMI class that represents a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7bcd4cbb-bade-4608-8735-dadbb70b1aae
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ResourceType class
- MSCluster_ResourceType class, described
topic_type:
- apiref
api_name:
- MSCluster_ResourceType
- MSCluster_ResourceType.Caption
- MSCluster_ResourceType.InstallDate
- MSCluster_ResourceType.Status
- MSCluster_ResourceType.Flags
- MSCluster_ResourceType.Characteristics
- MSCluster_ResourceType.Name
- MSCluster_ResourceType.DisplayName
- MSCluster_ResourceType.Description
- MSCluster_ResourceType.AdminExtensions
- MSCluster_ResourceType.DllName
- MSCluster_ResourceType.IsAlivePollInterval
- MSCluster_ResourceType.LooksAlivePollInterval
- MSCluster_ResourceType.QuorumCapable
- MSCluster_ResourceType.LocalQuorumCapable
- MSCluster_ResourceType.DeleteRequiresAllNodes
- MSCluster_ResourceType.DeadlockTimeout
- MSCluster_ResourceType.PendingTimeout
- MSCluster_ResourceType.DumpPolicy
- MSCluster_ResourceType.DumpLogQuery
- MSCluster_ResourceType.EnabledEventLogs
- MSCluster_ResourceType.PrivateProperties
- MSCluster_ResourceType.RequiredDependencyTypes
- MSCluster_ResourceType.ResourceClass
- MSCluster_ResourceType.RequiredDependencyClasses
- MSCluster_ResourceType.MaximumMonitors
- MSCluster_ResourceType.DumpServices
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_ResourceType class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [resource type](https://msdn.microsoft.com/library/aa372279).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{2F2EF49D-37DD-47c2-8328-6586142B8C99}"), AMENDMENT]
class MSCluster_ResourceType : MSCluster_LogicalElement
{
  string             Caption;
  datetime           InstallDate;
  string             Status;
  uint32             Flags;
  uint32             Characteristics;
  string             Name;
  string             DisplayName;
  string             Description;
  string             AdminExtensions[];
  string             DllName;
  uint32             IsAlivePollInterval;
  uint32             LooksAlivePollInterval;
  boolean            QuorumCapable;
  boolean            LocalQuorumCapable;
  boolean            DeleteRequiresAllNodes;
  uint32             DeadlockTimeout;
  uint32             PendingTimeout;
  uint64             DumpPolicy;
  string             DumpLogQuery[];
  string             EnabledEventLogs[];
  MSCluster_Property PrivateProperties;
  string             RequiredDependencyTypes[];
  uint32             ResourceClass;
  uint32             RequiredDependencyClasses[];
  uint32             MaximumMonitors;
  string             DumpServices[];
};
```

## Members

The **MSCluster\_ResourceType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_ResourceType** class has these methods.



| Method                                                                                  | Description                                                                                                                                                                                    |
|:----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateResourceType**](mscluster-resourcetype-createresourcetype.md)                 | Creates a resource type.<br/>                                                                                                                                                            |
| [**DeleteResourceType**](mscluster-resourcetype-deleteresourcetype.md)                 | Deletes a resource type.<br/>                                                                                                                                                            |
| [**ExecuteResourceTypeControl**](mscluster-resourcetype-executeresourcetypecontrol.md) | Executes a control code on the resource type.<br/>                                                                                                                                       |
| [**GetPossibleOwners**](mscluster-resourcetype-getpossibleowners.md)                   | Gets the possible owners of this resource type.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/> |



 

### Properties

The **MSCluster\_ResourceType** class has these properties.

<dl> <dt>

**AdminExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides the class identifiers (CLSIDs) for the Cluster Administrator extension DLLs that are associated with the resource type.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the resource type.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the characteristics of the resource type. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**DeadlockTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The length of time to wait, in milliseconds, before declaring a deadlock in any call into a resource.

</dd> <dt>

**DeleteRequiresAllNodes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource cannot be deleted unless all nodes are active.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Description)
</dt> </dl>

Provides access to the resource type's [**Description**](https://msdn.microsoft.com/library/aa372290) property.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource type's [**Name**](https://msdn.microsoft.com/library/aa372304) property, which is the name displayed for the resource type.

</dd> <dt>

**DllName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the resource type's [**DllName**](https://msdn.microsoft.com/library/aa372292) property, which is the name of the dynamic-link library (DLL) for the resource type.

</dd> <dt>

**DumpLogQuery**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Queries that can be used to export resource type specific logs.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**DumpPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Control cluster behavior when call into resource times out.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**DumpServices**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The process names and service names to dump if the resource or an instance of the resource type hangs or crashes.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**EnabledEventLogs**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Event logs that are enabled to diagnose problems with resources of the resource type.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the flags set for the resource type. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the resource type was installed. A lack of a value does not indicate that the resource type is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**IsAlivePollInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource type's [**IsAlivePollInterval**](https://msdn.microsoft.com/library/aa372297) property, which is the recommended interval in milliseconds at which the Cluster Service should poll the resource to determine whether it is operational.

</dd> <dt>

**LocalQuorumCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is obsolete.

</dd> <dt>

**LooksAlivePollInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource type's [**LooksAlivePollInterval**](https://msdn.microsoft.com/library/aa372301) property, which is the recommended interval in milliseconds at which the Cluster Service should poll the resource to determine whether it appears operational.

</dd> <dt>

**MaximumMonitors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of RHS instances that can be created due to resources of this type crashing.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Name), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Provides the name of the resource type.

</dd> <dt>

**PendingTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If a resource cannot be brought online or taken offline in the number of milliseconds specified by this property, the resource is forcibly terminated.

</dd> <dt>

**PrivateProperties**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Property**](mscluster-property.md)**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Private properties of the resource type.

</dd> <dt>

**QuorumCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource can be selected as the quorum resource for the cluster.

</dd> <dt>

**RequiredDependencyClasses**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource classes which a resource of this type must depend on.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

**Storage** (1)


</dt> <dd></dd> <dt>

<span id="Network"></span><span id="network"></span><span id="NETWORK"></span>

**Network** (2)


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** (32768)


</dt> <dd></dd> </dl>

</dd> <dt>

**RequiredDependencyTypes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource types which a resource of this type must depend on.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**ResourceClass**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The class of this resource type.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

**Storage** (1)


</dt> <dd></dd> <dt>

<span id="Network"></span><span id="network"></span><span id="NETWORK"></span>

**Network** (2)


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** (32768)


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

A string indicating the current status of the resource type.

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

</dd> </dl>

## Remarks

The **MSCluster\_ResourceType** class is derived from the [**MSCluster\_LogicalElement**](mscluster-logicalelement.md) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_LogicalElement**](mscluster-logicalelement.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





