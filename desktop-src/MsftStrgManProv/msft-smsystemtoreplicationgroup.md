---
title: MSFT\_SMSystemToReplicationGroup class
description: Represents a relationship between a system and a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: daed3622-f0e4-4e1f-a646-8d32397562f1
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystemToReplicationGroup class
- MSFT_SMSystemToReplicationGroup class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystemToReplicationGroup
- MSFT_SMSystemToReplicationGroup.Parent
- MSFT_SMSystemToReplicationGroup.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMSystemToReplicationGroup class

Represents a relationship between a system and a replication group.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMSystemToReplicationGroup
{
  MSFT_SMSystem           REF Parent;
  MSFT_SMReplicationGroup REF Child;
};
```

## Members

The **MSFT\_SMSystemToReplicationGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToReplicationGroup** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMReplicationGroup**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the replication group in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the system in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





