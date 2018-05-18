---
title: CreateStorageHardwareID method of the MSISCSITARGET\_StorageHardwareIDManagementService class
description: Creates a MSISCSITARGET\_StorageHardwareID instance, and creates the MSISCSITARGET\_ConcreteDependency association between this instance and the MSISCSITARGET\_StorageHardwareIDManagementService service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '365c7c3f-c86c-4c52-a84a-17651c6b220f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateStorageHardwareID method iSCSI Software Target API", "CreateStorageHardwareID method iSCSI Software Target API , MSISCSITARGET_StorageHardwareIDManagementService class", "MSISCSITARGET_StorageHardwareIDManagementService class iSCSI Software Target API , CreateStorageHardwareID method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageHardwareIDManagementService.CreateStorageHardwareID
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# CreateStorageHardwareID method of the MSISCSITARGET\_StorageHardwareIDManagementService class

Creates a [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instance, and creates the [**MSISCSITARGET\_ConcreteDependency**](msiscsitarget-concretedependency.md) association between this instance and the [**MSISCSITARGET\_StorageHardwareIDManagementService**](msiscsitarget-storagehardwareidmanagementservice.md) service.

This method overrides the method inherited from the **CIM\_StorageHardwareIDManagementService** class.

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

Specifies the **ElementName** property of the [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instance.

</dd> <dt>

*StorageID* \[in\]
</dt> <dd>

Specifies the hardware worldwide unique ID of the [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instance.

</dd> <dt>

*IDType* \[in\]
</dt> <dd>

Specifies the type of the *StorageID* parameter.

> [!Note]  
> An **iSCSI Name** can be in any one of three iSCSI formats, IQN, EUI, or NAA.

 

Possible values are.

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


</dt> <dd></dd> <dt>

<span id="SwitchWWN"></span><span id="switchwwn"></span><span id="SWITCHWWN"></span>

**SwitchWWN** (6)


</dt> <dd></dd> </dl> </dd> <dt>

*OtherIDType* \[in\]
</dt> <dd>

Specifies the type of the *StorageID* parameter when the *IDType* parameter is **Other**.

</dd> <dt>

*Setting* \[in\]
</dt> <dd>

Specifies a [**MSISCSITARGET\_StorageClientSettingData**](msiscsitarget-storageclientsettingdata.md) instance that contains the host environment properties that are associated with the [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instance.

If **NULL**, the instrumentation applies a [**MSISCSITARGET\_StorageClientSettingData**](msiscsitarget-storageclientsettingdata.md).**ClientTypes** property value of **Standard**.

</dd> <dt>

*HardwareID* \[out\]
</dt> <dd>

On return, contains a reference to the [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md) instance.

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

[**MSISCSITARGET\_StorageHardwareIDManagementService**](msiscsitarget-storagehardwareidmanagementservice.md)
</dt> </dl>

 

 





