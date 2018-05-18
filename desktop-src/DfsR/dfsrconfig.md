---
title: DfsrConfig class
description: This class is a DFSR configuration provider class. It includes provider-specific settings in addition to computer-wide service configuration parameters and methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e69c3cad-b977-48e7-b6bb-f6b6f2759c96'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DfsrConfig class Distributed File System Replication", "DfsrConfig class Distributed File System Replication , described"]
topic_type:
- apiref
api_name:
- DfsrConfig
- DfsrConfig.ProviderVersion
- DfsrConfig.ServiceVersion
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
---

# DfsrConfig class

This class is a DFSR configuration provider class. It includes provider-specific settings in addition to computer-wide service configuration parameters and methods.

## Syntax

``` syntax
[Dynamic, Provider("DfsrConfigProv"), Singleton]
class DfsrConfig
{
  string ProviderVersion;
  string ServiceVersion;
};
```

## Members

The **DfsrConfig** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DfsrConfig** class has these methods.



| Method                                    | Description                                                                                                                |
|:------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| [**PollDsNow**](polldsnow-dfsrconfig.md) | This static method polls the Active Directory for configuration changes and applies any changes to the service.<br/> |



 

### Properties

The **DfsrConfig** class has these properties.

<dl> <dt>

**ProviderVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("DFS Replication Configuration Provider Version")
</dt> </dl>

Current version of the provider.

The format of this string is *x*.*y*.*z*.*n*.

</dd> <dt>

**ServiceVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("DFS Replication Service Version")
</dt> </dl>

Service version.

The format of this string is *x*.*y*.*z*.*n*.

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





