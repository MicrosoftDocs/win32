---
title: Msps\_ProvisioningFile class
description: An abstract class representing raw data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 292f72bf-7e82-4d23-9da2-e67cc0800fda
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msps_ProvisioningFile class
- Msps_ProvisioningFile class, described
topic_type:
- apiref
api_name:
- Msps_ProvisioningFile
- Msps_ProvisioningFile.RawData
api_location:
- MSPSProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msps\_ProvisioningFile class

An abstract class representing raw data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class Msps_ProvisioningFile
{
  uint8 RawData[];
};
```

## Members

The **Msps\_ProvisioningFile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msps\_ProvisioningFile** class has these properties.

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
</dt> <dt>

[**Msps\_PDK**](msps-pdk.md)
</dt> <dt>

[**Msps\_VSC**](msps-vsc.md)
</dt> </dl>

 

 





