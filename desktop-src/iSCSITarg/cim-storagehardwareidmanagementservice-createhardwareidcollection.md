---
title: CreateHardwareIDCollection method of the CIM\_StorageHardwareIDManagementService class
description: Create a group of StorageHardwareIDs as a new instance of SystemSpecificCollection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd7aadb1a-3159-4a2f-98e5-3781310544c4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateHardwareIDCollection method iSCSI Software Target API", "CreateHardwareIDCollection method iSCSI Software Target API , CIM_StorageHardwareIDManagementService class", "CIM_StorageHardwareIDManagementService class iSCSI Software Target API , CreateHardwareIDCollection method"]
topic_type:
- apiref
api_name:
- CIM_StorageHardwareIDManagementService.CreateHardwareIDCollection
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# CreateHardwareIDCollection method of the CIM\_StorageHardwareIDManagementService class

Create a group of StorageHardwareIDs as a new instance of SystemSpecificCollection. This is useful to define a set of authorized subjects that can access volumes in a disk array. This method allows the client to make a request of a specific Service instance to create the collection and provide the appropriate class name. When these capabilities are standardized in CIM/WBEM, this method can be deprecated and intrinsic methods used. In addition to creating the collection, this method causes the creation of the HostedCollection association (to this service's scoping system) and MemberOfCollection association to members of the IDs parameter.

## Syntax


```mof
uint32 CreateHardwareIDCollection(
  [in]  string                           ElementName,
  [in]  string                           HardwareIDs[],
  [out] CIM_SystemSpecificCollection REF Collection
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

The ElementName to be assigned to the created collection.

</dd> <dt>

*HardwareIDs* \[in\]
</dt> <dd>

Array of strings containing representations of references to StorageHardwareID instances that will become members of the new collection.

</dd> <dt>

*Collection* \[out\]
</dt> <dd>

The new instance of SystemSpecificCollection that is created.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**DMTF Reserved** (6–4095)
</dt> <dt>

**Invalid HardwareID instance** (4096)
</dt> <dt>

**Implementation does not support hardware ID collections** (4097)
</dt> <dt>

**Input hardware IDs cannot be used in same collection** (4098)
</dt> <dt>

**Method Reserved** (4099–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

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

[**CIM\_StorageHardwareIDManagementService**](cim-storagehardwareidmanagementservice.md)
</dt> </dl>

 

 





