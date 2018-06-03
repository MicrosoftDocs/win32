---
title: MSFT\_SMSystemToReplicationCapabilities class
description: Represents an association between a system and a set of system capabilities.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 83bddf52-a161-4e19-b748-8471fee144de
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystemToReplicationCapabilities class
- MSFT_SMSystemToReplicationCapabilities class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystemToReplicationCapabilities
- MSFT_SMSystemToReplicationCapabilities.Parent
- MSFT_SMSystemToReplicationCapabilities.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMSystemToReplicationCapabilities class

Represents an association between a system and a set of system capabilities.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMSystemToReplicationCapabilities
{
  MSFT_SMSystem                  REF Parent;
  MSFT_SMReplicationCapabilities REF Child;
};
```

## Members

The **MSFT\_SMSystemToReplicationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToReplicationCapabilities** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMReplicationCapabilities**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMReplicationCapabilities**](msft-smreplicationcapabilities.md) object that represents the set of system capabilities in the association.

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

 

 





