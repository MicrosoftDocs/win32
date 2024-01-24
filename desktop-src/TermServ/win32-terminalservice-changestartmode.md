---
title: ChangeStartMode method of the Win32_Service class (Remote Desktop Services)
description: Modifies the start mode of a Win32\_TerminalService.
ms.assetid: 4F4B8CFC-B38C-47C6-A2BA-D498EC2B7F55
ms.tgt_platform: multiple
keywords:
- ChangeStartMode method Remote Desktop Services
- ChangeStartMode method Remote Desktop Services , Win32_Service class
- Win32_Service class Remote Desktop Services , ChangeStartMode method
topic_type:
- apiref
api_name:
- Win32_Service.ChangeStartMode
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ChangeStartMode method of the Win32_Service class (Remote Desktop Services)

The **ChangeStartMode** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method modifies the start mode of a [**Win32\_TerminalService**](win32-terminalservice.md).

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 ChangeStartMode(
  [in] string StartMode
);
```



## Parameters

<dl> <dt>

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

Service to be started by the Service Control Manager when a process calls the [**StartService**](win32-terminalservice-startservice.md) method.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled**


</dt> <dd>

Service that can no longer be started.

</dd> </dl> </dd> </dl>

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

The requested control code cannot be sent to the service because the state of the service ([**Win32\_BaseService**](/windows/desktop/CIMWin32Prov/win32-baseservice).**State** property) is equal to 0, 1, or 2.

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

## Examples

The following [Change StartMode of a Service](https://Gallery.TechNet.Microsoft.Com/6d0f06ed-f840-4228-ad2d-e16ebe6a3aed) PowerShell sample, pulled from TechNet Gallery, changes the start mode of a service.


```PowerShell
$wmi = get-wmiobject -class win32_service -namespace root\cimv2 -computername lisbon | 
where-object { $_.name -eq 'bits' } 
 
$rtn = $wmi.changestartmode("manual") 
if($rtn.returnvalue -eq 0) { "success" } 
ELSE 
  { " $($rtn.returnvalue) was reported" }
```



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

 

