---
title: RemoteAccessConnectionSummary class
description: Remote Access Connection Statistics Summary Record.
audience: developer
ms.assetid: 'f66dc48f-cdd0-42d1-9aaf-0f1acc731f3b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoteAccessConnectionSummary class", "RemoteAccessConnectionSummary class, described"]
topic_type:
- apiref
api_name:
- RemoteAccessConnectionSummary
- RemoteAccessConnectionSummary.TotalUniqueUsers
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# RemoteAccessConnectionSummary class

Remote Access Connection Statistics Summary Record

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessConnectionSummary
{
  uint32 TotalUniqueUsers;
};
```

## Members

The **RemoteAccessConnectionSummary** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessConnectionSummary** class has these properties.

<dl> <dt>

**TotalUniqueUsers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of unique users

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





