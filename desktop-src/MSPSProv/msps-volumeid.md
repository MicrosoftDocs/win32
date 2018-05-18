---
title: Msps\_VolumeID class
description: This class contains values used to identify a specific template disk volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '60e358ce-b9e3-4d2c-9b12-53b1ef2711cd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'shielded-vm-provisioning'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msps_VolumeID class", "Msps_VolumeID class, described"]
topic_type:
- apiref
api_name:
- Msps_VolumeID
- Msps_VolumeID.VolumeID
- Msps_VolumeID.Version
- Msps_VolumeID.Certificate
api_location:
- MSPSProv.dll
api_type:
- DllExport
---

# Msps\_VolumeID class

This class contains values used to identify a specific template disk volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mspsprov"), AMENDMENT]
class Msps_VolumeID
{
  string VolumeID;
  string Version;
  uint8  Certificate[];
};
```

## Members

The **Msps\_VolumeID** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msps\_VolumeID** class has these properties.

<dl> <dt>

**Certificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Certificate stored in this catalog, and used to verify signed data.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version of the template disk volume.

</dd> <dt>

**VolumeID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the template disk volume.

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
</dt> </dl>

 

 





