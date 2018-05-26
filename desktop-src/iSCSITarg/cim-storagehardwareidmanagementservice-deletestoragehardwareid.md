---
title: DeleteStorageHardwareID method of the CIM\_StorageHardwareIDManagementService class
description: This method deletes a named CIM\_StorageHardwareID, and also tears down the associations that are no longer needed, including CIM\_ConcreteDependency and CIM\_AuthorizedSubject.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d74b5d6a-d8c0-40e8-a085-ea03b8cb6a5b
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteStorageHardwareID method iSCSI Software Target API
- DeleteStorageHardwareID method iSCSI Software Target API , CIM_StorageHardwareIDManagementService class
- CIM_StorageHardwareIDManagementService class iSCSI Software Target API , DeleteStorageHardwareID method
topic_type:
- apiref
api_name:
- CIM_StorageHardwareIDManagementService.DeleteStorageHardwareID
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteStorageHardwareID method of the CIM\_StorageHardwareIDManagementService class

This method deletes a named CIM\_StorageHardwareID, and also tears down the associations that are no longer needed, including CIM\_ConcreteDependency and CIM\_AuthorizedSubject.

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

The storage hardware ID to be deleted.

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

[**CIM\_StorageHardwareIDManagementService**](cim-storagehardwareidmanagementservice.md)
</dt> </dl>

 

 





