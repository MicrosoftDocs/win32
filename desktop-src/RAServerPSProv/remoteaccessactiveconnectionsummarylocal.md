---
title: RemoteAccessActiveConnectionSummaryLocal class
description: Remote Access Connection Statistics Summary for Active Connections.
audience: developer
ms.assetid: 00358ae8-f063-4d38-b364-2624bddc4700
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessActiveConnectionSummaryLocal class
- RemoteAccessActiveConnectionSummaryLocal class, described
topic_type:
- apiref
api_name:
- RemoteAccessActiveConnectionSummaryLocal
- RemoteAccessActiveConnectionSummaryLocal.TotalUniqueUsers
- RemoteAccessActiveConnectionSummaryLocal.TotalConnections
- RemoteAccessActiveConnectionSummaryLocal.TotalDAConnections
- RemoteAccessActiveConnectionSummaryLocal.TotalVpnConnections
- RemoteAccessActiveConnectionSummaryLocal.TotalCumulativeConnections
- RemoteAccessActiveConnectionSummaryLocal.TotalBytesIn
- RemoteAccessActiveConnectionSummaryLocal.TotalBytesOut
- RemoteAccessActiveConnectionSummaryLocal.TotalBytesInOut
- RemoteAccessActiveConnectionSummaryLocal.MaxConcurrentConnections
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessActiveConnectionSummaryLocal class

Remote Access Connection Statistics Summary for Active Connections

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class RemoteAccessActiveConnectionSummaryLocal : RemoteAccessConnectionSummaryLocal
{
  uint32 TotalUniqueUsers;
  uint32 TotalConnections;
  uint32 TotalDAConnections;
  uint32 TotalVpnConnections;
  uint32 TotalCumulativeConnections;
  uint64 TotalBytesIn;
  uint64 TotalBytesOut;
  uint64 TotalBytesInOut;
  uint32 MaxConcurrentConnections;
};
```

## Members

The **RemoteAccessActiveConnectionSummaryLocal** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessActiveConnectionSummaryLocal** class has these properties.

<dl> <dt>

**MaxConcurrentConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (MaxConcurrentConnections)
</dt> </dl>

The maximum number of concurrent connections.

</dd> <dt>

**TotalBytesIn**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total bytes recieved since the service started.

</dd> <dt>

**TotalBytesInOut**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of bytes in and out since the service started.

</dd> <dt>

**TotalBytesOut**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total bytes output since the service started.

</dd> <dt>

**TotalConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (TotalConnections)
</dt> </dl>

The number of total connections.

</dd> <dt>

**TotalCumulativeConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of cumulative connections since the service started.

</dd> <dt>

**TotalDAConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (TotalDAConnections)
</dt> </dl>

The total number of direct access connections.

</dd> <dt>

**TotalUniqueUsers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of unique users.

This property is inherited from [**RemoteAccessConnectionSummaryLocal**](remoteaccessconnectionsummarylocal.md).

</dd> <dt>

**TotalVpnConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (TotalVpnConnections)
</dt> </dl>

The total number of VPN connections.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**RemoteAccessConnectionSummaryLocal**](remoteaccessconnectionsummarylocal.md)
</dt> </dl>

 

 





