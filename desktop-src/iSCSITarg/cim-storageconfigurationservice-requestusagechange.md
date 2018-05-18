---
title: RequestUsageChange method of the CIM\_StorageConfigurationService class
description: Allows a client to request the Usage to be set if the client has access to the element supplied and the request is valid.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6e4834e6-bf53-4c75-9b44-9ddb51774331'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RequestUsageChange method iSCSI Software Target API", "RequestUsageChange method iSCSI Software Target API , CIM_StorageConfigurationService class", "CIM_StorageConfigurationService class iSCSI Software Target API , RequestUsageChange method"]
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.RequestUsageChange
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# RequestUsageChange method of the CIM\_StorageConfigurationService class

Allows a client to request the Usage to be set if the client has access to the element supplied and the request is valid.

## Syntax


```mof
uint32 RequestUsageChange(
  [in]  uint16                 Operation,
  [in]  uint16                 UsageValue,
  [in]  string                 OtherUsageDescription,
  [out] CIM_ConcreteJob    REF Job,
  [in]  CIM_LogicalElement REF TheElement
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

The action to perform.

<dt>

<span id="Set"></span><span id="set"></span><span id="SET"></span>

**Set** (2)


</dt> <dd></dd> <dt>

<span id="Modify___Other___description_only"></span><span id="modify___other___description_only"></span><span id="MODIFY___OTHER___DESCRIPTION_ONLY"></span>

**Modify \\"Other\\" description only** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*UsageValue* \[in\]
</dt> <dd>

Applicable requested usage/restriction -- see the appropriate Usage ValueMap.

</dd> <dt>

*OtherUsageDescription* \[in\]
</dt> <dd>

New description text. Applicable when the usage value includes "Other".

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if job completed).

</dd> <dt>

*TheElement* \[in\]
</dt> <dd>

The storage element to modify.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
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

**Not Authorized** (6)
</dt> <dt>

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
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

[**CIM\_StorageConfigurationService**](cim-storageconfigurationservice.md)
</dt> </dl>

 

 





