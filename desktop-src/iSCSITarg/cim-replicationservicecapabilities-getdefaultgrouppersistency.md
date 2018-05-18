---
title: GetDefaultGroupPersistency method of the CIM\_ReplicationServiceCapabilities class
description: This method returns the default persistency for a newly created group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c29ccd65-c87c-4947-b202-5db104297e26'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetDefaultGroupPersistency method iSCSI Software Target API", "GetDefaultGroupPersistency method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class", "CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetDefaultGroupPersistency method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetDefaultGroupPersistency
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetDefaultGroupPersistency method of the CIM\_ReplicationServiceCapabilities class

This method returns the default persistency for a newly created group.

## Syntax


```mof
uint32 GetDefaultGroupPersistency(
  [out] uint16 DefaultGroupPersistency
);
```



## Parameters

<dl> <dt>

*DefaultGroupPersistency* \[out\]
</dt> <dd>

Default group persistency value.

<dt>

<span id="No_default_persistency"></span><span id="no_default_persistency"></span><span id="NO_DEFAULT_PERSISTENCY"></span>

**No default persistency** (0)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (1)


</dt> <dd></dd> <dt>

<span id="Persistent"></span><span id="persistent"></span><span id="PERSISTENT"></span>

**Persistent** (2)


</dt> <dd></dd> <dt>

<span id="Not_Persistent"></span><span id="not_persistent"></span><span id="NOT_PERSISTENT"></span>

**Not Persistent** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–32767</dd> <dt>

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

 

 





