---
title: GenerateWwpn method of the Msvm\_VirtualSystemManagementService class
description: Creates a range of World Wide Port Names (WWPN) from a Msvm\_VirtualSystemManagementServiceSettingData instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a7e0a774-ef1f-4330-a3b2-65203bc0d2bf
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GenerateWwpn method
- GenerateWwpn method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, GenerateWwpn method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.GenerateWwpn
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GenerateWwpn method of the Msvm\_VirtualSystemManagementService class

Creates a range of World Wide Port Names (WWPN) from a [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md) instance.

The range is defined by the **MinimumWwpnAddress** and **MaximumWwpnAddress** properties of the [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md) instance.

## Syntax


```mof
uint32 GenerateWwpn(
  [in]  uint32 NumberOfWwpns,
  [out] string GeneratedWwpn[]
);
```



## Parameters

<dl> <dt>

*NumberOfWwpns* \[in\]
</dt> <dd>

The number of WWPNs to create. Valid values can range between "1" and "1024".

If the valid number of WWPNs that can be generated is less than the requested number, then the remaining entries in the **GeneratedWwpn** array will contain the invalid entry of "0000000000000000", and this method will succeed.

</dd> <dt>

*GeneratedWwpn* \[out\]
</dt> <dd>

An array that contains the new WWPNs.

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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





