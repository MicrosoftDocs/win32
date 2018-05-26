---
title: Msps\_PDK class
description: Represents a Provisioning Data KeyFile (PDK).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed6bf6fc-bac0-472b-b734-f28fa0c66257
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msps_PDK class
- Msps_PDK class, described
topic_type:
- apiref
api_name:
- Msps_PDK
- Msps_PDK.RawData
- Msps_PDK.KeyProtector
- Msps_PDK.VolumeIDFilters
- Msps_PDK.PolicyData
api_location:
- MSPSProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msps\_PDK class

Represents a Provisioning Data KeyFile (PDK). A PDK contains private data that will be securely transferred to a machine as part of the secure provisioning process. Only the clear portions of the PDK are retrievable through this interface.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mspsprov"), AMENDMENT]
class Msps_PDK : Msps_ProvisioningFile
{
  uint8               RawData[];
  uint8               KeyProtector[];
  Msps_VolumeIDFilter VolumeIDFilters[];
  uint8               PolicyData[];
};
```

## Members

The **Msps\_PDK** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msps\_PDK** class has these properties.

<dl> <dt>

**KeyProtector**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**
</dt> </dl>

The KP associated with this PDK.

</dd> <dt>

**PolicyData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**
</dt> </dl>

The policy blob associated with this PDK.

</dd> <dt>

**RawData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**
</dt> </dl>

The encrypted raw data of the file.

This property is inherited from [**Msps\_ProvisioningFile**](msps-provisioningfile.md).

</dd> <dt>

**VolumeIDFilters**
</dt> <dd> <dl> <dt>

Data type: **Msps\_VolumeIDFilter** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**Msps\_VolumeIDFilter**](msps-volumeidfilter.md)")
</dt> </dl>

An array of [**Msps\_VolumeIDFilter**](msps-volumeidfilter.md) objects that this PDK applies to.

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

[Shielded VM Provisioning WMI Provider](shielded-vm-provisioning-wmi-provider-portal.md)
</dt> <dt>

[**Msps\_ProvisioningFile**](msps-provisioningfile.md)
</dt> <dt>

[**Msps\_VolumeIDFilter**](msps-volumeidfilter.md)
</dt> </dl>

 

 





