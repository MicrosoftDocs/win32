---
title: RemoteAccessUserActivityLocal class
description: Remote Access User Activity object.
audience: developer
ms.assetid: '5b7a94f3-21df-4df1-b794-902a885bc015'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoteAccessUserActivityLocal class", "RemoteAccessUserActivityLocal class, described"]
topic_type:
- apiref
api_name:
- RemoteAccessUserActivityLocal
- RemoteAccessUserActivityLocal.ServerIPAddress
- RemoteAccessUserActivityLocal.ProtocolID
- RemoteAccessUserActivityLocal.ServerPort
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
---

# RemoteAccessUserActivityLocal class

Remote Access User Activity object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class RemoteAccessUserActivityLocal
{
  string ServerIPAddress;
  uint32 ProtocolID;
  uint32 ServerPort;
};
```

## Members

The **RemoteAccessUserActivityLocal** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessUserActivityLocal** class has these properties.

<dl> <dt>

**ProtocolID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ID of the protocol using which the corp machine is being accessed

</dd> <dt>

**ServerIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Corp machine IP address which is accessed

</dd> <dt>

**ServerPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Port number using which Corp machine is being accessed

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





