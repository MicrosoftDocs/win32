---
description: Creates a new service.
ms.assetid: e000b896-3b49-4650-b706-548592cfe721
ms.tgt_platform: multiple
title: Create method of the Win32_BaseService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_BaseService.Create
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Create method of the Win32\_BaseService class

The **Create** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method creates a new service. The *LoadOrderGroup* parameter represents a grouping of system services defining execution dependencies. The services must be initiated in the order specified by the Load Order Group, as the services are dependent on each other. These dependent services require the presence of the antecedent services to function correctly.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Create(
  [in] string  Name,
  [in] string  DisplayName,
  [in] string  PathName,
  [in] uint8   ServiceType,
  [in] uint8   ErrorControl,
  [in] string  StartMode,
  [in] boolean DesktopInteract,
  [in] string  StartName,
  [in] string  StartPassword,
  [in] string  LoadOrderGroup,
  [in] string  LoadOrderGroupDependencies[],
  [in] string  ServiceDependencies[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the service to install to the **Create** method. The maximum string length is 256 characters. The service control manager database preserves the case of the characters, but service name comparisons are always case-insensitive. Forward-slashes (/) and double back-slashes (\\) are invalid service name characters.

</dd> <dt>

*DisplayName* \[in\]
</dt> <dd>

Display name of the service. This string has a maximum length of 256 characters. The name is case-preserved in the service control manager. *DisplayName* comparisons are always case-insensitive.

Constraints: Accepts the same value as the *Name* parameter.

Example: "Atdisk".

</dd> <dt>

*PathName* \[in\]
</dt> <dd>

Fully qualified path to the executable file that implements the service.

Example: "\\SystemRoot\\System32\\drivers\\afd.sys".

</dd> <dt>

*ServiceType* \[in\]
</dt> <dd>

Type of services provided to processes that call them. The value is a bitmap.

<dt>

<span id="Kernel_Driver"></span><span id="kernel_driver"></span><span id="KERNEL_DRIVER"></span>

<span id="Kernel_Driver"></span><span id="kernel_driver"></span><span id="KERNEL_DRIVER"></span>**Kernel Driver** (1)


</dt> <dd></dd> <dt>

<span id="File_System_Driver"></span><span id="file_system_driver"></span><span id="FILE_SYSTEM_DRIVER"></span>

<span id="File_System_Driver"></span><span id="file_system_driver"></span><span id="FILE_SYSTEM_DRIVER"></span>**File System Driver** (2)


</dt> <dd></dd> <dt>

<span id="Adapter"></span><span id="adapter"></span><span id="ADAPTER"></span>

<span id="Adapter"></span><span id="adapter"></span><span id="ADAPTER"></span>**Adapter** (4)


</dt> <dd></dd> <dt>

<span id="Recognizer_Driver"></span><span id="recognizer_driver"></span><span id="RECOGNIZER_DRIVER"></span>

<span id="Recognizer_Driver"></span><span id="recognizer_driver"></span><span id="RECOGNIZER_DRIVER"></span>**Recognizer Driver** (8)


</dt> <dd></dd> <dt>

<span id="Own_Process"></span><span id="own_process"></span><span id="OWN_PROCESS"></span>

<span id="Own_Process"></span><span id="own_process"></span><span id="OWN_PROCESS"></span>**Own Process** (16)


</dt> <dd></dd> <dt>

<span id="Share_Process"></span><span id="share_process"></span><span id="SHARE_PROCESS"></span>

<span id="Share_Process"></span><span id="share_process"></span><span id="SHARE_PROCESS"></span>**Share Process** (32)


</dt> <dd></dd> <dt>

256
</dt> <dd>

Interactive Process

</dd> <dt>




</dt> <dd></dd> </dl> </dd> <dt>

*ErrorControl* \[in\]
</dt> <dd>

Severity of the error if the **Create** method fails to start. The value indicates the action taken by the startup program if failure occurs. All errors are logged by the system.

<dt>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>**Ignore** (0)


</dt> <dd>

User is not notified.

</dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>**Normal** (1)


</dt> <dd>

User is notified.

</dd> <dt>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>**Severe** (2)


</dt> <dd>

System is restarted with the last-known-good configuration.

</dd> <dt>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>**Critical** (3)


</dt> <dd>

System attempts to start with a good configuration.

</dd> </dl> </dd> <dt>

*StartMode* \[in\]
</dt> <dd>

Start mode of the Windows base service.

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

Service to be started by the service control manager when a process calls the [**StartService**](startservice-method-in-class-win32-service.md) method.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** ("Disabled")


</dt> <dd>

Service that can no longer be started.

</dd> </dl> </dd> <dt>

*DesktopInteract* \[in\]
</dt> <dd>

If **true**, the service can create or communicate with windows on the desktop.

</dd> <dt>

*StartName* \[in\]
</dt> <dd>

Account name under which the service runs. Depending on the service type, the account name may be in the form of "DomainName\\Username". The service process is logged using one of these two forms when it runs. If the account belongs to the built-in domain, ".\\Username" can be specified. If **NULL** is specified, the service is logged on as the LocalSystem account. For a kernel or system-level drivers, *StartName* contains the driver object name (that is, \\FileSystem\\Rdr or \\Driver\\Xns) that the input and output (I/O) system uses to load the device driver. If **NULL** is specified, the driver runs with a default object name created by the I/O system based on the service name. Example: DWDOM\\Admin.

</dd> <dt>

*StartPassword* \[in\]
</dt> <dd>

Password to the account name specified by the *StartName* parameter. Specify **NULL** if you are not changing the password. Specify an empty string if the service has no password.

</dd> <dt>

*LoadOrderGroup* \[in\]
</dt> <dd>

Group name associated with the new service. Load order groups are contained in the registry, and determine the sequence in which services are loaded into the operating system. If the pointer is **NULL** or if it points to an empty string, the service does not belong to a group. Dependencies between groups should be listed in the *LoadOrderGroupDependencies* parameter. Services in the load-ordering group list are started first, followed by services in groups not in the load-ordering group list, followed by services that do not belong to a group. The registry has a list of load ordering groups located at:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**ServiceGroupOrder**

</dd> <dt>

*LoadOrderGroupDependencies* \[in\]
</dt> <dd>

Array of load-ordering groups that must start before this service. Each item in the array is delimited by **NULL** and the list is terminated by two **NULL** values. In Visual Basic or script you can pass a vbArray. If the pointer is **NULL** or if it points to an empty string, the service has no dependencies. Group names must be prefixed by the SC\_GROUP\_IDENTIFIER (defined in the Winsvc.h file) character to differentiate it from a service name, because services and service groups share the same namespace. Dependency on a group means that this service can run if at least one member of the group is running after an attempt to start all members of the group.

</dd> <dt>

*ServiceDependencies* \[in\]
</dt> <dd>

Array that contains names of services that must start before this service starts. Each item in the array is delimited by **NULL** and the list is terminated by two **NULL** values. In Visual Basic or script you can pass a vbArray. If the pointer is **NULL**, or if it points to an empty string, the service has no dependencies. Dependency on a service means that this service can only run if the service it depends on is running.

</dd> </dl>

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

The requested control code cannot be sent to the service because the state of the service ([**Win32\_BaseService**](win32-baseservice.md).**State** property) is equal to 0, 1, or 2.

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

 

