---
title: Msps\_VolumeIDFilter class
description: Contains additional information which can be used to filter a list of volumes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 50116467-249e-4dcd-8cec-bfa1f87fffcf
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msps_VolumeIDFilter class
- Msps_VolumeIDFilter class, described
topic_type:
- apiref
api_name:
- Msps_VolumeIDFilter
- Msps_VolumeIDFilter.VolumeID
- Msps_VolumeIDFilter.VersionRule
api_location:
- MSPSProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msps\_VolumeIDFilter class

Contains additional information which can be used to filter a list of volumes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mspsprov"), AMENDMENT]
class Msps_VolumeIDFilter
{
  Msps_VolumeID VolumeID;
  uint8         VersionRule;
};
```

## Members

The **Msps\_VolumeIDFilter** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msps\_VolumeIDFilter** class has these properties.

<dl> <dt>

**VersionRule**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version rule to evaluate the **Version** property of [**Msps\_VolumeID**](msps-volumeid.md) instance.

The possible values are.

<dt>

<span id="Equal"></span><span id="equal"></span><span id="EQUAL"></span>

**Equal** (0)


</dt> <dd></dd> <dt>

<span id="GreaterThan"></span><span id="greaterthan"></span><span id="GREATERTHAN"></span>

**GreaterThan** (1)


</dt> <dd></dd> <dt>

<span id="GreaterThanOrEqual"></span><span id="greaterthanorequal"></span><span id="GREATERTHANOREQUAL"></span>

**GreaterThanOrEqual** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**VolumeID**
</dt> <dd> <dl> <dt>

Data type: **Msps\_VolumeID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**Msps\_VolumeID**](msps-volumeid.md)")
</dt> </dl>

Identifies a volume. May contain wild cards.

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
</dt> </dl>

 

 





