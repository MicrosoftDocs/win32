---
title: MSISCSITARGET\_HostedStoragePool class
description: Defines an association indicating that the storage pool is defined in the context of the referenced System.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '13438703-4fed-498e-944a-777f320ad598'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_HostedStoragePool class iSCSI Software Target API", "MSISCSITARGET_HostedStoragePool class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_HostedStoragePool
- MSISCSITARGET_HostedStoragePool.GroupComponent
- MSISCSITARGET_HostedStoragePool.PartComponent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_HostedStoragePool class

Defines an association indicating that the storage pool is defined in the context of the referenced System.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Aggregation, Composition, Version("1.0.0")]
class MSISCSITARGET_HostedStoragePool : CIM_HostedStoragePool
{
  CIM_System      REF GroupComponent;
  CIM_StoragePool REF PartComponent;
};
```

## Members

The **MSISCSITARGET\_HostedStoragePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_HostedStoragePool** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The parent system in the Association.

This property is inherited from [**CIM\_HostedStoragePool**](cim-hostedstoragepool.md).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StoragePool**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The StoragePool that is a component of a System.

This property is inherited from [**CIM\_HostedStoragePool**](cim-hostedstoragepool.md).

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

[**CIM\_HostedStoragePool**](cim-hostedstoragepool.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





