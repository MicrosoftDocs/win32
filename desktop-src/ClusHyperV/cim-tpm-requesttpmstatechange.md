---
title: RequestTPMStateChange method of the CIM\_TPM class
description: Requests that the state of the TPM be changed to the value specified in the RequestedTPMState parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '96701f8b-9595-43b5-9b6e-bd864fd43662'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RequestTPMStateChange method", "RequestTPMStateChange method, CIM_TPM class", "CIM_TPM class, RequestTPMStateChange method"]
topic_type:
- apiref
api_name:
- CIM_TPM.RequestTPMStateChange
api_location:
- VMMS.exe
api_type:
- COM
---

# RequestTPMStateChange method of the CIM\_TPM class

Requests that the state of the TPM be changed to the value specified in the **RequestedTPMState** parameter.

## Syntax


```mof
uint32 RequestTPMStateChange(
  [in]  uint16              RequestedTPMState,
  [in]  string              AuthorizationToken,
  [out] CIM_ConcreteJob REF Job,
  [in]  datetime            TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedTPMState* \[in\]
</dt> <dd>

The requested TPM states.

<dt>

<span id="S1_Enabled-Active-Owned"></span><span id="s1_enabled-active-owned"></span><span id="S1_ENABLED-ACTIVE-OWNED"></span>

**S1 Enabled-Active-Owned** (2)


</dt> <dd></dd> <dt>

<span id="S2_Disabled-Active-Owned"></span><span id="s2_disabled-active-owned"></span><span id="S2_DISABLED-ACTIVE-OWNED"></span>

**S2 Disabled-Active-Owned** (3)


</dt> <dd></dd> <dt>

<span id="S3_Enabled-Inactive-Owned"></span><span id="s3_enabled-inactive-owned"></span><span id="S3_ENABLED-INACTIVE-OWNED"></span>

**S3 Enabled-Inactive-Owned** (4)


</dt> <dd></dd> <dt>

<span id="S4_Disabled-Inactive-Owned"></span><span id="s4_disabled-inactive-owned"></span><span id="S4_DISABLED-INACTIVE-OWNED"></span>

**S4 Disabled-Inactive-Owned** (5)


</dt> <dd></dd> <dt>

<span id="S5_Enabled-Active-Unowned"></span><span id="s5_enabled-active-unowned"></span><span id="S5_ENABLED-ACTIVE-UNOWNED"></span>

**S5 Enabled-Active-Unowned** (6)


</dt> <dd></dd> <dt>

<span id="S6_Disabled-Active-Unowned"></span><span id="s6_disabled-active-unowned"></span><span id="S6_DISABLED-ACTIVE-UNOWNED"></span>

**S6 Disabled-Active-Unowned** (7)


</dt> <dd></dd> <dt>

<span id="S7_Enabled-Inactive-Unowned"></span><span id="s7_enabled-inactive-unowned"></span><span id="S7_ENABLED-INACTIVE-UNOWNED"></span>

**S7 Enabled-Inactive-Unowned** (8)


</dt> <dd></dd> <dt>

<span id="S8_Disabled-Inactive-Unowned"></span><span id="s8_disabled-inactive-unowned"></span><span id="S8_DISABLED-INACTIVE-UNOWNED"></span>

**S8 Disabled-Inactive-Unowned** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*AuthorizationToken* \[in\]
</dt> <dd>

The authorization token if it is required for the state change.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional concrete job that tracks the state transition initiated by the method invocation.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

The timeout interval that specifies the maximum amount of time that the client expects the transition to the new state to take. A value of 0 or a null parameter indicates that the client has no time requirements for the transition.

</dd> </dl>

## Return value

The possible values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown or Unspecified Error** (2)
</dt> <dt>

**Cannot complete within Timeout Period** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Invalid State Transition** (4097)
</dt> <dt>

**Use of Timeout Parameter Not Supported** (4098)
</dt> <dt>

**Busy** (4099)
</dt> <dt>

**Method Reserved** (4100–32767)
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

[**CIM\_TPM**](cim-tpm.md)
</dt> </dl>

 

 





