---
title: Msps\_FSK class
description: Represents a Fabric Specialization KeyFile (FSK).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 465225c4-0f51-45ac-a385-7278329d39a1
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msps_FSK class
- Msps_FSK class, described
topic_type:
- apiref
api_name:
- Msps_FSK
- Msps_FSK.RawData
- Msps_FSK.FabricDataPairs
api_location:
- MSPSProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msps\_FSK class

Represents a Fabric Specialization KeyFile (FSK). An FSK contains public data that will be securely transferred to a machine as part of the secure provisioning process.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mspsprov"), AMENDMENT]
class Msps_FSK : Msps_ProvisioningFile
{
  uint8           RawData[];
  Msps_FabricData FabricDataPairs[];
};
```

## Members

The **Msps\_FSK** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msps\_FSK** class has these properties.

<dl> <dt>

**FabricDataPairs**
</dt> <dd> <dl> <dt>

Data type: **Msps\_FabricData** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**Msps\_FabricData**](msps-fabricdata.md)")
</dt> </dl>

An array of [**Msps\_FabricData**](msps-fabricdata.md) objects contained in this FSK.

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

[**Msps\_FabricData**](msps-fabricdata.md)
</dt> <dt>

[**Msps\_ProvisioningFile**](msps-provisioningfile.md)
</dt> </dl>

 

 





