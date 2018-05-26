---
title: CIM\_SystemDevice class
description: LogicalDevices may be aggregated by a System. This relationship is made explicit by the SystemDevice association.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa420ea9-14e8-4260-9220-99203110f0f1
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_SystemDevice class
- CIM_SystemDevice class, described
topic_type:
- apiref
api_name:
- CIM_SystemDevice
- CIM_SystemDevice.GroupComponent
- CIM_SystemDevice.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_SystemDevice class

LogicalDevices may be aggregated by a System. This relationship is made explicit by the SystemDevice association.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Aggregation, UUID("{D6CB4144-71F3-46b3-AE99-C0AD9A930CD1}"), AMENDMENT]
class CIM_SystemDevice : CIM_SystemComponent
{
  CIM_System        REF GroupComponent;
  CIM_LogicalDevice REF PartComponent;
};
```

## Members

The **CIM\_SystemDevice** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SystemDevice** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The parent system in the Association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The LogicalDevice that is a component of a System.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> </dl>

 

 





