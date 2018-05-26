---
title: DeleteStorageHardwareID method of the MSISCSITARGET\_StorageHardwareIDManagementService class
description: Deletes a specified MSISCSITARGET\_StorageHardwareID instance, and deletes the associations that are no longer needed, which include the MSISCSITARGET\_ConcreteDependency and MSISCSITARGET\_AuthorizedSubject classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b4890be8-d845-4745-b115-56c4e4357e29
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteStorageHardwareID method iSCSI Software Target API
- DeleteStorageHardwareID method iSCSI Software Target API , MSISCSITARGET_StorageHardwareIDManagementService class
- MSISCSITARGET_StorageHardwareIDManagementService class iSCSI Software Target API , DeleteStorageHardwareID method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageHardwareIDManagementService.DeleteStorageHardwareID
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteStorageHardwareID method of the MSISCSITARGET\_StorageHardwareIDManagementService class

Deletes a specified [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instance, and deletes the associations that are no longer needed, which include the [**MSISCSITARGET\_ConcreteDependency**](msiscsitarget-concretedependency.md) and [**MSISCSITARGET\_AuthorizedSubject**](msiscsitarget-authorizedsubject.md) classes.

This method overrides the method inherited from the **CIM\_StorageHardwareIDManagementService** class.

## Syntax


```mof
uint32 DeleteStorageHardwareID(
  [in] CIM_StorageHardwareID REF HardwareID
);
```



## Parameters

<dl> <dt>

*HardwareID* \[in\]
</dt> <dd>

Specifies the storage hardware ID to delete.

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

**DMTF Reserved** (6 4095)
</dt> <dt>

**Specified instance not found** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageHardwareIDManagementService**](msiscsitarget-storagehardwareidmanagementservice.md)
</dt> </dl>

 

 





