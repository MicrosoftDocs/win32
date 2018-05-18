---
title: CreateHardwareIDCollection method of the MSISCSITARGET\_StorageHardwareIDManagementService class
description: Creates a new instance of CIM\_SystemSpecificCollection and associates a group of MSISCSITARGET\_StorageHardwareID instances to it by using CIM\_MemberOfCollection associations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5c88c86a-4953-483f-842b-cf223e67651e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateHardwareIDCollection method iSCSI Software Target API", "CreateHardwareIDCollection method iSCSI Software Target API , MSISCSITARGET_StorageHardwareIDManagementService class", "MSISCSITARGET_StorageHardwareIDManagementService class iSCSI Software Target API , CreateHardwareIDCollection method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageHardwareIDManagementService.CreateHardwareIDCollection
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# CreateHardwareIDCollection method of the MSISCSITARGET\_StorageHardwareIDManagementService class

Creates a new instance of **CIM\_SystemSpecificCollection** and associates a group of [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instances to it by using **CIM\_MemberOfCollection** associations. A **CIM\_HostedCollection** instance is created to associate the new collection with the parent system.

This method is inherited from the **CIM\_StorageHardwareIDManagementService** class.

## Syntax


```mof
uint32 CreateHardwareIDCollection(
  [in]  string                           ElementName,
  [in]  string                           HardwareIDs[],
  [out] CIM_SystemSpecificCollection Ref Collection
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

Specifies the **ElementName** property of the new collection.

</dd> <dt>

*HardwareIDs* \[in\]
</dt> <dd>

Specifies string representations of the [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instances to include in the new collection.

</dd> <dt>

*Collection* \[out\]
</dt> <dd>

On return, contains the new **CIM\_SystemSpecificCollection** instance.

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

**DMTF Reserved** (6–0x0FFF)
</dt> <dt>

**Invalid HardwareID instance** (0x1000)
</dt> <dt>

**Implementation does not support hardware ID collections** (0x1001)
</dt> <dt>

**Input hardware IDs cannot be used in same collection** (0x1002)
</dt> <dt>

**Method Reserved** (0x1003–0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000–0xFFFF)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageHardwareIDManagementService**](msiscsitarget-storagehardwareidmanagementservice.md)
</dt> </dl>

 

 





