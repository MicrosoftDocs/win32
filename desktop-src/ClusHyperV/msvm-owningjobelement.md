---
title: Msvm\_OwningJobElement class
description: Associates a Msvm\_ConcreteJob instance with the Msvm\_Service object that created the job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c102c9e-11de-4bfe-9df6-0d4dff93f8d5
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_OwningJobElement class
- Msvm_OwningJobElement class, described
topic_type:
- apiref
api_name:
- Msvm_OwningJobElement
- Msvm_OwningJobElement.OwningElement
- Msvm_OwningJobElement.OwnedElement
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_OwningJobElement class

Associates a [**Msvm\_ConcreteJob**](msvm-concretejob.md) instance with the [**Msvm\_Service**](msvm-serviceaffectselement.md) object that created the job.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_OwningJobElement : CIM_OwningJobElement
{
  CIM_ManagedElement REF OwningElement;
  CIM_Job            REF OwnedElement;
};
```

## Members

The **Msvm\_OwningJobElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_OwningJobElement** class has these properties.

<dl> <dt>

**OwnedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Job**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the job created by the managed element.

This property is inherited from [**CIM\_OwningJobElement**](cim-owningjobelement.md).

</dd> <dt>

**OwningElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the managed element that created the job.

This property is inherited from [**CIM\_OwningJobElement**](cim-owningjobelement.md).

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

[**CIM\_OwningJobElement**](cim-owningjobelement.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





