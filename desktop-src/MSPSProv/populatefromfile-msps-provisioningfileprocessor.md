---
title: PopulateFromFile method of the Msps\_ProvisioningFileProcessor class
description: Populates a provisioning file from a file on disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9e9e484a-1d5c-4571-9add-c2db3af80fa8
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PopulateFromFile method
- PopulateFromFile method, Msps_ProvisioningFileProcessor class
- Msps_ProvisioningFileProcessor class, PopulateFromFile method
topic_type:
- apiref
api_name:
- Msps_ProvisioningFileProcessor.PopulateFromFile
api_location:
- MSPSProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PopulateFromFile method of the Msps\_ProvisioningFileProcessor class

Populates a provisioning file from a file on disk.

## Syntax


```mof
uint32 PopulateFromFile(
  [in]  string                FilePath,
  [out] Msps_ProvisioningFile ProvisioningFile
);
```



## Parameters

<dl> <dt>

*FilePath* \[in\]
</dt> <dd>

The path of the data file.

</dd> <dt>

*ProvisioningFile* \[out\]
</dt> <dd>

An embedded instance of the new [**Msps\_ProvisioningFile**](msps-provisioningfile.md) object.

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

 

 





