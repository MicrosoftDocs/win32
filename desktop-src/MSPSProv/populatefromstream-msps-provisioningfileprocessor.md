---
title: PopulateFromStream method of the Msps\_ProvisioningFileProcessor class
description: Populates a provisioning file from a byte stream. May not be supported by large provisioning files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d329d0dc-f2ea-49ac-abe4-a7660fe791f8
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PopulateFromStream method
- PopulateFromStream method, Msps_ProvisioningFileProcessor class
- Msps_ProvisioningFileProcessor class, PopulateFromStream method
topic_type:
- apiref
api_name:
- Msps_ProvisioningFileProcessor.PopulateFromStream
api_location:
- MSPSProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PopulateFromStream method of the Msps\_ProvisioningFileProcessor class

Populates a provisioning file from a byte stream. May not be supported by large provisioning files.

## Syntax


```mof
uint32 PopulateFromStream(
  [in]  uint8                 Data[],
  [out] Msps_ProvisioningFile ProvisioningFile
);
```



## Parameters

<dl> <dt>

*Data* \[in\]
</dt> <dd>

An octetstring containing the data to use to populate the provisioning file.

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

 

 





