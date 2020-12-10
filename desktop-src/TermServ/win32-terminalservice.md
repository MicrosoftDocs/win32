---
title: Win32_TerminalService class
description: A subclass of the Win32\_Service class. Win32\_TerminalService represents the Element property of the Win32\_TerminalServiceToSetting association.
ms.assetid: 06c69d71-4e6f-48af-b13d-e593b8fcf376
ms.tgt_platform: multiple
keywords:
- Win32_TerminalService class Remote Desktop Services
- Win32_TerminalService class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TerminalService
- Win32_TerminalService.AcceptPause
- Win32_TerminalService.AcceptStop
- Win32_TerminalService.Caption
- Win32_TerminalService.CheckPoint
- Win32_TerminalService.CreationClassName
- Win32_TerminalService.DelayedAutoStart
- Win32_TerminalService.Description
- Win32_TerminalService.DesktopInteract
- Win32_TerminalService.DisplayName
- Win32_TerminalService.ErrorControl
- Win32_TerminalService.ExitCode
- Win32_TerminalService.InstallDate
- Win32_TerminalService.Name
- Win32_TerminalService.PathName
- Win32_TerminalService.ProcessId
- Win32_TerminalService.ServiceSpecificExitCode
- Win32_TerminalService.ServiceType
- Win32_TerminalService.Started
- Win32_TerminalService.StartMode
- Win32_TerminalService.StartName
- Win32_TerminalService.State
- Win32_TerminalService.Status
- Win32_TerminalService.SystemCreationClassName
- Win32_TerminalService.SystemName
- Win32_TerminalService.TagId
- Win32_TerminalService.WaitHint
- Win32_TerminalService.DisconnectedSessions
- Win32_TerminalService.TotalSessions
api_location:
- TSCfgWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TerminalService class

The **Win32\_TerminalService** WMI class is a subclass of the [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) class. **Win32\_TerminalService** represents the **Element** property of the [**Win32\_TerminalServiceToSetting**](win32-terminalservicetosetting.md) association.

