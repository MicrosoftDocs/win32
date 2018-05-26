---
title: Msvm\_ConcreteIdentity class
description: An association between two managed elements that represent different aspects of the same underlying entity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ac9052d1-b8ee-4573-96f0-2eda96d4ff85
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_ConcreteIdentity class
- Msvm_ConcreteIdentity class, described
topic_type:
- apiref
api_name:
- Msvm_ConcreteIdentity
- Msvm_ConcreteIdentity.SystemElement
- Msvm_ConcreteIdentity.SameElement
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_ConcreteIdentity class

An association between two managed elements that represent different aspects of the same underlying entity.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ConcreteIdentity : CIM_ConcreteIdentity
{
  CIM_ManagedElement REF SystemElement;
  CIM_ManagedElement REF SameElement;
};
```

## Members

The **Msvm\_ConcreteIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ConcreteIdentity** class has these properties.

<dl> <dt>

**SameElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The second aspect in the association.

This property is inherited from [**CIM\_ConcreteIdentity**](cim-concreteidentity.md).

</dd> <dt>

**SystemElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The first aspect in the association. The use of System in the property name does not limit the scope of the association.

This property is inherited from [**CIM\_ConcreteIdentity**](cim-concreteidentity.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ConcreteIdentity**](cim-concreteidentity.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





