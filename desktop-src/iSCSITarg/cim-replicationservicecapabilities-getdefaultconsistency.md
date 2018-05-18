---
title: GetDefaultConsistency method of the CIM\_ReplicationServiceCapabilities class
description: This method for a given ReplicationType, returns the default consistency value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c538f79b-4233-4677-97e0-0a68c9189ea1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetDefaultConsistency method iSCSI Software Target API", "GetDefaultConsistency method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class", "CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetDefaultConsistency method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetDefaultConsistency
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetDefaultConsistency method of the CIM\_ReplicationServiceCapabilities class

This method for a given ReplicationType, returns the default consistency value.

## Syntax


```mof
uint32 GetDefaultConsistency(
  [in]  uint16 ReplicationType,
  [out] uint16 DefaultConsistency
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the ReplicationType.

</dd> <dt>

*DefaultConsistency* \[out\]
</dt> <dd>

Default consistency value.

<dt>

<span id="No_default_consistency"></span><span id="no_default_consistency"></span><span id="NO_DEFAULT_CONSISTENCY"></span>

**No default consistency** (0)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (1)


</dt> <dd></dd> <dt>

<span id="Sequentially_Consistent"></span><span id="sequentially_consistent"></span><span id="SEQUENTIALLY_CONSISTENT"></span>

**Sequentially Consistent** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>3–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> </dl>

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

**DMTF Reserved** (7–32767)
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

 

 





