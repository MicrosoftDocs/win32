---
title: RemoteAccessMonitoringSummary class
description: Remote Access Connection Statistics Summary Record From Monitoring Data.
audience: developer
ms.assetid: 0623f16a-4cc1-4a10-a874-2525dc83ceef
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessMonitoringSummary class
- RemoteAccessMonitoringSummary class, described
topic_type:
- apiref
api_name:
- RemoteAccessMonitoringSummary
- RemoteAccessMonitoringSummary.TotalUniqueUsers
- RemoteAccessMonitoringSummary.TotalCumulativeConnections
- RemoteAccessMonitoringSummary.TotalBytesIn
- RemoteAccessMonitoringSummary.TotalBytesOut
- RemoteAccessMonitoringSummary.TotalBytesInOut
- RemoteAccessMonitoringSummary.TotalConnections
- RemoteAccessMonitoringSummary.TotalDAConnections
- RemoteAccessMonitoringSummary.TotalVpnConnections
- RemoteAccessMonitoringSummary.MaxConcurrentConnections
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessMonitoringSummary class

Remote Access Connection Statistics Summary Record From Monitoring Data

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessMonitoringSummary : RemoteAccessConnectionSummary
{
  uint32 TotalUniqueUsers;
  uint32 TotalCumulativeConnections;
  uint64 TotalBytesIn;
  uint64 TotalBytesOut;
  uint64 TotalBytesInOut;
  uint32 TotalConnections;
  uint32 TotalDAConnections;
  uint32 TotalVpnConnections;
  uint32 MaxConcurrentConnections;
};
```

## Members

The **RemoteAccessMonitoringSummary** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessMonitoringSummary** class has these properties.

<dl> <dt>

**MaxConcurrentConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum concurrent connections

</dd> <dt>

**TotalBytesIn**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total bytes in since service start

</dd> <dt>

**TotalBytesInOut**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total bytes in/out since service start

</dd> <dt>

**TotalBytesOut**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total bytes out since service start.

</dd> <dt>

**TotalConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of connections

</dd> <dt>

**TotalCumulativeConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total cumulative connections since start of service

</dd> <dt>

**TotalDAConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of direct access connections

</dd> <dt>

**TotalUniqueUsers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of unique users

This property is inherited from [**RemoteAccessConnectionSummary**](remoteaccessconnectionsummary.md).

</dd> <dt>

**TotalVpnConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of VPN connections

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





