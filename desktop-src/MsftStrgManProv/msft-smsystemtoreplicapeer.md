---
title: MSFT\_SMSystemToReplicaPeer class
description: Represents an association between a system and a replica peer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f2d690df-f0c2-434a-9b43-224252368c1d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystemToReplicaPeer class
- MSFT_SMSystemToReplicaPeer class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystemToReplicaPeer
- MSFT_SMSystemToReplicaPeer.Parent
- MSFT_SMSystemToReplicaPeer.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMSystemToReplicaPeer class

Represents an association between a system and a replica peer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMSystemToReplicaPeer
{
  MSFT_SMSystem      REF Parent;
  MSFT_SMReplicaPeer REF Child;
};
```

## Members

The **MSFT\_SMSystemToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToReplicaPeer** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMReplicaPeer**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMReplicaPeer**](msft-smreplicapeer.md) object that represents the replica peer in the association.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMSystem**](msft-smsystem.md) object that represents the system in the association.

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

 

 





