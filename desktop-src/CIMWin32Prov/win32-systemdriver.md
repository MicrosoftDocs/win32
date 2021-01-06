---
description: Represents the system driver for a base service.
ms.assetid: 67dc6e14-c8c1-4168-8f99-b04c6ecd4ad2
ms.tgt_platform: multiple
title: Win32_SystemDriver class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemDriver
- Win32_SystemDriver.AcceptPause
- Win32_SystemDriver.AcceptStop
- Win32_SystemDriver.Caption
- Win32_SystemDriver.CreationClassName
- Win32_SystemDriver.Description
- Win32_SystemDriver.DesktopInteract
- Win32_SystemDriver.DisplayName
- Win32_SystemDriver.ErrorControl
- Win32_SystemDriver.ExitCode
- Win32_SystemDriver.InstallDate
- Win32_SystemDriver.Name
- Win32_SystemDriver.PathName
- Win32_SystemDriver.ServiceSpecificExitCode
- Win32_SystemDriver.ServiceType
- Win32_SystemDriver.Started
- Win32_SystemDriver.StartMode
- Win32_SystemDriver.StartName
- Win32_SystemDriver.State
- Win32_SystemDriver.Status
- Win32_SystemDriver.SystemCreationClassName
- Win32_SystemDriver.SystemName
- Win32_SystemDriver.TagId
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_SystemDriver class

