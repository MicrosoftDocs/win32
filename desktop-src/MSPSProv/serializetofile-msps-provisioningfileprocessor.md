---
title: SerializeToFile method of the Msps\_ProvisioningFileProcessor class
description: Serialize a provisioning file to a file on disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6822ebe0-09ed-462e-9ddf-cb6cf3aa8b67'
ms.prod: 'windows-server-dev'
ms.technology:
- 'shielded-vm-provisioning'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SerializeToFile method", "SerializeToFile method, Msps_ProvisioningFileProcessor class", "Msps_ProvisioningFileProcessor class, SerializeToFile method"]
topic_type:
- apiref
api_name:
- Msps_ProvisioningFileProcessor.SerializeToFile
api_location:
- MSPSProv.dll
api_type:
- COM
---

# SerializeToFile method of the Msps\_ProvisioningFileProcessor class

Serialize a provisioning file to a file on disk. May not be supported by all provisioning file instances.

## Syntax


```mof
uint32 SerializeToFile(
  [in] string                FilePath,
  [in] Msps_ProvisioningFile ProvisioningFile
);
```



## Parameters

<dl> <dt>

*FilePath* \[in\]
</dt> <dd>

The file to create.

</dd> <dt>

*ProvisioningFile* \[in\]
</dt> <dd>

The [**Msps\_ProvisioningFile**](msps-provisioningfile.md) object to serialize.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\MSPS<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>MSPSProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msps\_ProvisioningFileProcessor**](msps-provisioningfileprocessor.md)
</dt> </dl>

 

 





