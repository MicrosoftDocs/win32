---
title: MSFT\_SMStorageDiscovery class
description: Represents a set of discovery information about a storage service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '35d76340-66c2-4de9-aaca-2c52166b9b1e'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMStorageDiscovery class", "MSFT_SMStorageDiscovery class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMStorageDiscovery
- MSFT_SMStorageDiscovery.systemName
- MSFT_SMStorageDiscovery.version
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMStorageDiscovery class

Represents a set of discovery information about a storage service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMStorageDiscovery
{
  String systemName;
  String version;
};
```

## Members

The **MSFT\_SMStorageDiscovery** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMStorageDiscovery** class has these methods.



| Method                                                               | Description                                                                |
|:---------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**PartialDiscovery**](partialdiscovery-msft-smstoragediscovery.md) | Starts the Microsoft storage service partial discovery process.<br/> |
| [**StartDiscovery**](startdiscovery-msft-smstoragediscovery.md)     | Starts the Microsoft storage service discovery process.<br/>         |



 

### Properties

The **MSFT\_SMStorageDiscovery** class has these properties.

<dl> <dt>

**systemName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the system.

</dd> <dt>

**version**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the storage service.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