The **Win32\_SystemDriver** [WMI class](../wmisdk/retrieving-a-class.md) represents the system driver for a base service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), SupportsUpdate, UUID("{8502C4C5-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemDriver : Win32_BaseService
{
  boolean  AcceptPause;
  boolean  AcceptStop;
  string   Caption;
  string   CreationClassName;
  string   Description;
  boolean  DesktopInteract;
  string   DisplayName;
  string   ErrorControl;
  uint32   ExitCode;
  datetime InstallDate;
  string   Name;
  string   PathName;
  uint32   ServiceSpecificExitCode;
  string   ServiceType;
  boolean  Started;
  string   StartMode;
  string   StartName;
  string   State;
  string   Status;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   TagId;
};
```

## Members

The **Win32\_SystemDriver** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_SystemDriver** class has these methods.



| Method                                                                              | Description                                                                                     |
|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Change**](change-method-in-class-win32-systemdriver.md)                         | Class method that modifies a service.<br/>                                                |
| [**ChangeStartMode**](changestartmode-method-in-class-win32-systemdriver.md)       | Class method that modifies the start mode of a service.<br/>                              |
| [**Create**](create-method-in-class-win32-systemdriver.md)                         | Class method that creates a new service.<br/>                                             |
| [**Delete**](delete-method-in-class-win32-systemdriver.md)                         | Class method that deletes an existing service.<br/>                                       |
| [**InterrogateService**](interrogateservice-method-in-class-win32-systemdriver.md) | Class method that requests that the service update its state to the service manager.<br/> |
| [**PauseService**](pauseservice-method-in-class-win32-systemdriver.md)             | Class method that attempts to place the service in the paused state.<br/>                 |
| [**ResumeService**](resumeservice-method-in-class-win32-systemdriver.md)           | Class method that attempts to place the service in the resumed state.<br/>                |
| [**StartService**](startservice-method-in-class-win32-systemdriver.md)             | Class method that attempts to place the service into its startup state.<br/>              |
| [**StopService**](stopservice-method-in-class-win32-systemdriver.md)               | Class method that places the service in the stopped state.<br/>                           |
| [**UserControlService**](usercontrolservice-method-in-class-win32-systemdriver.md) | Class method that attempts to send a user-defined control code to a service.<br/>         |



 

### Properties

The **Win32\_SystemDriver** class has these properties.

<dl> <dt>

**AcceptPause**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/win32/api/winsvc/ns-winsvc-service_status)\|dwControlsAccepted\|SERVICE\_ACCEPT\_PAUSE\_CONTINUE"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Service Accepts Pause")
</dt> </dl>

Service can be paused.

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

</dd> <dt>

**AcceptStop**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/win32/api/winsvc/ns-winsvc-service_status)\|dwControlsAccepted\|SERVICE\_ACCEPT\_STOP"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Service Accepts Stop")
</dt> </dl>

Service can be stopped.

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Caption")
</dt> </dl>

Short description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Class Name")
</dt> </dl>

Name of the first concrete class to appear in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Description")
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**DesktopInteract**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/win32/api/winsvc/ns-winsvc-query_service_configa)\|dwServiceType\|SERVICE\_INTERACTIVE\_PROCESS"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Interacts With Desktop")
</dt> </dl>

This service can create or communicate with windows on the desktop.

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/win32/api/winsvc/ns-winsvc-query_service_configa)\|lpDisplayName"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Display Name")
</dt> </dl>

Display name of the service. This string has a maximum length of 256 characters. The name is case-preserved in the Service Control Manager. **DisplayName** comparisons are always case-insensitive.

Constraints: Accepts the same value as the **Name** property.

Example: "Atdisk"

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

</dd> <dt>

**ErrorControl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/win32/api/winsvc/ns-winsvc-query_service_configa)\|dwErrorControl"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Severity Of Startup Failure")
</dt> </dl>

Severity of the error if this service fails to start during startup. This value indicates the action taken by the startup program if failure occurs. All errors are logged by the computer system.

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

<dt>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>**Ignore** ("Ignore")


</dt> <dd>

User is not notified.

</dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>**Normal** ("Normal")


</dt> <dd>

User is notified.

</dd> <dt>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>**Severe** ("Severe")


</dt> <dd>

System is restarted with the last-known-good configuration.

</dd> <dt>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>**Critical** ("Critical")


</dt> <dd>

System attempts to restart with a good configuration.

</dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** ("Unknown")


</dt> <dd>

Cause of the failure is unknown.

</dd> </dl>

</dd> <dt>

**ExitCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/win32/api/winsvc/ns-winsvc-service_status)\|dwWin32ExitCode"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Exit Code")
</dt> </dl>

Windows error code defining any problems encountered in starting or stopping the service. This property is set to **ERROR\_SERVICE\_SPECIFIC\_ERROR** (1066) when the error is unique to the service represented by this class, and information about the error is available in the **ServiceSpecificExitCode** property. The service sets this value to **NO\_ERROR** when running, and again upon normal termination.

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Install Date")
</dt> </dl>

Object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/key-qualifier.md)
</dt> </dl>

Unique identifier for the service which provides an indication of the functionality that is managed. This functionality is described in more detail in the object **Description** property.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**PathName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/win32/api/winsvc/ns-winsvc-query_service_configa)\|lpBinaryPathName"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("File Path Name")
</dt> </dl>

Fully qualified path to the service binary file that implements the service.

Example: "\\SystemRoot\\System32\\drivers\\afd.sys"

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

</dd> <dt>

**ServiceSpecificExitCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/win32/api/winsvc/ns-winsvc-service_status)\|dwServiceSpecificExitCode"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Server Specific Exit Code")
</dt> </dl>

Service-specific error code for errors that occur while the service is either starting or stopping. The exit codes are defined by the service represented by this class. This value is only set when the **ExitCode** property value is **ERROR\_SERVICE\_SPECIFIC\_ERROR** (1066).

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

</dd> <dt>

**ServiceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/win32/api/winsvc/ns-winsvc-query_service_configa)\|dwServiceType"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Service Type")
</dt> </dl>

Type of service provided to calling processes.

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

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

</dd> <dt>

**Started**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Started")
</dt> </dl>

Service has been started.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**StartMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Start Mode")
</dt> </dl>

Start mode of the system driver.

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

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

Service to be started automatically by the service control manager during system start up.

</dd> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>**Manual** ("Manual")


</dt> <dd>

Service to be started by the service control manager when a process calls the [**StartService**](startservice-method-in-class-win32-systemdriver.md) method.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** ("Disabled")


</dt> <dd>

Service that can no longer be started.

</dd> </dl>

</dd> <dt>

**StartName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/win32/api/winsvc/ns-winsvc-query_service_configa)\|lpServiceStartName"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Starting Account Name")
</dt> </dl>

Account name under which the service runs. Depending on the service type, the account name may be in the form of DomainName\\Username. The service process will be logged using one of these two forms when it runs. If the account belongs to the built-in domain, .\\Username can be specified. If **NULL** is specified, the service will be logged on as the LocalSystem account. For kernel or system-level drivers, **StartName** contains the driver object name (that is, \\FileSystem\\Rdr or \\Driver\\Xns) which the input and output (I/O) system uses to load the device driver. Additionally, if **NULL** is specified, the driver runs with a default object name created by the I/O system based on the service name.

Example: "DWDOM\\Admin"

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**SERVICE\_STATUS**](/windows/win32/api/winsvc/ns-winsvc-service_status)\|dwCurrentState "), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("State")
</dt> </dl>

Current state of the base service.

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

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

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (10), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Status")
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

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

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("System Class Name")
</dt> </dl>

Type name of the system that hosts this service.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_System**](cim-system.md).**Name**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("System Name")
</dt> </dl>

Name of the system that hosts this service.

This property is inherited from [**CIM\_Service**](cim-service.md).

</dd> <dt>

**TagId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Service Structures\|[**QUERY\_SERVICE\_CONFIG**](/windows/win32/api/winsvc/ns-winsvc-query_service_configa)\|dwTagId"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Tag Id")
</dt> </dl>

Unique tag value for this service in the group. A value of 0 (zero) indicates that the service has not been assigned a tag. A tag can be used for ordering service startup within a load order group by specifying a tag order vector in the registry located at:

This property is inherited from [**Win32\_BaseService**](win32-baseservice.md).

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\GroupOrderList**.

Tags are only evaluated for Kernel Driver and File System Driver start-type services that have Boot or System start modes.

</dd> </dl>

## Remarks

The **Win32\_SystemDriver** class is derived from [**Win32\_BaseService**](win32-baseservice.md).

## Examples

The [List System Drivers](https://Gallery.TechNet.Microsoft.Com/5629cc13-cefc-4e51-a24f-aac6db23d141) VBScript sample Displays installed system drivers in an HTML file.

The following PowerShell example retrieves a number of properties from the running system drivers on a computer.


```PowerShell
Get-WmiObject -Class Win32_SystemDriver | Where-Object -FilterScript {$_.State -eq "Running"} | Where-Object -FilterScript {$_.StartMode -eq "Manual"} | Format-Table -Property Name,DisplayName
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_BaseService**](win32-baseservice.md)
</dt> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> </dl>

 

 
