---
title: Create method of the Win32_Service class (Remote Desktop Services)
description: Create method of the Win32_Service class (Remote Desktop Services) - Creates a new system service.
ms.assetid: 805754AA-B62A-4324-B289-503C42BEFA49
ms.tgt_platform: multiple
keywords:
- Create method Remote Desktop Services
- Create method Remote Desktop Services , Win32_Service class
- Win32_Service class Remote Desktop Services , Create method
topic_type:
- apiref
api_name:
- Win32_Service.Create
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Create method of the Win32_Service class (Remote Desktop Services)

The **Create** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method creates a new system service.

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

Type of services provided to processes that call them.

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

Severity of the error if the **Create** method fails to start. The value indicates the action taken by the startup program if failure occurs. All errors are logged by the system.

<dt>

0
</dt> <dd>

User is not notified.

</dd> <dt>

1
</dt> <dd>

User is notified.

</dd> <dt>

2
</dt> <dd>

System is restarted with the last-known-good configuration.

</dd> <dt>

3
</dt> <dd>

System attempts to start with a good configuration.

</dd> </dl> </dd> <dt>

*StartMode* \[in\]
</dt> <dd>

Start mode of the Windows base service.

<dt>

Boot
</dt> <dd>

Device driver started by the operating system loader. This value is valid only for driver services.

</dd> <dt>

System
</dt> <dd>

Device driver started by the operating system initialization process. This value is valid only for driver services.

</dd> <dt>

Automatic
</dt> <dd>

Service to be started automatically by the Service Control Manager during system startup.

</dd> <dt>

Manual
</dt> <dd>

Service to be started by the Service Control Manager when a process calls the [**StartService**](win32-terminalservice-startservice.md) method.

</dd> <dt>

Disabled
</dt> <dd>

Service that can no longer be started.

</dd> </dl> </dd> <dt>

*DesktopInteract* \[in\]
</dt> <dd>

If **true**, the service can create or communicate with windows on the desktop.

</dd> <dt>

*StartName* \[in\]
</dt> <dd>

Account name under which the service runs. Depending on the service type, the account name may be in the form of DomainName\\Username or User Principal Name (UPN) format (Username@DomainName). The service process is logged using one of these two forms when it runs. If the account belongs to the built-in domain, .\\Username can be specified. If **NULL** is specified, the service is logged on as the LocalSystem account. For a kernel or system-level drivers, *StartName* contains the driver object name (that is, \\FileSystem\\Rdr or \\Driver\\Xns) which the input and output (I/O) system uses to load the device driver. If **NULL** is specified, the driver runs with a default object name created by the I/O system based on the service name. Example: DWDOM\\Admin.

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

Array of load-ordering groups that must start before this service. Each item in the array is delimited by **NULL** and the list is terminated by two **NULL** values. In Visual Basic or script you can pass a vbArray. If the pointer is **NULL** or if it points to an empty string, the service has no dependencies. Group names must be prefixed by the **SC\_GROUP\_IDENTIFIER** (defined in the Winsvc.h file) character to differentiate it from a service name, because services and service groups share the same namespace. Dependency on a group means that this service can run if at least one member of the group is running after an attempt to start all of the members of the group.

</dd> <dt>

*ServiceDependencies* \[in\]
</dt> <dd>

Array that contains names of services that must start before this service starts. Each item in the array is delimited by **NULL** and the list is terminated by two **NULL** values. In Visual Basic or script you can pass a vbArray. If the pointer is **NULL**, or if it points to an empty string, the service has no dependencies. Dependency on a service means that this service can only run if the service it depends on is running.

</dd> </dl>

## Return value

Returns one of the values listed in the following list or any other value to indicate an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**0**
</dt> <dd>

The request was accepted.

</dd> <dt>

**1**
</dt> <dd>

The request is not supported.

</dd> <dt>

**2**
</dt> <dd>

The user did not have the necessary access.

</dd> <dt>

**3**
</dt> <dd>

The service cannot be stopped because other services that are running are dependent on it.

</dd> <dt>

**4**
</dt> <dd>

The requested control code is not valid, or it is unacceptable to the service.

</dd> <dt>

**5**
</dt> <dd>

The requested control code cannot be sent to the service because the state of the service (**State** property of the [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice) class) is equal to 0, 1, or 2.

</dd> <dt>

**6**
</dt> <dd>

The service has not been started.

</dd> <dt>

**7**
</dt> <dd>

The service did not respond to the start request in a timely fashion.

</dd> <dt>

**8**
</dt> <dd>

Unknown failure when starting the service.

</dd> <dt>

**9**
</dt> <dd>

The directory path to the service executable file was not found.

</dd> <dt>

**10**
</dt> <dd>

The service is already running.

</dd> <dt>

**11**
</dt> <dd>

The database to add a new service is locked.

</dd> <dt>

**12**
</dt> <dd>

A dependency this service relies on has been removed from the system.

</dd> <dt>

**13**
</dt> <dd>

The service failed to find the service needed from a dependent service.

</dd> <dt>

**14**
</dt> <dd>

The service has been disabled from the system.

</dd> <dt>

**15**
</dt> <dd>

The service does not have the correct authentication to run on the system.

</dd> <dt>

**16**
</dt> <dd>

This service is being removed from the system.

</dd> <dt>

**17**
</dt> <dd>

The service has no execution thread.

</dd> <dt>

**18**
</dt> <dd>

The service has circular dependencies when it starts.

</dd> <dt>

**19**
</dt> <dd>

A service is running under the same name.

</dd> <dt>

**20**
</dt> <dd>

The service name has invalid characters.

</dd> <dt>

**21**
</dt> <dd>

Invalid parameters have been passed to the service.

</dd> <dt>

**22**
</dt> <dd>

The account under which this service runs is either invalid or lacks the permissions to run the service.

</dd> <dt>

**23**
</dt> <dd>

The service exists in the database of services available from the system.

</dd> <dt>

**24**
</dt> <dd>

The service is currently paused in the system.

</dd> </dl>

## Remarks

Services are generally installed in one of two ways: either as a part of the operating system installation or by using an installation program provided by the service developer. However, some services, particularly those created in-house, might not have an installation program. In those instances, you can use the **Create** method to programmatically install services.

Despite the name, the Create method does not actually create a service; it merely installs an existing service. To use this command, you need to copy the service executable file to a computer and then use **Create** to install the service.

The **Create** method is similar to the [**Change**](win32-terminalservice-change.md) method. In both cases, the properties of the service are passed as parameters to the method. As with the parameters used with the **Change** method, the order in which these parameters are passed is very important.

The *LoadOrderGroup* parameter represents a grouping of system services defining execution dependencies. The services must be initiated in the order specified by the Load Order Group, as the services are dependent on each other. These dependent services require the presence of the antecedent services to function correctly.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service)
</dt> <dt>

[Operating System Classes](/windows/desktop/CIMWin32Prov/operating-system-classes)
</dt> <dt>

[**Win32\_TerminalService**](win32-terminalservice.md)
</dt> <dt>

[WMI Tasks: Services](/windows/desktop/WmiSdk/wmi-tasks--services)
</dt> </dl>

 