The following syntax is simplified from MOF code and includes all defined and inherited properties, in alphabetical order.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TERMINALSERVICE_Prov"), ClassContext("local|hkey_local_machine\\SYSTEM\\CurrentControlSet\\Control\\TerminalServer"), AMENDMENT]
class Win32_TerminalService : Win32_Service
{
  boolean  AcceptPause;
  boolean  AcceptStop;
  string   Caption;
  uint32   CheckPoint;
  string   CreationClassName;
  boolean  DelayedAutoStart;
  string   Description;
  boolean  DesktopInteract;
  string   DisplayName;
  string   ErrorControl;
  uint32   ExitCode;
  datetime InstallDate;
  string   Name;
  string   PathName;
  uint32   ProcessId;
  uint32   ServiceSpecificExitCode;
  string   ServiceType;
  boolean  Started;
  string   StartMode;
  string   StartName;
  string   State;
  string   Status;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   TagId;
  uint32   WaitHint;
  uint32   DisconnectedSessions;
  uint32   TotalSessions;
};
```

## Members

The **Win32\_TerminalService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TerminalService** class has these methods.



| Method                                                                       | Description                                                                                          |
|:-----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**Change**](win32-terminalservice-change.md)                               | Modifies a service.<br/>                                                                       |
| [**ChangeStartMode**](win32-terminalservice-changestartmode.md)             | Modifies the start mode of a service.<br/>                                                     |
| [**Create**](win32-terminalservice-create.md)                               | Creates a new service.<br/>                                                                    |
| [**Delete**](win32-terminalservice-delete.md)                               | Deletes an existing service.<br/>                                                              |
| [**GetSecurityDescriptor**](win32-terminalservice-getsecuritydescriptor.md) | Returns the security descriptor that controls access to the service.<br/>                      |
| [**InterrogateService**](win32-terminalservice-interrogateservice.md)       | Requests that a service update its state to the service manager.<br/>                          |
| [**PauseService**](win32-terminalservice-pauseservice.md)                   | Attempts to place a service in the paused state.<br/>                                          |
| [**ResumeService**](win32-terminalservice-resumeservice.md)                 | Attempts to place a service in the resumed state.<br/>                                         |
| [**SetSecurityDescriptor**](win32-terminalservice-setsecuritydescriptor.md) | Writes an updated version of the security descriptor that controls access to the service.<br/> |
| [**StartService**](win32-terminalservice-startservice.md)                   | Attempts to place a service into the startup state.<br/>                                       |
| [**StopService**](win32-terminalservice-stopservice.md)                     | Places a service in the stopped state.<br/>                                                    |
| [**UserControlService**](win32-terminalservice-usercontrolservice.md)       | Attempts to send a user-defined control code to a service.<br/>                                |



 

### Properties

The **Win32\_TerminalService** class has these properties.

<dl> <dt>

**AcceptPause**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/desktop/api/winsvc/ns-winsvc-service_status)\|dwControlsAccepted\|SERVICE\_ACCEPT\_PAUSE\_CONTINUE"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Service Accepts Pause")
</dt> </dl>

Indicates whether the service can be paused.

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**AcceptStop**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/desktop/api/winsvc/ns-winsvc-service_status)\|dwControlsAccepted\|SERVICE\_ACCEPT\_STOP"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Service Accepts Stop")
</dt> </dl>

Indicates whether the service can be stopped.

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

Short description of the service  a one-line string.

This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**CheckPoint**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/desktop/api/winsvc/ns-winsvc-service_status)\|dwCheckPoint"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Check Point Count")
</dt> </dl>

Value that the service increments periodically to report its progress during a long start, stop, pause, or continue operation. For example, the service increments this value as it completes each step of its initialization when it is starting up. The user interface program that invokes the operation on the service uses this value to track the progress of the service during a lengthy operation. This value is not valid and should be zero when the service does not have a start, stop, pause, or continue operation pending.

This property is inherited from [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Class Name")
</dt> </dl>

Name of the first concrete class to appear in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service).

</dd> <dt>

**DelayedAutoStart**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_DELAYED\_AUTO\_START\_INFO**](/windows/desktop/api/winsvc/ns-winsvc-service_delayed_auto_start_info)\|fDelayedAutostart"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Delayed Auto-Start")
</dt> </dl>

If **True**, the service is started after other auto-start services are started plus a short delay.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not supported before Windows Server 2016 and Windows 10.

This property is inherited from [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**DesktopInteract**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/desktop/api/winsvc/ns-winsvc-query_service_configa)\|dwServiceType\|SERVICE\_INTERACTIVE\_PROCESS"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Interacts With Desktop")
</dt> </dl>

Indicates whether the service can create or communicate with windows on the desktop, and thus interact in some way with a user. Interactive services must run under the Local System account. Most services are not interactive; that is, they do not communicate with the user in any way.

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**DisconnectedSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of disconnected sessions on the current server. These sessions may still be actively consuming server resources, however they currently have no network connection with a client.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/desktop/api/winsvc/ns-winsvc-query_service_configa)\|lpDisplayName"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Display Name")
</dt> </dl>

Name of the service as viewed in the Services snap-in. This string has a maximum length of 256 characters. Note that the display name and the service name (which is stored in the registry) are not always the same. For example, the DHCP Client service has the service name Dhcp but the display name DHCP Client. The name is case-preserved in the Service Control Manager. However, [**DisplayName**](/windows/desktop/CIMWin32Prov/win32-service) comparisons are always case-insensitive.

Constraint: Accepts the same value as the [**Name**](/windows/desktop/CIMWin32Prov/win32-service) property.

Example: "Atdisk"

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**ErrorControl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/desktop/api/winsvc/ns-winsvc-query_service_configa)\|dwErrorControl"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Severity Of Startup Failure")
</dt> </dl>

Severity of the error if this service fails to start during startup. The value indicates the action taken by the startup program if failure occurs. All errors are logged by the computer system.

<dt>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>**Ignore** ("Ignore")


</dt> <dd>

User is not notified.

</dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>**Normal** ("Normal")


</dt> <dd>

User is notified. Usually this will be a message box display notifying the user of the problem.

</dd> <dt>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>**Severe** ("Severe")


</dt> <dd>

System is restarted with the last-known-good configuration.

</dd> <dt>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>**Critical** ("Critical")


</dt> <dd>

System attempts to restart with a good configuration. If the service fails to start a second time, startup fails.

</dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** ("Unknown")


</dt> <dd>

Severity of the error is unknown.

</dd> </dl>

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**ExitCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/desktop/api/winsvc/ns-winsvc-service_status)\|dwWin32ExitCode"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Exit Code")
</dt> </dl>

Windows error code that defines errors encountered in starting or stopping the service. This property is set to **ERROR\_SERVICE\_SPECIFIC\_ERROR** (1066) when the error is unique to the service represented by this class, and information about the error is available in the [**ServiceSpecificExitCode**](/windows/desktop/CIMWin32Prov/win32-service) property. The service sets this value to **NO\_ERROR** when running, and again upon normal termination.

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Date object is installed. This property does not require a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Unique identifier of the service that provides an indication of the functionality that is managed. This functionality is described in the [**Description**](/windows/desktop/CIMWin32Prov/win32-service) property of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**PathName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/desktop/api/winsvc/ns-winsvc-query_service_configa)\|lpBinaryPathName"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("File Path Name")
</dt> </dl>

Fully qualified path to the service binary file that implements the service.

Example: "\\SystemRoot\\System32\\drivers\\afd.sys"

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**ProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_STATUS\_PROCESS**](/windows/desktop/api/winsvc/ns-winsvc-service_status_process)\|dwProcessId"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Process Id")
</dt> </dl>

Process identifier of the service.

Example: 324

This property is inherited from [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service).

</dd> <dt>

**ServiceSpecificExitCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/desktop/api/winsvc/ns-winsvc-service_status)\|dwServiceSpecificExitCode"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Server Specific Exit Code")
</dt> </dl>

Service-specific error code for errors that occur while the service is either starting or stopping. The exit codes are defined by the service represented by this class. This value is only set when the [**ExitCode**](/windows/desktop/CIMWin32Prov/win32-service) property value is **ERROR\_SERVICE\_SPECIFIC\_ERROR** (1066).

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**ServiceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/desktop/api/winsvc/ns-winsvc-query_service_configa)\|dwServiceType"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Service Type")
</dt> </dl>

Type of service provided to calling processes.

The values are:

<dt>

<span id="Kernel_Driver"></span><span id="kernel_driver"></span><span id="KERNEL_DRIVER"></span>

**Kernel Driver** ("Kernel Driver")


</dt> <dd></dd> <dt>

<span id="File_System_Driver"></span><span id="file_system_driver"></span><span id="FILE_SYSTEM_DRIVER"></span>

**File System Driver** ("File System Driver")


</dt> <dd></dd> <dt>

<span id="Adapter"></span><span id="adapter"></span><span id="ADAPTER"></span>

**Adapter** ("Adapter")


</dt> <dd></dd> <dt>

<span id="Recognizer_Driver"></span><span id="recognizer_driver"></span><span id="RECOGNIZER_DRIVER"></span>

**Recognizer Driver** ("Recognizer Driver")


</dt> <dd></dd> <dt>

<span id="Own_Process"></span><span id="own_process"></span><span id="OWN_PROCESS"></span>

**Own Process** ("Own Process")


</dt> <dd></dd> <dt>

<span id="Share_Process"></span><span id="share_process"></span><span id="SHARE_PROCESS"></span>

**Share Process** ("Share Process")


</dt> <dd></dd> <dt>

<span id="Interactive_Process"></span><span id="interactive_process"></span><span id="INTERACTIVE_PROCESS"></span>

**Interactive Process** ("Interactive Process")


</dt> <dd></dd> </dl>

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**Started**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Started")
</dt> </dl>

Indicates whether or not the service is started.

This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service).

</dd> <dt>

**StartMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Start Mode")
</dt> </dl>

Start mode of the Windows base service.

<dt>

<span id="Boot"></span><span id="boot"></span><span id="BOOT"></span>

<span id="Boot"></span><span id="boot"></span><span id="BOOT"></span>**Boot** ("Boot")


</dt> <dd>

Device driver started by the operating system loader (valid only for driver services).

</dd> <dt>

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>**System** ("System")


</dt> <dd>

Device driver started by the operating system initialization process. This value is valid only for driver services.

</dd> <dt>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>**Auto** ("Auto")


</dt> <dd>

Service to be started automatically by the service control manager during system startup. Auto services are started even if a user does not log on.

</dd> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>**Manual** ("Manual")


</dt> <dd>

Service to be started by the Service Control Manager when a process calls the [**StartService**](/windows/desktop/CIMWin32Prov/startservice-method-in-class-win32-service) method. These services do not start unless a user logs on and starts them.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** ("Disabled")


</dt> <dd>

Service that cannot be started until its StartMode is changed to either Auto or Manual.

</dd> </dl>

This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service).

</dd> <dt>

**StartName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/desktop/api/winsvc/ns-winsvc-query_service_configa)\|lpServiceStartName"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Starting Account Name")
</dt> </dl>

Account name under which a service runs. Depending on the service type, the account name may be in the form of "DomainName\\Username" or UPN format ("*Username@DomainName*"). The service process is logged by using one of these two forms when it runs. If the account belongs to the built-in domain, then ".\\Username" can be specified. For kernel or system-level drivers, [**StartName**](/windows/desktop/CIMWin32Prov/win32-service) contains the driver object name (that is, "\\FileSystem\\Rdr" or "\\Driver\\Xns") which the I/O system uses to load the device driver. Additionally, if **NULL** is specified, the driver runs with a default object name created by the I/O system based on the service name.

Example: "DWDOM\\Admin"

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/desktop/api/winsvc/ns-winsvc-service_status)\|dwCurrentState "), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("State")
</dt> </dl>

Current state of the base service.

The values are:

<dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** ("Stopped")


</dt> <dd></dd> <dt>

<span id="Start_Pending"></span><span id="start_pending"></span><span id="START_PENDING"></span>

**Start Pending** ("Start Pending")


</dt> <dd></dd> <dt>

<span id="Stop_Pending"></span><span id="stop_pending"></span><span id="STOP_PENDING"></span>

**Stop Pending** ("Stop Pending")


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

**Running** ("Running")


</dt> <dd></dd> <dt>

<span id="Continue_Pending"></span><span id="continue_pending"></span><span id="CONTINUE_PENDING"></span>

**Continue Pending** ("Continue Pending")


</dt> <dd></dd> <dt>

<span id="Pause_Pending"></span><span id="pause_pending"></span><span id="PAUSE_PENDING"></span>

**Pause Pending** ("Pause Pending")


</dt> <dd></dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

**Paused** ("Paused")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> </dl>

**Windows Server 2008 and Windows Vista:** This property is read-only before Windows 7 and Windows Server 2008 R2.

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

The values are:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_System**](/windows/desktop/CIMWin32Prov/cim-system).CreationClassName"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("System Class Name")
</dt> </dl>

Type name of the system that hosts this service.

This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_System**](/windows/desktop/CIMWin32Prov/cim-system).Name"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("System Name")
</dt> </dl>

Name of the system that hosts this service.

This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service).

</dd> <dt>

**TagId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/desktop/api/winsvc/ns-winsvc-query_service_configa)\|dwTagId"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Tag Id")
</dt> </dl>

Unique tag value for this service in the group. A value of 0 (zero) indicates that the service does not have a tag. A tag can be used to order service startup within a load order group by specifying a tag order vector in the registry located at:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\    **GroupOrderList**

Tags are only evaluated for Kernel Driver and File System Driver start type services that have Boot or System start modes.

This property is inherited from [**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).

</dd> <dt>

**TotalSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of sessions on the current server. This includes both connected and disconnected sessions.

</dd> <dt>

**WaitHint**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/desktop/api/winsvc/ns-winsvc-service_status)\|dwWaitHint"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Estimated Wait Time")
</dt> </dl>

Estimated time required, in milliseconds, for a pending start, stop, pause, or continue operation. After the specified time has elapsed, the service makes its next call to the **SetServiceStatus** method with either an incremented [**CheckPoint**](/windows/desktop/CIMWin32Prov/win32-service) value or a change in **CurrentState**. If the amount of time specified by **WaitHint** passes, and **CheckPoint** has not been incremented, or **CurrentState** has not changed, the service control manager or service control program assumes that an error has occurred.

This property is inherited from [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service).

</dd> </dl>

## Remarks

Since the **Win32\_TerminalService** class is a subclass of the [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) class, the class inherits all properties and methods of **Win32\_Service**.

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md) is associated to **Win32\_TerminalService** as the **Setting** property of the [**Win32\_TerminalServiceToSetting**](win32-terminalservicetosetting.md) association.

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md) is associated to **Win32\_TerminalService** as the **Setting** property of the [**Win32\_TSSessionDirectorySetting**](win32-tssessiondirectorysetting.md) association.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service)
</dt> <dt>

[**Win32\_TerminalServiceToSetting**](win32-terminalservicetosetting.md)
</dt> <dt>

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md)
</dt> <dt>

[**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice)
</dt> <dt>

[**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service)
</dt> </dl>

 

