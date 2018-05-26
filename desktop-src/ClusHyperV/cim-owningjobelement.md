---
title: CIM\_OwningJobElement class
description: Represents an association between a job and the managed element that created the job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 67808117-ad45-482e-a20b-c3cdbf4600ea
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_OwningJobElement class
- CIM_OwningJobElement class, described
topic_type:
- apiref
api_name:
- CIM_OwningJobElement
- CIM_OwningJobElement.OwningElement
- CIM_OwningJobElement.OwnedElement
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_OwningJobElement class

Represents an association between a job and the managed element that created the job. Since a job might move between systems, and the managed element might not exist for the entire duration of the job, in some cases, this association might not be possible or might only exist for a portion of the existence of the job.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.7.0"), UMLPackagePath("CIM::System::Processing"), ModelCorrespondence("CIM_Job.Owner"), AMENDMENT]
class CIM_OwningJobElement
{
  CIM_ManagedElement REF OwningElement;
  CIM_Job            REF OwnedElement;
};
```

## Members

The **CIM\_OwningJobElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_OwningJobElement** class has these properties.

<dl> <dt>

**OwnedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Job**](cim-job.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the job created by the managed element.

</dd> <dt>

**OwningElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the managed element that created the job.

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

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





