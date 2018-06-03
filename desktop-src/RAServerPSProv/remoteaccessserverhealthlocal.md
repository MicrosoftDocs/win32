---
title: RemoteAccessServerHealthLocal class
description: Remote Access Server Health object.
audience: developer
ms.assetid: 860707d9-ae64-40b3-976b-cd6abd82d825
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessServerHealthLocal class
- RemoteAccessServerHealthLocal class, described
topic_type:
- apiref
api_name:
- RemoteAccessServerHealthLocal
- RemoteAccessServerHealthLocal.HealthStatus
- RemoteAccessServerHealthLocal.NumOfHealthMonitors
- RemoteAccessServerHealthLocal.Data
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessServerHealthLocal class

Remote Access Server Health object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class RemoteAccessServerHealthLocal
{
  uint32 HealthStatus;
  uint32 NumOfHealthMonitors;
  uint8  Data[];
};
```

## Members

The **RemoteAccessServerHealthLocal** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessServerHealthLocal** class has these properties.

<dl> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Data Blob for all the health monitors

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Health Status

</dd> <dt>

**NumOfHealthMonitors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of health monitors

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





