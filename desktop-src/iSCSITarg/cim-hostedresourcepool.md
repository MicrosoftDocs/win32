---
title: CIM\_HostedResourcePool class
description: HostedResourcePool is a specialization of the SystemComponent association that establishes that the ResourcePool is defined in the context of the System.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5725df05-b71a-418b-b232-792b1735a2f9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_HostedResourcePool class iSCSI Software Target API", "CIM_HostedResourcePool class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_HostedResourcePool
- CIM_HostedResourcePool.GroupComponent
- CIM_HostedResourcePool.PartComponent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_HostedResourcePool class

HostedResourcePool is a specialization of the SystemComponent association that establishes that the ResourcePool is defined in the context of the System

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Experimental, Aggregation, Composition, Version("2.15.0"), UMLPackagePath("CIM::Core::Resource")]
class CIM_HostedResourcePool : CIM_SystemComponent
{
  CIM_System       REF GroupComponent;
  CIM_ResourcePool REF PartComponent;
};
```

## Members

The **CIM\_HostedResourcePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedResourcePool** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The parent system in the association

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourcePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The ResourcePool that is a component of the system

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> </dl>

 

 





