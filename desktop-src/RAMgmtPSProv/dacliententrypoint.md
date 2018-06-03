---
title: DAClientEntrypoint class
description: DirectAccess client entry point specific settings class.
audience: developer
ms.assetid: 10cdc4df-687c-4d9c-92b1-0f8c891d2cf3
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAClientEntrypoint class
- DAClientEntrypoint class, described
topic_type:
- apiref
api_name:
- DAClientEntrypoint
- DAClientEntrypoint.DownlevelSecurityGroupNameList
- DAClientEntrypoint.DownlevelGpoName
- DAClientEntrypoint.EntrypointName
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DAClientEntrypoint class

DirectAccess client entry point specific settings class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAClientEntrypoint
{
  string DownlevelSecurityGroupNameList[];
  string DownlevelGpoName[];
  string EntrypointName;
};
```

## Members

The **DAClientEntrypoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAClientEntrypoint** class has these properties.

<dl> <dt>

**DownlevelGpoName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Downlevel Gpo name list

</dd> <dt>

**DownlevelSecurityGroupNameList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Downlevel security group name list

</dd> <dt>

**EntrypointName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the entry point

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





