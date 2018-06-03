---
title: MSFT\_SMDiscovery class
description: Represents a set of discovery information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4eb483eb-df5e-4646-8e80-39b5dc85938d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMDiscovery class
- MSFT_SMDiscovery class, described
topic_type:
- apiref
api_name:
- MSFT_SMDiscovery
- MSFT_SMDiscovery.DiscoveryId
- MSFT_SMDiscovery.Status
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMDiscovery class

Represents a set of discovery information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMDiscovery
{
  String DiscoveryId;
  String Status;
};
```

## Members

The **MSFT\_SMDiscovery** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMDiscovery** class has these properties.

<dl> <dt>

**DiscoveryId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of the discovery information.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the discovery information.

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

 

 





