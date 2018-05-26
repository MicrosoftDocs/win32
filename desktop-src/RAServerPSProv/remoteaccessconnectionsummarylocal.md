---
title: RemoteAccessConnectionSummaryLocal class
description: Contains the remote access connection statistics summary record.
audience: developer
ms.assetid: 6cf60eb0-e122-4e9a-a854-b4316c5e2c48
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessConnectionSummaryLocal class
- RemoteAccessConnectionSummaryLocal class, described
topic_type:
- apiref
api_name:
- RemoteAccessConnectionSummaryLocal
- RemoteAccessConnectionSummaryLocal.TotalUniqueUsers
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessConnectionSummaryLocal class

Contains the remote access connection statistics summary record.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class RemoteAccessConnectionSummaryLocal
{
  uint32 TotalUniqueUsers;
};
```

## Members

The **RemoteAccessConnectionSummaryLocal** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessConnectionSummaryLocal** class has these properties.

<dl> <dt>

**TotalUniqueUsers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of unique users.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





