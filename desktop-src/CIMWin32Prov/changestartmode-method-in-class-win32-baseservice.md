---
description: Modifies the start mode of a service object derived from Win32\_BaseService.
ms.assetid: 33040632-6c04-4084-af09-8e1b8bc29090
ms.tgt_platform: multiple
title: ChangeStartMode method of the Win32_BaseService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_BaseService.ChangeStartMode
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# ChangeStartMode method of the Win32\_BaseService class

The **ChangeStartMode** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method modifies the start mode of a service object derived from [**Win32\_BaseService**](win32-baseservice.md).

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 ChangeStartMode(
  [in] string StartMode = Auto Start
);
```



## Parameters

<dl> <dt>

*StartMode* \[in\]
</dt> <dd>

Start mode of the Windows base service. The default is "Automatic".

<dt>

<span id="Boot_Start"></span><span id="boot_start"></span><span id="BOOT_START"></span>

<span id="Boot_Start"></span><span id="boot_start"></span><span id="BOOT_START"></span>**Boot Start** ("Boot")


</dt> <dd>

Device driver started by the operating system loader. This value is valid only for driver services.

</dd> <dt>

<span id="System_Start"></span><span id="system_start"></span><span id="SYSTEM_START"></span>

<span id="System_Start"></span><span id="system_start"></span><span id="SYSTEM_START"></span>**System Start** ("System")


</dt> <dd>

Device driver started by the operating system initialization process. This value is valid only for driver services.

</dd> <dt>

<span id="Auto_Start"></span><span id="auto_start"></span><span id="AUTO_START"></span>

<span id="Auto_Start"></span><span id="auto_start"></span><span id="AUTO_START"></span>**Auto Start** ("Automatic")


</dt> <dd>

Service to be started automatically by the service control manager during system startup.

</dd> <dt>

<span id="Demand_Start"></span><span id="demand_start"></span><span id="DEMAND_START"></span>

<span id="Demand_Start"></span><span id="demand_start"></span><span id="DEMAND_START"></span>**Demand Start** ("Manual")


</dt> <dd>

Service to be started by the service control manager when a process calls the [**StartService**](startservice-method-in-class-win32-baseservice.md) method.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** ("Disabled")


</dt> <dd>

Service is disabled.

</dd> </dl> </dd> </dl>

## Return value

Returns one of the values listed in the following list or any other value to indicate an error.

<dl> <dt>

**Success**
</dt> <dd>

0

The request was accepted.

</dd> <dt>

**Not Supported**
</dt> <dd>

1

The request is not supported.

</dd> <dt>

**Access Denied**
</dt> <dd>

2

The user did not have the necessary access.

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

The requested control code cannot be sent to the service because the state of the service ([**Win32\_BaseService**](win32-baseservice.md)[**State**](win32-baseservice.md) property) is equal to 0, 1, or 2.

</dd> <dt>

**Service Not Active**
</dt> <dd>

6

The service has not been started.

</dd> <dt>

**Service Request Timeout**
</dt> <dd>

7

The service did not respond to the start request in a timely fashion.

</dd> <dt>

**Unknown Failure**
</dt> <dd>

8

Interactive process.

</dd> <dt>

**Path Not Found**
</dt> <dd>

9

The directory path to the service executable file was not found.

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

A dependency on which this service relies has been removed from the system.

</dd> <dt>

**Service Dependency Failure**
</dt> <dd>

13

The service failed to find the service needed from a dependent service.

</dd> <dt>

**Service Disabled**
</dt> <dd>

14

The service has been disabled from the system.

</dd> <dt>

**Service Logon Failed**
</dt> <dd>

15

The service does not have the correct authentication to run on the system.

</dd> <dt>

**Service Marked For Deletion**
</dt> <dd>

16

This service is being removed from the system.

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

Invalid parameters have been passed to the service.

</dd> <dt>

**Status Invalid Service Account**
</dt> <dd>

22

The account which this service is to run under is either invalid or lacks the permissions to run the service.

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

 

