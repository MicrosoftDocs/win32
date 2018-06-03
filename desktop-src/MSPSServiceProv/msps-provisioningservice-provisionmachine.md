---
title: ProvisionMachine method of the Msps\_ProvisioningService class
description: This method is used to securely provisioning a machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7c262ee0-2c4c-46f0-96ae-a0c9f510d850
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ProvisionMachine method
- ProvisionMachine method, Msps_ProvisioningService class
- Msps_ProvisioningService class, ProvisionMachine method
topic_type:
- apiref
api_name:
- Msps_ProvisioningService.ProvisionMachine
api_location:
- MSPSService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProvisionMachine method of the Msps\_ProvisioningService class

This method is used to securely provisioning a machine. The method should be executed against a target machine identified. If this is a VM, it must have been created but has not yet been started. A [**Msps\_ProvisioningJob**](msps-provisioningjob.md) instance will be returned which can be used to monitor the provisioning process.

## Syntax


```mof
uint32 ProvisionMachine(
  [in]  string               PDKPath,
  [in]  string               FSKPath,
  [in]  string               MachineID,
  [out] Msps_ProvisioningJob ProvisioningJob
);
```



## Parameters

<dl> <dt>

*PDKPath* \[in\]
</dt> <dd>

Path to the Provisioning Data Keyfile (PDK) used in the provisioning process.

</dd> <dt>

*FSKPath* \[in\]
</dt> <dd>

Path to the Fabric Specialization Keyfile (FSK) used to provision the machine.

</dd> <dt>

*MachineID* \[in\]
</dt> <dd>

The virtual machine ID associated with the targeted VM machine to provision. The ID is often in the form of a GUID.

</dd> <dt>

*ProvisioningJob* \[out\]
</dt> <dd>

On success, contains an embedded instance of a [**Msps\_ProvisioningJob**](msps-provisioningjob.md) that contains the provisioning job associated with this provision attempt. This job can be queried for fabric policy, status and the result of provisioning the VM.

</dd> </dl>

## Remarks

If the specified machine is a virtual machine, you must first create the machine, but not start it, before provisioning.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                             |
| Namespace<br/>                | Root\\MSPS<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>MSPSService.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSService.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msps\_ProvisioningService**](msps-provisioningservice.md)
</dt> </dl>

 

 





