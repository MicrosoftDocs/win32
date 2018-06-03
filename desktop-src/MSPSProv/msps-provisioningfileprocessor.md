---
title: Msps\_ProvisioningFileProcessor class
description: Provides common serialization methods for PtP classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7333921b-c0b7-48d0-adee-f9bd242ba8d0
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msps_ProvisioningFileProcessor class
- Msps_ProvisioningFileProcessor class, described
topic_type:
- apiref
api_name:
- Msps_ProvisioningFileProcessor
api_location:
- MSPSProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msps\_ProvisioningFileProcessor class

Provides common serialization methods for PtP classes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mspsprov"), AMENDMENT]
class Msps_ProvisioningFileProcessor
{
};
```

## Members

The **Msps\_ProvisioningFileProcessor** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msps\_ProvisioningFileProcessor** class has these methods.



| Method                                                                                      | Description                                                                                                               |
|:--------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**PdkVscApplicabilityCheck**](pdkvscapplicabilitycheck-msps-provisioningfileprocessor.md) | Determines if a PDK can be applied to a volume represented by a VSC.<br/>                                           |
| [**PopulateFromFile**](populatefromfile-msps-provisioningfileprocessor.md)                 | Populates an provisioning file from a file on disk.<br/>                                                            |
| [**PopulateFromStream**](populatefromstream-msps-provisioningfileprocessor.md)             | Populates an provisioning file from a byte stream. May not be supported by large provisioning files.<br/>           |
| [**QueryPolicyValue**](msps-provisioningfileprocessor-querypolicyvalue.md)                 | Requests a specific policy from a provided policy data set.<br/>                                                    |
| [**SerializeToFile**](serializetofile-msps-provisioningfileprocessor.md)                   | Serialize a provisioning file from to a file on disk. May not be supported by all provisioning file instances.<br/> |



 

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

 

 





