---
title: AddFibreChannelChap method of the Msvm\_VirtualSystemManagementService class
description: Adds DH-CHAP parameters to a synthetic fibre channel port in a VM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fc56ded1-851f-47a2-9da9-b603e5a22141
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddFibreChannelChap method
- AddFibreChannelChap method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, AddFibreChannelChap method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.AddFibreChannelChap
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddFibreChannelChap method of the Msvm\_VirtualSystemManagementService class

Adds DH-CHAP parameters to a synthetic fibre channel port in a VM.

> [!Note]  
> This will fail if the VM is running.

 

## Syntax


```mof
uint32 AddFibreChannelChap(
  [in] string FcPortSettings[],
  [in] uint8  SecretEncoding,
  [in] uint8  SharedSecret[]
);
```



## Parameters

<dl> <dt>

*FcPortSettings* \[in\]
</dt> <dd>

An array that contains embedded instances [**Msvm\_SyntheticFcPortSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850228) that describe settings for the synthetic fibre channel ports. All **Msvm\_SyntheticFcPortSettingData** instances must have a valid **InstanceID** property value in order to identify the feature settings to modify.

</dd> <dt>

*SecretEncoding* \[in\]
</dt> <dd>

The type of encoding for the shared secret that is used to authenticate the port.

<dt>

<span id="Printable_ASCII"></span><span id="printable_ascii"></span><span id="PRINTABLE_ASCII"></span>

**Printable ASCII** (1)


</dt> <dd></dd> <dt>

<span id="Binary"></span><span id="binary"></span><span id="BINARY"></span>

**Binary** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

An array that contains the shared secret used to authenticate the port.

</dd> </dl>

## Return value

The possible values are:

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

 

 





