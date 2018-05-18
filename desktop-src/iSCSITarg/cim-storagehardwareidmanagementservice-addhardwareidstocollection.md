---
title: AddHardwareIDsToCollection method of the CIM\_StorageHardwareIDManagementService class
description: Create MemberOfCollection instances between the specified Collection and the StorageHardwareIDs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dc5a372d-3e6a-406c-b384-84e65456df79'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddHardwareIDsToCollection method iSCSI Software Target API", "AddHardwareIDsToCollection method iSCSI Software Target API , CIM_StorageHardwareIDManagementService class", "CIM_StorageHardwareIDManagementService class iSCSI Software Target API , AddHardwareIDsToCollection method"]
topic_type:
- apiref
api_name:
- CIM_StorageHardwareIDManagementService.AddHardwareIDsToCollection
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# AddHardwareIDsToCollection method of the CIM\_StorageHardwareIDManagementService class

Create MemberOfCollection instances between the specified Collection and the StorageHardwareIDs. This method allows the client to make a request of a specific Service instance to create the associations. When these capabilities are standardized in CIM/WBEM, this method can be deprecated and intrinsic methods used.

## Syntax


```mof
uint32 AddHardwareIDsToCollection(
  [in] string                           HardwareIDs[],
  [in] CIM_SystemSpecificCollection REF Collection
);
```



## Parameters

<dl> <dt>

*HardwareIDs* \[in\]
</dt> <dd>

Array of strings containing representations of references to StorageHardwareID instances that will become members of the collection.

</dd> <dt>

*Collection* \[in\]
</dt> <dd>

The Collection which groups the StorageHardwareIDs.

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

**Invalid LogicalDevice instance** (4096)
</dt> <dt>

**Implementation does not support device collections** (4097)
</dt> <dt>

**Input devices cannot be used in this collection** (4098)
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

 

 





