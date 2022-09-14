---
description: Creates a new service managed by the system driver.
ms.assetid: 212c88eb-f26d-4b07-b8fe-8508050c97fc
ms.tgt_platform: multiple
title: Create method of the Win32_SystemDriver class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemDriver.Create
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Create method of the Win32\_SystemDriver class

The **Create** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method creates a new service managed by the system driver. The *Win32\_LoadOrderGroup* parameter represents a grouping of system services defining execution dependencies. The services must be initiated in the order specified by the Load Order Group, as the services are dependent on each other. These dependent services require the presence of the antecedent services to function correctly.

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

Name of the service to install to the **Create** method. The maximum string length is 256 characters. The Service Control Manager database preserves the case of the characters, but service name comparisons are always case-insensitive. Forward-slashes (/) and double back-slashes (\\) are invalid service name characters.

</dd> <dt>

*DisplayName* \[in\]
</dt> <dd>

Display name of the service. This string has a maximum length of 256 characters. The name is case-preserved in the Service Control Manager. *DisplayName* comparisons are always case-insensitive.

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

Severity of the error if the **Create** method fails to start. This value indicates the action taken by the startup program if failure occurs. All errors are logged by the system.

<dt>

0
</dt> <dd>

"Ignore"

User is not notified.

</dd> <dt>

1
</dt> <dd>

"Normal"

User is notified.

</dd> <dt>

2
</dt> <dd>

"Severe"

System is restarted with the last-known-good configuration.

</dd> <dt>

3
</dt> <dd>

"Critical"

System attempts to start with a good configuration.

</dd> </dl> </dd> <dt>

*StartMode* \[in\]
</dt> <dd>

Start mode of the Windows base service.

<dt>

<span id="Boot"></span><span id="boot"></span><span id="BOOT"></span>

<span id="Boot"></span><span id="boot"></span><span id="BOOT"></span>**Boot**


</dt> <dd>

Device driver started by the operating system loader. This value is valid only for driver services.

</dd> <dt>

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>**System**


</dt> <dd>

Device driver started by the operating system initialization process. This value is valid only for driver services.

</dd> <dt>

<span id="Automatic"></span><span id="automatic"></span><span id="AUTOMATIC"></span>

<span id="Automatic"></span><span id="automatic"></span><span id="AUTOMATIC"></span>**Automatic**


</dt> <dd>

Service to be started automatically by the Service Control Manager during system startup.

</dd> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>**Manual**


</dt> <dd>

Service to be started by the Service Control Manager when a process calls the [**StartService**](startservice-method-in-class-win32-systemdriver.md) method.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled**


</dt> <dd>

Service that can no longer be started.

</dd> </dl> </dd> <dt>

*DesktopInteract* \[in\]
</dt> <dd>

If **true**, the service can create or communicate with the windows on the desktop.

</dd> <dt>

*StartName* \[in\]
</dt> <dd>

Account name under which the service runs. Depending on the service type, the account name may be in the form of DomainName\\Username or User Principal Name (UPN) format (Username@DomainName). The service process is logged using one of these two forms when it runs. If the account belongs to the built-in domain, .\\Username can be specified. If **NULL** is specified, the service is logged on as the LocalSystem account. For a kernel or system-level drivers, *StartName* contains the driver object name (that is, \\FileSystem\\Rdr or \\Driver\\Xns) that the input and output (I/O) system uses to load the device driver. If **NULL** is specified, the driver runs with a default object name created by the I/O system based on the service name.

Example: DWDOM\\Admin

</dd> <dt>

*StartPassword* \[in\]
</dt> <dd>

Password to the account name specified by the *StartName* parameter. Specify **NULL** if you are not changing the password. Specify an empty string if the service has no password.

</dd> <dt>

*LoadOrderGroup* \[in\]
</dt> <dd>

Group name associated with the new service. Load order groups are contained in the registry and determine the sequence in which services are loaded into the operating system. If the pointer is **NULL** or if it points to an empty string, the service does not belong to a group. Dependencies between groups should be listed in the *LoadOrderGroupDependencies* parameter. Services in the load-ordering group list are started first, followed by services in groups not in the load-ordering group list, followed by services that do not belong to a group. The registry has a list of load ordering groups located at:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**ServiceGroupOrder**

</dd> <dt>

*LoadOrderGroupDependencies* \[in\]
</dt> <dd>

Array of load-ordering groups that must start before this service. Each item in the array is delimited by **NULL** and the list is terminated by two **NULL** values. In Visual Basic or script you can pass a vbArray. If the pointer is **NULL** or if it points to an empty string, the service has no dependencies. Group names must be prefixed by the **SC\_GROUP\_IDENTIFIER** (defined in the Winsvc.h file) character to differentiate it from a service name, because services and service groups share the same namespace. Dependency on a group means that this service can run if at least one member of the group is running after an attempt to start all of the members of the group.

</dd> <dt>

*ServiceDependencies* \[in\]
</dt> <dd>

An array that contains the names of services that must start before this service starts. Each item in the array is delimited by **NULL** and the list is terminated by two **NULL** values. In Visual Basic or script you can pass a vbArray. If the pointer is **NULL**, or if it points to an empty string, the service has no dependencies. Dependency on a service means that this service can only run if the service it depends on is running.

</dd> </dl>

## Return value

Returns a value of 0 (zero) if the service was successfully created, 1 (one) if the request is not supported, and any other number to indicate an error.

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

[**Win32\_SystemDriver**](win32-systemdriver.md)
</dt> </dl>

 

