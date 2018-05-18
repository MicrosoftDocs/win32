---
title: Msps\_ProvisioningService class
description: Represents the Shielded VM Provisioning Service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e895dfa5-8802-47d5-bcd7-62b9813384d2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'shielded-vm-provisioning'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msps_ProvisioningService class", "Msps_ProvisioningService class, described"]
topic_type:
- apiref
api_name:
- Msps_ProvisioningService
api_location:
- MSPSService.dll
api_type:
- DllExport
---

# Msps\_ProvisioningService class

Represents the Shielded VM Provisioning Service. It is used to provision a new shielded virtual machine from a secure VHD template.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mspsservice"), AMENDMENT]
class Msps_ProvisioningService
{
};
```

## Members

The **Msps\_ProvisioningService** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msps\_ProvisioningService** class has these methods.



| Method                                                                                  | Description                                                                |
|:----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**PrepareSpecializedMachine**](msps-provisioningservice-preparespecializedmachine.md) | This method is used to prepare an existing VM for provisioning.<br/> |
| [**ProvisionMachine**](msps-provisioningservice-provisionmachine.md)                   | This method is used to securely provisioning a machine.<br/>         |



 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                             |
| Namespace<br/>                | Root\\MSPS<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>MSPSService.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSService.dll</dt> </dl> |



 

 





