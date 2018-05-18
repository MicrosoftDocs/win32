---
title: DAAppServer class
description: DirectAccess application server class.
audience: developer
ms.assetid: 'fc828e53-ebc3-489b-a4bc-5fbaeacca1a4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DAAppServer class", "DAAppServer class, described"]
topic_type:
- apiref
api_name:
- DAAppServer
- DAAppServer.SecurityGroupNameList
- DAAppServer.AppServerConnection
- DAAppServer.GpoName
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DAAppServer class

DirectAccess application server class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAAppServer
{
  string                SecurityGroupNameList[];
  DAAppServerConnection AppServerConnection;
  string                GpoName[];
};
```

## Members

The **DAAppServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAAppServer** class has these properties.

<dl> <dt>

**AppServerConnection**
</dt> <dd> <dl> <dt>

Data type: **DAAppServerConnection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAAppServerConnection**](daappserverconnection.md)")
</dt> </dl>

A [**DAAppServerConnection**](daappserverconnection.md) embedded instance

</dd> <dt>

**GpoName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

List of application server GPOs

</dd> <dt>

**SecurityGroupNameList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An arrary of application server security groups

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





