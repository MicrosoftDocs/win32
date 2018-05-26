---
title: RemoteAccessAccountingSummary class
description: Remote Access Connection Statistics Summary Record From Accounting Data.
audience: developer
ms.assetid: de2b09b7-521b-489b-8144-a1ac0f78d0b3
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessAccountingSummary class
- RemoteAccessAccountingSummary class, described
topic_type:
- apiref
api_name:
- RemoteAccessAccountingSummary
- RemoteAccessAccountingSummary.TotalUniqueUsers
- RemoteAccessAccountingSummary.TotalSessions
- RemoteAccessAccountingSummary.TotalDASessions
- RemoteAccessAccountingSummary.TotalVpnSessions
- RemoteAccessAccountingSummary.TotalUniqueDAClients
- RemoteAccessAccountingSummary.AverageSessionsPerDay
- RemoteAccessAccountingSummary.MaxConcurrentSessions
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessAccountingSummary class

Remote Access Connection Statistics Summary Record From Accounting Data

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessAccountingSummary : RemoteAccessConnectionSummary
{
  uint32 TotalUniqueUsers;
  uint32 TotalSessions;
  uint32 TotalDASessions;
  uint32 TotalVpnSessions;
  uint32 TotalUniqueDAClients;
  uint32 AverageSessionsPerDay;
  uint32 MaxConcurrentSessions;
};
```

## Members

The **RemoteAccessAccountingSummary** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessAccountingSummary** class has these properties.

<dl> <dt>

**AverageSessionsPerDay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Average sessions per day

</dd> <dt>

**MaxConcurrentSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum concurrent sessions

</dd> <dt>

**TotalDASessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of direct access sessions

</dd> <dt>

**TotalSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of sessions

</dd> <dt>

**TotalUniqueDAClients**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of unique direct access clients

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

**TotalVpnSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of VPN sessions

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





