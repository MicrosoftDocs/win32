---
title: PdkVscApplicabilityCheck method of the Msps\_ProvisioningFileProcessor class
description: Validates whether a Provisioning Data KeyFile (PDK) can be applied to a volume represented by a Volume Signature Catalog (VSC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 20e8eb88-fbde-44c4-b4f1-f72391ed2d6e
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PdkVscApplicabilityCheck method
- PdkVscApplicabilityCheck method, Msps_ProvisioningFileProcessor class
- Msps_ProvisioningFileProcessor class, PdkVscApplicabilityCheck method
topic_type:
- apiref
api_name:
- Msps_ProvisioningFileProcessor.PdkVscApplicabilityCheck
api_location:
- MSPSProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PdkVscApplicabilityCheck method of the Msps\_ProvisioningFileProcessor class

Validates whether a Provisioning Data KeyFile (PDK) can be applied to a volume represented by a Volume Signature Catalog (VSC).

## Syntax


```mof
uint32 PdkVscApplicabilityCheck(
  [in]  Msps_VSC Vsc,
  [in]  Msps_PDK Pdk,
  [out] boolean  Applicable
);
```



## Parameters

<dl> <dt>

*Vsc* \[in\]
</dt> <dd>

The [**Msps\_VSC**](msps-vsc.md) object representing a template disk.

</dd> <dt>

*Pdk* \[in\]
</dt> <dd>

The [**Msps\_PDK**](msps-pdk.md) to be used to deploy the template disk.

</dd> <dt>

*Applicable* \[out\]
</dt> <dd>

True, if the PDK can be applied to a template disk of the supplied VSC.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\MSPS<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>MSPSProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msps\_ProvisioningFileProcessor**](msps-provisioningfileprocessor.md)
</dt> </dl>

 

 





