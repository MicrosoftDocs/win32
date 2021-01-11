---
description: Modifies a Win32\_SystemDriver service.
ms.assetid: 61ee3297-2a66-466e-bdba-74d683f3ea70
ms.tgt_platform: multiple
title: Change method of the Win32_SystemDriver class (Mbnapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemDriver.Change
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Change method of the Win32\_SystemDriver class

The **Change** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method modifies a [**Win32\_SystemDriver**](win32-systemdriver.md) service. The [**Win32\_LoadOrderGroup**](win32-loadordergroup.md) parameter represents a grouping of system services defining execution dependencies. The services must be initiated in the order specified by the Load Order Group as the services are dependent on each other. These dependent services require the presence of the antecedent services to function correctly.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Change(
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

*DisplayName* \[in\]
</dt> <dd>

The display name of the service. This string has a maximum length of 256 characters. The name is case-preserved in the service control manager. *DisplayName* comparisons are always case-insensitive.

Constraints: Accepts the same value as the *Name* parameter.

Example: "Atdisk"

</dd> <dt>

*PathName* \[in\]
</dt> <dd>

The fully qualified path to the executable file that implements the service.

Example: *\\SystemRoot\\System32\\drivers\\afd.sys*

</dd> <dt>

*ServiceType* \[in\]
</dt> <dd>

Type of services provided to the processes that call them.

<dt>

1 (0x1)
</dt> <dd>

Kernel Driver

</dd> <dt>

2 (0x2)
</dt> <dd>

File System Driver

</dd> <dt>

4 (0x4)
</dt> <dd>

Adapter

</dd> <dt>

8 (0x8)
</dt> <dd>

Recognizer Driver

</dd> <dt>

16 (0x10)
</dt> <dd>

Own Process

</dd> <dt>

32 (0x20)
</dt> <dd>

Share Process

</dd> <dt>

256 (0x100)
</dt> <dd>

Interactive Process

</dd> </dl> </dd> <dt>

*ErrorControl* \[in\]
</dt> <dd>

The severity of the error if this service fails to start during startup. The value indicates the action taken by the startup program if failure occurs. All errors are logged by the system.

<dt>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>**Ignore** (0)


</dt> <dd>

User is not notified.

</dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>**Normal** (1)


</dt> <dd>

Normal. User is notified.

</dd> <dt>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>**Severe** (2)


</dt> <dd>

System is restarted with the last good configuration.

</dd> <dt>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>**Critical** (3)


</dt> <dd>

System attempts to restart with a good configuration.

</dd> </dl> </dd> <dt>

*StartMode* \[in\]
</dt> <dd>

The start mode of the Windows base service.

<dt>

<span id="Boot_Start"></span><span id="boot_start"></span><span id="BOOT_START"></span>

<span id="Boot_Start"></span><span id="boot_start"></span><span id="BOOT_START"></span>**Boot Start**


</dt> <dd>

Device driver started by the operating system loader.

</dd> <dt>

<span id="Boot_Start"></span><span id="boot_start"></span><span id="BOOT_START"></span>

<span id="Boot_Start"></span><span id="boot_start"></span><span id="BOOT_START"></span>**Boot Start**


</dt> <dd>

Device driver that the operating system loader starts.

</dd> <dt>

<span id="System_Start"></span><span id="system_start"></span><span id="SYSTEM_START"></span>

<span id="System_Start"></span><span id="system_start"></span><span id="SYSTEM_START"></span>**System Start**


</dt> <dd>

Device driver started by the operating system initialization process. This value is valid only for driver services.

</dd> <dt>

<span id="Auto_Start"></span><span id="auto_start"></span><span id="AUTO_START"></span>

<span id="Auto_Start"></span><span id="auto_start"></span><span id="AUTO_START"></span>**Auto Start**


</dt> <dd>

Service to start automatically by the service control manager during system startup.

</dd> <dt>

<span id="Demand_Start"></span><span id="demand_start"></span><span id="DEMAND_START"></span>

<span id="Demand_Start"></span><span id="demand_start"></span><span id="DEMAND_START"></span>**Demand Start**


</dt> <dd>

Service to start by the service control manager when a process calls the [**StartService**](startservice-method-in-class-win32-systemdriver.md) method.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled**


</dt> <dd>

Service that cannot be started.

</dd> </dl> </dd> <dt>

*DesktopInteract* \[in\]
</dt> <dd>

A value that, if **True**, the service can create or communicate with the windows on the desktop.

</dd> <dt>

*StartName* \[in\]
</dt> <dd>

The account name the service runs under. Depending on the service type, the account name may be in the form of DomainName\\Username or .\\Username. When it runs, the service process is logged using one of these two forms. If the account belongs to the built-in domain, .\\Username can be specified. If an empty string is specified, the service is logged on as the LocalSystem account. For kernel or system-level drivers, *StartName* contains the driver object name, for example, \\FileSystem\\Rdr or \\Driver\\Xns), which the input and output (I/O) system uses to load the device driver. If **NULL** is specified, the driver runs with a default object name that the I/O system creates based on the service name, for example, DWDOM\\Admin.

You also can use the User Principal Name (UPN) format to specify the **StartName**, for example, *Username@DomainName*.

</dd> <dt>

*StartPassword* \[in\]
</dt> <dd>

The password to the account name specified by the *StartName* parameter. Specify **NULL** if you are not changing the password. Specify an empty string if the service has no password.

> [!Note]  
> When changing a service from a local system to a network, or from a network to a local system, *StartPassword* must be an empty string ("") and not **NULL**.

 

</dd> <dt>

*LoadOrderGroup* \[in\]
</dt> <dd>

The group name that it is associated with. Load order groups are contained in the system registry, and determine the sequence in which services are loaded into the operating system. If the pointer is **NULL**, or if it points to an empty string, the service does not belong to a group. Dependencies between groups should be listed in the *LoadOrderGroupDependencies* parameter. Services in the load-ordering group list are started first, followed by services in groups not in the load-ordering group list, followed by services that do not belong to a group. The system registry has a list of load ordering groups located at:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**ServiceGroupOrder**

</dd> <dt>

*LoadOrderGroupDependencies* \[in\]
</dt> <dd>

The list of load-ordering groups that must start before this service starts. The array is doubly **null**-terminated. If the pointer is **NULL**, or if it points to an empty string, the service has no dependencies. Group names must be prefixed by the **SC\_GROUP\_IDENTIFIER** (defined in the WinSvc.h file) character to differentiate them from service names, because services and service groups share the same namespace. Dependency on a group means that this service can run if at least one member of the group is running after an attempt to start all of the members of the group.

</dd> <dt>

*ServiceDependencies* \[in\]
</dt> <dd>

The list that contains the names of the services that must start before this service starts. The array is doubly **null**-terminated. If the pointer is **NULL**, or if it points to an empty string, the service has no dependencies. Dependency on a service means that this service can run only if the service it depends on is running.

</dd> </dl>

## Return value

Returns a value of zero (0) if the service was successfully modified, 1 (one) if the request is not supported, and any other number to indicate an error.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Access Denied** (2)
</dt> <dt>

**Dependent Services Running** (3)
</dt> <dt>

**Invalid Service Control** (4)
</dt> <dt>

**Service Cannot Accept Control** (5)
</dt> <dt>

**Service Not Active** (6)
</dt> <dt>

**Service Request Timeout** (7)
</dt> <dt>

**Unknown Failure** (8)
</dt> <dt>

**Path Not Found** (9)
</dt> <dt>

**Service Already Running** (10)
</dt> <dt>

**Service Database Locked** (11)
</dt> <dt>

**Service Dependency Deleted** (12)
</dt> <dt>

**Service Dependency Failure** (13)
</dt> <dt>

**Service Disabled** (14)
</dt> <dt>

**Service Logon Failed** (15)
</dt> <dt>

**Service Marked For Deletion** (16)
</dt> <dt>

**Service No Thread** (17)
</dt> <dt>

**Status Circular Dependency** (18)
</dt> <dt>

**Status Duplicate Name** (19)
</dt> <dt>

**Status Invalid Name** (20)
</dt> <dt>

**Status Invalid Parameter** (21)
</dt> <dt>

**Status Invalid Service Account** (22)
</dt> <dt>

**Status Service Exists** (23)
</dt> <dt>

**Service Already Paused** (24)
</dt> <dt>

**Other** (25 4294967295)
</dt> </dl>

## Remarks

To change a service from a network service to the local system, use the following values for the *StartName* and *StartPassword* parameters:


```C++
StartName = "LocalSystem"
StartPassword = "" // - empty string, not NULL
```



To change a service from a local system service to network service, use the following values for the *StartName* and *StartPassword* parameters:


```C++
StartName = "NT AUTHORITY\NetworkService"
StartPassword = "" // - empty string, not NULL
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Mbnapi.h</dt> </dl>     |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Win32\_SystemDriver**](win32-systemdriver.md)
</dt> </dl>

 

