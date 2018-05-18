---
title: CreateReferencePoint method of the Msvm\_CollectionReferencePointService class
description: Creates a reference point of a virtual system collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a428851b-ba58-4ead-8e8e-f52370c80934'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateReferencePoint method", "CreateReferencePoint method, Msvm_CollectionReferencePointService class", "Msvm_CollectionReferencePointService class, CreateReferencePoint method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionReferencePointService.CreateReferencePoint
api_location:
- VMMS.exe
api_type:
- COM
---

# CreateReferencePoint method of the Msvm\_CollectionReferencePointService class

Creates a reference point of a virtual system collection.

## Syntax


```mof
uint32 CreateReferencePoint(
  [in]      Msvm_VirtualSystemCollection REF Collection,
  [in]      string                           ReferencePointSettings,
  [in]      uint16                           ReferencePointType,
  [in, out] CIM_Collection               REF ResultingReferencePointCollection,
  [out]     CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) reference to the virtual system collection.

</dd> <dt>

*ReferencePointSettings* \[in\]
</dt> <dd>

The parameter settings for the reference point.

</dd> <dt>

*ReferencePointType* \[in\]
</dt> <dd>

The type of the reference point to create.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Log_based"></span><span id="log_based"></span><span id="LOG_BASED"></span>

<span id="Log_based"></span><span id="log_based"></span><span id="LOG_BASED"></span>**Log based** (1)


</dt> <dd></dd> <dt>

<span id="RCT_based"></span><span id="rct_based"></span><span id="RCT_BASED"></span>

<span id="RCT_based"></span><span id="rct_based"></span><span id="RCT_BASED"></span>**RCT based** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Vendor Reserved

</dd> </dl> </dd> <dt>

*ResultingReferencePointCollection* \[in, out\]
</dt> <dd>

The new reference point.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**Invalid Type** (6)
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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md)
</dt> </dl>

 

 





