---
title: AddHardwareIDsToCollection method of the MSISCSITARGET\_StorageHardwareIDManagementService class
description: Creates CIM\_MemberOfCollection instances to associate specified hardware IDs to a specified collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2832f193-79ec-45e6-97d8-9539f0eb1c79
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddHardwareIDsToCollection method iSCSI Software Target API
- AddHardwareIDsToCollection method iSCSI Software Target API , MSISCSITARGET_StorageHardwareIDManagementService class
- MSISCSITARGET_StorageHardwareIDManagementService class iSCSI Software Target API , AddHardwareIDsToCollection method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageHardwareIDManagementService.AddHardwareIDsToCollection
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddHardwareIDsToCollection method of the MSISCSITARGET\_StorageHardwareIDManagementService class

Creates **CIM\_MemberOfCollection** instances to associate specified hardware IDs to a specified collection.

## Syntax


```mof
uint32 AddHardwareIDsToCollection(
  [in] string                           HardwareIDs[],
  [in] CIM_SystemSpecificCollection Ref Collection
);
```



## Parameters

<dl> <dt>

*HardwareIDs* \[in\]
</dt> <dd>

Specifies string representations of the [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instances to add to the collection.

</dd> <dt>

*Collection* \[in\]
</dt> <dd>

Specifies the collection to which to add the specified hardware IDs.

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

**DMTF Reserved** (6 0x0FFF)
</dt> <dt>

**Invalid LogicalDevice instance** (0x1000)
</dt> <dt>

**Implementation does not support device collections** (0x1001)
</dt> <dt>

**Input devices cannot be used in this collection** (0x1002)
</dt> <dt>

**Method Reserved** (0x1003 0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 0xFFFF)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageHardwareIDManagementService**](msiscsitarget-storagehardwareidmanagementservice.md)
</dt> </dl>

 

 





