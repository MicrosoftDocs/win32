---
title: CreateStorageHardwareID method of the CIM\_StorageHardwareIDManagementService class
description: This method creates a CIM\_StorageHardwareID, it creates the association CIM\_ConcreteDependency between this service and the new CIM\_StorageHardwareID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '05ac9ef3-27b8-436c-a89a-b41846b8a2ad'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateStorageHardwareID method iSCSI Software Target API", "CreateStorageHardwareID method iSCSI Software Target API , CIM_StorageHardwareIDManagementService class", "CIM_StorageHardwareIDManagementService class iSCSI Software Target API , CreateStorageHardwareID method"]
topic_type:
- apiref
api_name:
- CIM_StorageHardwareIDManagementService.CreateStorageHardwareID
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# CreateStorageHardwareID method of the CIM\_StorageHardwareIDManagementService class

This method creates a CIM\_StorageHardwareID, it creates the association CIM\_ConcreteDependency between this service and the new CIM\_StorageHardwareID.

## Syntax


```mof
uint32 CreateStorageHardwareID(
  [in]  string                           ElementName,
  [in]  string                           StorageID,
  [in]  uint16                           IDType,
  [in]  string                           OtherIDType,
  [in]  CIM_StorageClientSettingData REF Setting,
  [out] CIM_StorageHardwareID        REF HardwareID
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

The ElementName of the new StorageHardwareID instance.

</dd> <dt>

*StorageID* \[in\]
</dt> <dd>

StorageID is the value used by the SecurityService to represent Identity - in this case, a hardware worldwide unique name.

</dd> <dt>

*IDType* \[in\]
</dt> <dd>

The type of the StorageID property. iSCSI IDs may use one of three iSCSI formats - iqn, eui, or naa. This three letter format is the name prefix; so a single iSCSI type is provided here, the prefix can be used to further refine the format.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="PortWWN"></span><span id="portwwn"></span><span id="PORTWWN"></span>

**PortWWN** (2)


</dt> <dd></dd> <dt>

<span id="NodeWWN"></span><span id="nodewwn"></span><span id="NODEWWN"></span>

**NodeWWN** (3)


</dt> <dd></dd> <dt>

<span id="Hostname"></span><span id="hostname"></span><span id="HOSTNAME"></span>

**Hostname** (4)


</dt> <dd></dd> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>

**iSCSI Name** (5)


</dt> <dd></dd> </dl> </dd> <dt>

*OtherIDType* \[in\]
</dt> <dd>

The type of the storage ID, when IDType is "Other".

</dd> <dt>

*Setting* \[in\]
</dt> <dd>

REF to the StorageClientSettingData containing the OSType appropriate for this initiator. If left NULL, the instrumentation assumes a standard OSType - i.e., that no OS-specific behavior for this initiator is defined.

</dd> <dt>

*HardwareID* \[out\]
</dt> <dd>

REF to the new StorageHardwareID instance.

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

**ID already created** (4096)
</dt> <dt>

**Hardware implementation does not support specified IDType** (4097)
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

 

 





