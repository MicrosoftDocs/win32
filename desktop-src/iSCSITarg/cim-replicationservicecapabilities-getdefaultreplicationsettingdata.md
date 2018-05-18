---
title: GetDefaultReplicationSettingData method of the CIM\_ReplicationServiceCapabilities class
description: This method for a given ReplicationType returns the default ReplicationSettingData as an instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fb30750d-b5de-4370-9d9a-4a033db04d32'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetDefaultReplicationSettingData method iSCSI Software Target API", "GetDefaultReplicationSettingData method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class", "CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetDefaultReplicationSettingData method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetDefaultReplicationSettingData
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetDefaultReplicationSettingData method of the CIM\_ReplicationServiceCapabilities class

This method for a given ReplicationType returns the default ReplicationSettingData as an instance.

## Syntax


```mof
uint32 GetDefaultReplicationSettingData(
  [in]  uint16 ReplicationType,
  [out] string DefaultInstance
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*DefaultInstance* \[out\]
</dt> <dd>

A copy of the instance this populated with default values for the given ReplicationType.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**No default ReplicationSettingData** (7)
</dt> <dt>

**DMTF Reserved** (8–32767)
</dt> <dt>

**Vendor Specific** (32768–4294967295)
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

[**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
</dt> </dl>

 

 





