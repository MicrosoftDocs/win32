---
description: Attempts to send a user-defined control code to a service.
ms.assetid: d181dbf8-e1ad-47b2-9e64-4aabc77e64bd
ms.tgt_platform: multiple
title: UserControlService method of the Win32_BaseService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_BaseService.UserControlService
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# UserControlService method of the Win32\_BaseService class

The [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method attempts to send a user-defined control code to a service.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 UserControlService(
  [in] uint8 ControlCode
);
```



## Parameters

<dl> <dt>

*ControlCode* \[in\]
</dt> <dd>

Value that specifies a control command to a service. For example a control command is a "pause" or "continue" command. The value can be a predefined code, or a value and action that the service defines. The following are the predefined control codes:

<dt>

<span id="SERVICE_CONTROL_CONTINUE"></span><span id="service_control_continue"></span>

<span id="SERVICE_CONTROL_CONTINUE"></span><span id="service_control_continue"></span>**SERVICE\_CONTROL\_CONTINUE**


</dt> <dd>

Notifies a paused service to resume.

</dd> <dt>

<span id="SERVICE_CONTROL_INTERROGATE"></span><span id="service_control_interrogate"></span>

<span id="SERVICE_CONTROL_INTERROGATE"></span><span id="service_control_interrogate"></span>**SERVICE\_CONTROL\_INTERROGATE**


</dt> <dd>

Notifies a service to report the current status information to the service control manager.

</dd> <dt>

<span id="SERVICE_CONTROL_NETBINDADD"></span><span id="service_control_netbindadd"></span>

<span id="SERVICE_CONTROL_NETBINDADD"></span><span id="service_control_netbindadd"></span>**SERVICE\_CONTROL\_NETBINDADD**


</dt> <dd>

Notifies a network service that there is a new component for binding.

</dd> <dt>

<span id="SERVICE_CONTROL_NETBINDDISABLE"></span><span id="service_control_netbinddisable"></span>

<span id="SERVICE_CONTROL_NETBINDDISABLE"></span><span id="service_control_netbinddisable"></span>**SERVICE\_CONTROL\_NETBINDDISABLE**


</dt> <dd>

Notifies a network service that one of its bindings is disabled.

</dd> <dt>

<span id="SERVICE_CONTROL_NETBINDENABLE"></span><span id="service_control_netbindenable"></span>

<span id="SERVICE_CONTROL_NETBINDENABLE"></span><span id="service_control_netbindenable"></span>**SERVICE\_CONTROL\_NETBINDENABLE**


</dt> <dd>

Notifies a network service that a disabled binding is enabled.

</dd> <dt>

<span id="SERVICE_CONTROL_NETBINDREMOVE"></span><span id="service_control_netbindremove"></span>

<span id="SERVICE_CONTROL_NETBINDREMOVE"></span><span id="service_control_netbindremove"></span>**SERVICE\_CONTROL\_NETBINDREMOVE**


</dt> <dd>

Notifies a network service that a component for binding has been removed.

</dd> <dt>

<span id="SERVICE_CONTROL_PARAMCHANGE"></span><span id="service_control_paramchange"></span>

<span id="SERVICE_CONTROL_PARAMCHANGE"></span><span id="service_control_paramchange"></span>**SERVICE\_CONTROL\_PARAMCHANGE**


</dt> <dd>

Notifies a service that its startup parameters are changed.

</dd> <dt>

<span id="SERVICE_CONTROL_PAUSE"></span><span id="service_control_pause"></span>

<span id="SERVICE_CONTROL_PAUSE"></span><span id="service_control_pause"></span>**SERVICE\_CONTROL\_PAUSE**


</dt> <dd>

Notifies a service to pause.

</dd> <dt>

<span id="SERVICE_CONTROL_STOP"></span><span id="service_control_stop"></span>

<span id="SERVICE_CONTROL_STOP"></span><span id="service_control_stop"></span>**SERVICE\_CONTROL\_STOP**


</dt> <dd>

Notifies a service to stop.

</dd> </dl> </dd> </dl>

## Return value

Returns one of the values listed in the following list, or a different value to indicate an error.

<dl> <dt>

**Success**
</dt> <dd>

0

The request is accepted.

</dd> <dt>

**Not Supported**
</dt> <dd>

1

The request is not supported.

</dd> <dt>

**Access Denied**
</dt> <dd>

2

The user does not have the necessary access rights.

</dd> <dt>

**Dependent Services Running**
</dt> <dd>

3

The service cannot be stopped because other services that are running are dependent on it.

</dd> <dt>

**Invalid Service Control**
</dt> <dd>

4

The requested control code is not valid, or it is unacceptable to the service.

</dd> <dt>

**Service Cannot Accept Control**
</dt> <dd>

5

The requested control code cannot be sent to the service because the state of the service ([**Win32\_BaseService**](win32-baseservice.md).**State** property) is equal to 0, 1, or 2.

</dd> <dt>

**Service Not Active**
</dt> <dd>

6

The service has not started.

</dd> <dt>

**Service Request Timeout**
</dt> <dd>

7

The service does not respond to the start request quickly.

</dd> <dt>

**Unknown Failure**
</dt> <dd>

8

Interactive process.

</dd> <dt>

**Path Not Found**
</dt> <dd>

9

The directory path to the service executable file is not found.

</dd> <dt>

**Service Already Running**
</dt> <dd>

10

The service is already running.

</dd> <dt>

**Service Database Locked**
</dt> <dd>

11

The database to add a new service is locked.

</dd> <dt>

**Service Dependency Deleted**
</dt> <dd>

12

A dependency that this service relies on is removed from the system.

</dd> <dt>

**Service Dependency Failure**
</dt> <dd>

13

The service does not find the service needed from a dependent service.

</dd> <dt>

**Service Disabled**
</dt> <dd>

14

The service is disabled from the system.

</dd> <dt>

**Service Logon Failed**
</dt> <dd>

15

The service does not have the correct authentication to run on the system.

</dd> <dt>

**Service Marked For Deletion**
</dt> <dd>

16

The service is being removed from the system.

</dd> <dt>

**Service No Thread**
</dt> <dd>

17

There is no execution thread for the service.

</dd> <dt>

**Status Circular Dependency**
</dt> <dd>

18

There are circular dependencies when starting the service.

</dd> <dt>

**Status Duplicate Name**
</dt> <dd>

19

There is a service running under the same name.

</dd> <dt>

**Status Invalid Name**
</dt> <dd>

20

There are invalid characters in the name of the service.

</dd> <dt>

**Status Invalid Parameter**
</dt> <dd>

21

Invalid parameters have passed to the service.

</dd> <dt>

**Status Invalid Service Account**
</dt> <dd>

22

The account that this service runs under is not valid or does not have the permissions to run the service.

</dd> <dt>

**Status Service Exists**
</dt> <dd>

23

The service exists in the database of services available from the system.

</dd> <dt>

**Service Already Paused**
</dt> <dd>

24

The service is currently paused in the system.

</dd> <dt>

**Other**
</dt> <dd>

25 4294967295

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Win32\_BaseService**](win32-baseservice.md)
</dt> </dl>

 

