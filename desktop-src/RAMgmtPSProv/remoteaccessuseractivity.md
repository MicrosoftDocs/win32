---
title: RemoteAccessUserActivity class
description: Remote Access User Activity object.
audience: developer
ms.assetid: 80711289-4b13-4acd-b2c1-e3de92650c08
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessUserActivity class
- RemoteAccessUserActivity class, described
topic_type:
- apiref
api_name:
- RemoteAccessUserActivity
- RemoteAccessUserActivity.ServerIPAddress
- RemoteAccessUserActivity.ProtocolID
- RemoteAccessUserActivity.ServerPort
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessUserActivity class

Remote Access User Activity object

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessUserActivity
{
  string ServerIPAddress;
  uint32 ProtocolID;
  uint32 ServerPort;
};
```

## Members

The **RemoteAccessUserActivity** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessUserActivity** class has these properties.

<dl> <dt>

**ProtocolID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ID of the protocol being used to access the server

</dd> <dt>

**ServerIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the server that is accessed

</dd> <dt>

**ServerPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Port number being used to access the server

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





