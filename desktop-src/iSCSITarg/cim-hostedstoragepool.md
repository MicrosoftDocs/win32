---
title: CIM\_HostedStoragePool class
description: HostedStoragePool is a specialization of HostedResourcePool association that establishes that the StoragePool is defined in the context of the System.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd2c02b23-fae4-4ce1-be86-9c89f50e6720'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_HostedStoragePool class iSCSI Software Target API", "CIM_HostedStoragePool class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_HostedStoragePool
- CIM_HostedStoragePool.GroupComponent
- CIM_HostedStoragePool.PartComponent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_HostedStoragePool class

HostedStoragePool is a specialization of HostedResourcePool association that establishes that the StoragePool is defined in the context of the System.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Aggregation, Composition, Version("2.15.0"), UMLPackagePath("CIM::Device::StorageServices")]
class CIM_HostedStoragePool : CIM_HostedResourcePool
{
  CIM_System      REF GroupComponent;
  CIM_StoragePool REF PartComponent;
};
```

## Members

The **CIM\_HostedStoragePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedStoragePool** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The parent system in the Association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StoragePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The StoragePool that is a component of a System.

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

[**CIM\_HostedResourcePool**](cim-hostedresourcepool.md)
</dt> </dl>

 

 





