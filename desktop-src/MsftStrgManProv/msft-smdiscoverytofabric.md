---
title: MSFT\_SMDiscoveryToFabric class
description: Represents a relationship between a set of discovery information and a Windows Fabric storage service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 826ea89e-f06c-43d1-b27a-84be728446b2
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMDiscoveryToFabric class
- MSFT_SMDiscoveryToFabric class, described
topic_type:
- apiref
api_name:
- MSFT_SMDiscoveryToFabric
- MSFT_SMDiscoveryToFabric.Parent
- MSFT_SMDiscoveryToFabric.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMDiscoveryToFabric class

Represents a relationship between a set of discovery information and a Windows Fabric storage service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMDiscoveryToFabric
{
  MSFT_SMDiscovery REF Parent;
  MSFT_SMFabric    REF Child;
};
```

## Members

The **MSFT\_SMDiscoveryToFabric** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMDiscoveryToFabric** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFabric**](msft-smfabric.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMFabric**](msft-smfabric.md) object that represents the Windows Fabric storage service in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMDiscovery**](msft-smdiscovery.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMDiscovery**](msft-smdiscovery.md) object that represents the discovery information in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





