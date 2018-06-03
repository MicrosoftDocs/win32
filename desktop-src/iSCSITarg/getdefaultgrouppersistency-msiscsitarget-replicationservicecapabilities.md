---
title: GetDefaultGroupPersistency method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves the default persistency for a newly created group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09541c3c-efbc-42a8-986d-787f8b657395
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetDefaultGroupPersistency method iSCSI Software Target API
- GetDefaultGroupPersistency method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class
- MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetDefaultGroupPersistency method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetDefaultGroupPersistency
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetDefaultGroupPersistency method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves the default persistency for a newly created group.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetDefaultGroupPersistency(
  [out] uint16 DefaultGroupPersistency
);
```



## Parameters

<dl> <dt>

*DefaultGroupPersistency* \[out\]
</dt> <dd>

On return, indicates the default group persistency.

The possible values are.

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


</dt> <dd>4 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> </dl>

## Return value

This method returns one of the following values.

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

**DMTF Reserved** (7 0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
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

[**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





