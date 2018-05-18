---
title: MSFT\_SMDiscoveryToSystem class
description: Represents a relationship between a set of discovery information and a system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4ad27144-3929-4835-8bf9-897ec90b8deb'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMDiscoveryToSystem class", "MSFT_SMDiscoveryToSystem class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMDiscoveryToSystem
- MSFT_SMDiscoveryToSystem.Parent
- MSFT_SMDiscoveryToSystem.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMDiscoveryToSystem class

Represents a relationship between a set of discovery information and a system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMDiscoveryToSystem
{
  MSFT_SMDiscovery REF Parent;
  MSFT_SMSystem    REF Child;
};
```

## Members

The **MSFT\_SMDiscoveryToSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMDiscoveryToSystem** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMSystem**](msft-smsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMSystem**](msft-smsystem.md) object that represents the system in the relationship.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





