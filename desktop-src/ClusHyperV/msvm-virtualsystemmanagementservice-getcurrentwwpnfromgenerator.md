---
title: GetCurrentWwpnFromGenerator method of the Msvm\_VirtualSystemManagementService class
description: Retrieves the current World Wide Port Name (WWPN) from the GenerateWwpn method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '27789fa2-b1a1-4498-b77c-2341ecb2db19'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetCurrentWwpnFromGenerator method", "GetCurrentWwpnFromGenerator method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, GetCurrentWwpnFromGenerator method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.GetCurrentWwpnFromGenerator
api_location:
- VMMS.exe
api_type:
- COM
---

# GetCurrentWwpnFromGenerator method of the Msvm\_VirtualSystemManagementService class

Retrieves the current World Wide Port Name (WWPN) from the [**GenerateWwpn**](msvm-virtualsystemmanagementservice-generatewwpn.md) method.

## Syntax


```mof
uint32 GetCurrentWwpnFromGenerator(
  [out] string CurrentWwpn
);
```



## Parameters

<dl> <dt>

*CurrentWwpn* \[out\]
</dt> <dd>

The current WWPN. When the are no more WWPNs to create, [**GenerateWwpn**](msvm-virtualsystemmanagementservice-generatewwpn.md) returns "0000000000000000".

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





