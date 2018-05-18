---
title: QueryPolicyValue method of the Msps\_ProvisioningFileProcessor class
description: Requests a specific policy from a provided policy data set.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f23256e6-5b8f-4efd-9014-fc010bf3c674'
ms.prod: 'windows-server-dev'
ms.technology:
- 'shielded-vm-provisioning'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["QueryPolicyValue method", "QueryPolicyValue method, Msps_ProvisioningFileProcessor class", "Msps_ProvisioningFileProcessor class, QueryPolicyValue method"]
---

# QueryPolicyValue method of the Msps\_ProvisioningFileProcessor class

Requests a specific policy from a provided policy data set.

## Syntax


```mof
uint32 QueryPolicyValue(
  [in]  uint8  PolicyData[],
  [in]  string PolicyGUID,
  [out] uint8  PolicyValue[]
);
```



## Parameters

<dl> <dt>

*PolicyData* \[in\]
</dt> <dd>

The policy set to query.

</dd> <dt>

*PolicyGUID* \[in\]
</dt> <dd>

The ID of the policy requested.

</dd> <dt>

*PolicyValue* \[out\]
</dt> <dd>

The returned value of the policy.

</dd> </dl>

## Return value

TBD

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\MSPS<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>MSPSProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msps\_ProvisioningFileProcessor**](msps-provisioningfileprocessor.md)
</dt> </dl>

 

 





