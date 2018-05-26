---
title: RemoteAccessHealthMonitor class
description: Remote Access Health Monitor.
audience: developer
ms.assetid: a72e7e24-6d50-4029-ab1d-b5d12d2f3bff
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessHealthMonitor class
- RemoteAccessHealthMonitor class, described
topic_type:
- apiref
api_name:
- RemoteAccessHealthMonitor
- RemoteAccessHealthMonitor.Component
- RemoteAccessHealthMonitor.RemoteAccessServer
- RemoteAccessHealthMonitor.HealthState
- RemoteAccessHealthMonitor.TimeStamp
- RemoteAccessHealthMonitor.Heuristics
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessHealthMonitor class

Remote Access Health Monitor

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessHealthMonitor
{
  string                      Component;
  string                      RemoteAccessServer;
  string                      HealthState;
  datetime                    TimeStamp;
  RemoteAccessHealthHeuristic Heuristics[];
};
```

## Members

The **RemoteAccessHealthMonitor** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessHealthMonitor** class has these properties.

<dl> <dt>

**Component**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The component of DA or VPN whose health impacts the overall health of the server or cluster

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health of the component

The possible values are.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** ("Warning")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> </dl>

</dd> <dt>

**Heuristics**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessHealthHeuristic** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessHealthHeuristic**](remoteaccesshealthheuristic.md)")
</dt> </dl>

An array of health heuristics

</dd> <dt>

**RemoteAccessServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Remote Access server whose component health is represented

</dd> <dt>

**TimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when the component health changed to the current state

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





