---
title: MSCluster\_FaultDomain class
description: Describes a node in the fault domain hierarchy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 43f5d4e2-0f14-4c72-b83f-a718ccecdf86
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_FaultDomain class
- MSCluster_FaultDomain class, described
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain
- MSCluster_FaultDomain.Id
- MSCluster_FaultDomain.Name
- MSCluster_FaultDomain.Location
- MSCluster_FaultDomain.Description
- MSCluster_FaultDomain.Type
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_FaultDomain class

Describes a node in the fault domain hierarchy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("MSCLUSTEREXT"), AMENDMENT]
class MSCluster_FaultDomain
{
  string Id;
  string Name;
  string Location;
  string Description;
  uint32 Type;
};
```

## Members

The **MSCluster\_FaultDomain** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_FaultDomain** class has these methods.



| Method                                                               | Description                                                            |
|:---------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**CreateFaultDomain**](mscluster-faultdomain-createfaultdomain.md) | Creates a fault domain.<br/>                                     |
| [**GetChildren**](mscluster-faultdomain-getchildren.md)             | Retrieves the children of the fault domain.<br/>                 |
| [**GetFaultDomainXML**](mscluster-faultdomain-getfaultdomainxml.md) | Gets an XML representation of the cluster fault domains.<br/>    |
| [**GetParent**](mscluster-faultdomain-getparent.md)                 | Gets the parent of the fault domain.<br/>                        |
| [**MoveFaultDomain**](mscluster-faultdomain-movefaultdomain.md)     | Moves the specified fault domain hierarchy to a new parent.<br/> |
| [**RemoveFaultDomain**](mscluster-faultdomain-removefaultdomain.md) | Removes the fault domain from the cluster.<br/>                  |
| [**SetFaultDomain**](mscluster-faultdomain-setfaultdomain.md)       | Changes settings on a fault domain object.<br/>                  |
| [**SetFaultDomainXML**](mscluster-faultdomain-setfaultdomainxml.md) | Sets a fault domain via XML.<br/>                                |



 

### Properties

The **MSCluster\_FaultDomain** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the fault domain.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID that uniquely identifies the fault domain.

</dd> <dt>

**Location**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The physical location of the fault domain.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name of the fault domain.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the current fault domain.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Site"></span><span id="site"></span><span id="SITE"></span>

**Site** (1000)


</dt> <dd></dd> <dt>

<span id="Rack"></span><span id="rack"></span><span id="RACK"></span>

**Rack** (2000)


</dt> <dd></dd> <dt>

<span id="Chassis"></span><span id="chassis"></span><span id="CHASSIS"></span>

**Chassis** (3000)


</dt> <dd></dd> <dt>

<span id="Node"></span><span id="node"></span><span id="NODE"></span>

**Node** (4000)


</dt> <dd></dd> <dt>

<span id="Enclosure"></span><span id="enclosure"></span><span id="ENCLOSURE"></span>

**Enclosure** (5000)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



 

 





