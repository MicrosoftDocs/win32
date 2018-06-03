---
title: MSFT\_ServerServiceDetail class
description: Represents the details about an installed system service on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dbf4b1ab-c752-41e8-8a14-064f3972ebbc
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_ServerServiceDetail class
- MSFT_ServerServiceDetail class, described
topic_type:
- apiref
api_name:
- MSFT_ServerServiceDetail
- MSFT_ServerServiceDetail.Name
- MSFT_ServerServiceDetail.DisplayName
- MSFT_ServerServiceDetail.Description
- MSFT_ServerServiceDetail.StartupType
- MSFT_ServerServiceDetail.IsDelayedAutoStart
- MSFT_ServerServiceDetail.IsTriggered
- MSFT_ServerServiceDetail.SupportedControlCodes
- MSFT_ServerServiceDetail.Status
- MSFT_ServerServiceDetail.ExitCode
- MSFT_ServerServiceDetail.DependentServices
api_location:
- MgmtProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_ServerServiceDetail class

Represents the details about an installed system service on the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerServiceDetail
{
  string  Name;
  string  DisplayName;
  string  Description;
  uint32  StartupType;
  boolean IsDelayedAutoStart;
  boolean IsTriggered;
  uint32  SupportedControlCodes;
  uint32  Status = 0;
  uint64  ExitCode = 0;
  string  DependentServices[];
};
```

## Members

The **MSFT\_ServerServiceDetail** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerServiceDetail** class has these properties.

<dl> <dt>

**DependentServices**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list of names of dependent services.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description of the service.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The localized name of the service.

</dd> <dt>

**ExitCode**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The service exit code reported by the Service Control Manager.

</dd> <dt>

**IsDelayedAutoStart**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Is the service auto delayed start.

</dd> <dt>

**IsTriggered**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Does the service has other start triggers.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the service.

</dd> <dt>

**StartupType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The startup type of the service.

<dt>

<span id="Boot"></span><span id="boot"></span><span id="BOOT"></span>

**Boot** (0)


</dt> <dd></dd> <dt>

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>

**System** (1)


</dt> <dd></dd> <dt>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>

**Auto** (2)


</dt> <dd></dd> <dt>

<span id="Demand"></span><span id="demand"></span><span id="DEMAND"></span>

**Demand** (3)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the service.

<dt>

<span id="Not_Found"></span><span id="not_found"></span><span id="NOT_FOUND"></span>

**Not Found** (0)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (1)


</dt> <dd></dd> <dt>

<span id="Start_Pending"></span><span id="start_pending"></span><span id="START_PENDING"></span>

**Start Pending** (2)


</dt> <dd></dd> <dt>

<span id="Stop_Pending"></span><span id="stop_pending"></span><span id="STOP_PENDING"></span>

**Stop Pending** (3)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

**Running** (4)


</dt> <dd></dd> <dt>

<span id="Continue_Pending"></span><span id="continue_pending"></span><span id="CONTINUE_PENDING"></span>

**Continue Pending** (5)


</dt> <dd></dd> <dt>

<span id="Pause_Pending"></span><span id="pause_pending"></span><span id="PAUSE_PENDING"></span>

**Pause Pending** (6)


</dt> <dd></dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

**Paused** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**SupportedControlCodes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**BitMap**](https://msdn.microsoft.com/library/aa393650) ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), [**BitValues**](https://msdn.microsoft.com/library/aa393650) ("Stop", "Pause Continue", "Shutdown", "Parameter Change", "Net Binding Change", "Hardware Profile Change", "Power Event", "Session Change", "PreShutdown", "Time Change", "Trigger Event")
</dt> </dl>

The control codes supported by the service.

<dt>

0
</dt> <dd>

Stop

</dd> <dt>

1
</dt> <dd>

Pause Continue

</dd> <dt>

2
</dt> <dd>

Shutdown

</dd> <dt>

3
</dt> <dd>

Parameter Change

</dd> <dt>

4
</dt> <dd>

Net Binding Change

</dd> <dt>

5
</dt> <dd>

Hardware Profile Change

</dd> <dt>

6
</dt> <dd>

Power Event

</dd> <dt>

7
</dt> <dd>

Session Change

</dd> <dt>

8
</dt> <dd>

PreShutdown

</dd> <dt>

9
</dt> <dd>

Time Change

</dd> <dt>

10
</dt> <dd>

Trigger Event

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



 

 





