---
title: MSFT\_DfsrServiceConfig class
description: This class is a DFSR configuration provider class. It includes provider-specific settings in addition to computer-wide service configuration parameters and methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6e45e13e-4e08-453d-b248-a668ec3f6cba
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrServiceConfig class Distributed File System Replication
- MSFT_DfsrServiceConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrServiceConfig
- MSFT_DfsrServiceConfig.Identifier
- MSFT_DfsrServiceConfig.ProviderVersion
- MSFT_DfsrServiceConfig.ServiceVersion
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DfsrServiceConfig class

This class is a DFSR configuration provider class. It includes provider-specific settings in addition to computer-wide service configuration parameters and methods.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrServiceConfig
{
  string Identifier;
  string ProviderVersion;
  string ServiceVersion;
};
```

## Members

The **MSFT\_DfsrServiceConfig** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsrServiceConfig** class has these methods.



| Method                                                | Description                                                                               |
|:------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**PollDsNow**](polldsnow-msft-dfsrserviceconfig.md) | Polls Active Directory Domain Services and applies any changes to the service.<br/> |



 

### Properties

The **MSFT\_DfsrServiceConfig** class has these properties.

<dl> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Identifier for DFSR service config")
</dt> </dl>

Identifier for the DFSR service configuration.

</dd> <dt>

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
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





