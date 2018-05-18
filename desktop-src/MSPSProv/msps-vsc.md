---
title: Msps\_VSC class
description: An OS Volume Signature Catalog (VSC) contents are signed by a signature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '32190b95-e943-4f5b-9284-e3d7668ab432'
ms.prod: 'windows-server-dev'
ms.technology:
- 'shielded-vm-provisioning'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msps_VSC class", "Msps_VSC class, described"]
topic_type:
- apiref
api_name:
- Msps_VSC
- Msps_VSC.RawData
- Msps_VSC.VolumeID
api_location:
- MSPSProv.dll
api_type:
- DllExport
---

# Msps\_VSC class

An OS Volume Signature Catalog (VSC) contents are signed by a signature. A Populate command will fail if the signature is not valid.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mspsprov"), AMENDMENT]
class Msps_VSC : Msps_ProvisioningFile
{
  uint8         RawData[];
  Msps_VolumeID VolumeID;
};
```

## Members

The **Msps\_VSC** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msps\_VSC** class has these properties.

<dl> <dt>

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

**VolumeID**
</dt> <dd> <dl> <dt>

Data type: **Msps\_VolumeID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**Msps\_VolumeID**](msps-volumeid.md)")
</dt> </dl>

The signed [**Msps\_VolumeID**](msps-volumeid.md) embedded object describing the template disk associated with this catalog.

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

[Shielded VM Provisioning WMI Provider](shielded-vm-provisioning-wmi-provider-portal.md)
</dt> <dt>

[**Msps\_ProvisioningFile**](msps-provisioningfile.md)
</dt> <dt>

[**Msps\_VolumeID**](msps-volumeid.md)
</dt> </dl>

 

 





