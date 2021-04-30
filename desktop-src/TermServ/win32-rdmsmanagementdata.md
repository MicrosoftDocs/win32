---
title: Win32_RDMSManagementData class
description: Synchronizes publishing data for Remote Desktop Management Services (RDMS).
ms.assetid: 17f06294-6580-4297-9301-f88314db7775
ms.tgt_platform: multiple
keywords:
- Win32_RDMSManagementData class Remote Desktop Services
- Win32_RDMSManagementData class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDMSManagementData
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDMSManagementData class

Synchronizes publishing data for Remote Desktop Management Services (RDMS).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDMSManagementData
{
};
```

## Members

The **Win32\_RDMSManagementData** class has these types of members:

-   [Methods](#methods)

### Methods

The **Win32\_RDMSManagementData** class has these methods.



| Method                                                                                        | Description                                                            |
|:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**SynchronizeAllPublishingData**](synchronizeallpublishingdata-win32-rdmsmanagementdata.md) | Synchronizes all publishing data for RDMS.<br/>                  |
| [**SynchronizePublishingData**](synchronizepublishingdata-win32-rdmsmanagementdata.md)       | Synchronizes the specified set of publishing data for RDMS.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> </dl>

 

 





