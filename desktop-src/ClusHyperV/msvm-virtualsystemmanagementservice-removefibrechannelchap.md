---
title: RemoveFibreChannelChap method of the Msvm\_VirtualSystemManagementService class
description: Removes DH-CHAP settings from a synthetic fibre channel port in a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7111ac3e-1c45-49eb-92d9-a1cd58f02217'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveFibreChannelChap method", "RemoveFibreChannelChap method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, RemoveFibreChannelChap method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.RemoveFibreChannelChap
api_location:
- VMMS.exe
api_type:
- COM
---

# RemoveFibreChannelChap method of the Msvm\_VirtualSystemManagementService class

Removes DH-CHAP settings from a synthetic fibre channel port in a virtual machine.

> [!Note]  
> This will fail if the virtual machine is running.

 

## Syntax


```mof
uint32 RemoveFibreChannelChap(
  [in] string FcPortSettings[]
);
```



## Parameters

<dl> <dt>

*FcPortSettings* \[in\]
</dt> <dd>

An array that contains embedded instances of [**Msvm\_SyntheticFcPortSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850228) that represent the settings to remove.

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

 

 





