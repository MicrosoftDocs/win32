---
title: RemoteAccessHealthHeuristic class
description: Remote Access Health Heuristic.
audience: developer
ms.assetid: 2b2c774a-cce5-4cb4-aae2-7aac8bb8cb55
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessHealthHeuristic class
- RemoteAccessHealthHeuristic class, described
topic_type:
- apiref
api_name:
- RemoteAccessHealthHeuristic
- RemoteAccessHealthHeuristic.Id
- RemoteAccessHealthHeuristic.Status
- RemoteAccessHealthHeuristic.OperationStatus
- RemoteAccessHealthHeuristic.ErrorDesc
- RemoteAccessHealthHeuristic.ErrorCause
- RemoteAccessHealthHeuristic.ErrorResoln
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessHealthHeuristic class

Remote Access Health Heuristic

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessHealthHeuristic
{
  uint32 Id;
  string Status;
  string OperationStatus;
  string ErrorDesc;
  string ErrorCause;
  string ErrorResoln;
};
```

## Members

The **RemoteAccessHealthHeuristic** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessHealthHeuristic** class has these properties.

<dl> <dt>

**ErrorCause**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the cause of each of the warning and critical monitors that are currently active

</dd> <dt>

**ErrorDesc**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Detail description of each of the warning and critical monitors that are currently active

</dd> <dt>

**ErrorResoln**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the resolution of each of the warning and critical monitors that are currently active

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique Id describing a monitor

</dd> <dt>

**OperationStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Operation Status of the monitor

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status of the monitor

The possible values are.

<dt>

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

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





