---
title: PrepareSpecializedMachine method of the Msps\_ProvisioningService class
description: Used to prepare an existing VM for provisioning.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6cb48543-974f-438c-9980-f5e045455578
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PrepareSpecializedMachine method
- PrepareSpecializedMachine method, Msps_ProvisioningService class
- Msps_ProvisioningService class, PrepareSpecializedMachine method
topic_type:
- apiref
api_name:
- Msps_ProvisioningService.PrepareSpecializedMachine
api_location:
- MSPSService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrepareSpecializedMachine method of the Msps\_ProvisioningService class

Used to prepare an existing VM for provisioning. The method should be executed against a target machine. If this is a VM, it must have been created but turned off. A [**Msps\_ProvisioningJob**](msps-provisioningjob.md) instance will be returned which can be used to monitor the process.

## Syntax


```mof
uint32 PrepareSpecializedMachine(
  [in]  string               TemplateUtilityDiskPath,
  [in]  string               MachineID,
  [out] Msps_ProvisioningJob PreparationJob
);
```



## Parameters

<dl> <dt>

*TemplateUtilityDiskPath* \[in\]
</dt> <dd>

Template utility disk path.

</dd> <dt>

*MachineID* \[in\]
</dt> <dd>

**GUID** for the virtual machine.

</dd> <dt>

*PreparationJob* \[out\]
</dt> <dd>

Returns an embedded instance of [**Msps\_ProvisioningJob**](msps-provisioningjob.md).

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                             |
| Namespace<br/>                | Root\\MSPS<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>MSPSService.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSService.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msps\_ProvisioningService**](msps-provisioningservice.md)
</dt> <dt>

[**Msps\_ProvisioningJob**](msps-provisioningjob.md)
</dt> </dl>

 

 





