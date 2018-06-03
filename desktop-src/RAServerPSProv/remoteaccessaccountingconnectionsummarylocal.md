---
title: RemoteAccessAccountingConnectionSummaryLocal class
description: Remote Access Connection Statistics Summary Record From Accounting Data.
audience: developer
ms.assetid: 2e6ab500-3689-484a-917e-195995d0f5ab
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessAccountingConnectionSummaryLocal class
- RemoteAccessAccountingConnectionSummaryLocal class, described
topic_type:
- apiref
api_name:
- RemoteAccessAccountingConnectionSummaryLocal
- RemoteAccessAccountingConnectionSummaryLocal.TotalSessions
- RemoteAccessAccountingConnectionSummaryLocal.TotalDASessions
- RemoteAccessAccountingConnectionSummaryLocal.TotalVpnSessions
- RemoteAccessAccountingConnectionSummaryLocal.TotalUniqueDAClients
- RemoteAccessAccountingConnectionSummaryLocal.AverageSessionsPerDay
- RemoteAccessAccountingConnectionSummaryLocal.MaxConcurrentSessions
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessAccountingConnectionSummaryLocal class

Remote Access Connection Statistics Summary Record From Accounting Data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class RemoteAccessAccountingConnectionSummaryLocal : RemoteAccessConnectionSummaryLocal
{
  uint32 TotalSessions;
  uint32 TotalDASessions;
  uint32 TotalVpnSessions;
  uint32 TotalUniqueDAClients;
  uint32 AverageSessionsPerDay;
  uint32 MaxConcurrentSessions;
};
```

## Members

The **RemoteAccessAccountingConnectionSummaryLocal** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessAccountingConnectionSummaryLocal** class has these properties.

<dl> <dt>

**AverageSessionsPerDay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The average number of sessions per day.

</dd> <dt>

**MaxConcurrentSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of concurrent sessions.

</dd> <dt>

**TotalDASessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

the total number of direct access sessions.

</dd> <dt>

**TotalSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of sessions.

</dd> <dt>

**TotalUniqueDAClients**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of unique direct access clients.

</dd> <dt>

**TotalVpnSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of VPN sessions.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





