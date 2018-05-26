---
title: Msps\_FabricData class
description: A key/value pair representing a Fabric Data entry for a Fabric Specialization KeyFile (FSK).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 98286a93-45b7-4ae4-afab-e70db7f5ce6c
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msps_FabricData class
- Msps_FabricData class, described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msps\_FabricData class

A key/value pair representing a Fabric Data entry for a Fabric Specialization KeyFile (FSK).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mspsprov"), AMENDMENT]
class Msps_FabricData
{
  string key;
  string Value;
};
```

## Members

The **Msps\_FabricData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msps\_FabricData** class has these properties.

<dl> <dt>

**key**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

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

[**Msps\_FSK**](msps-fsk.md)
</dt> </dl>

 

 





