---
title: PauseService method of the Win32\_Service class
description: Attempts to place the service in the paused state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '101987F6-FBAB-4E79-B1FA-346B1EF58DE1'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["PauseService method Remote Desktop Services", "PauseService method Remote Desktop Services , Win32_Service class", "Win32_Service class Remote Desktop Services , PauseService method"]
topic_type:
- apiref
api_name:
- Win32_Service.PauseService
api_location:
- TSCfgWmi.dll
api_type:
- COM
---

# PauseService method of the Win32\_Service class

The **PauseService** [WMI class](https://msdn.microsoft.com/library/aa393244) method attempts to place the service in the paused state.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 PauseService();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the values listed in the following list, or any other value to indicate an error. For additional error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978). For general **HRESULT** values, see [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

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

The requested control code cannot be sent to the service because the state of the service ([**Win32\_BaseService**](https://msdn.microsoft.com/library/aa394073).**State** property) is equal to 0, 1, or 2.

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

After you have determined which services can be stopped or paused, you can use the [**StopService**](win32-terminalservice-stopservice.md) and **PauseService** methods to stop and pause services. The decision to stop a service rather than pause it, or vice versa, depends on several factors, including the following:

-   Is the service capable of being paused? If not, your only option is the stop the service.
-   Do you need to continue handling client requests for anyone already connected to the service? If so, pausing a service typically allows it to handle existing clients while denying access to new clients. By contrast, when you stop a service, all clients are immediately disconnected.
-   Do you need to reconfigure a service and have the changes take effect immediately? Although service properties can be changed while a service is paused, most of them do not take effect until the service is actually stopped and restarted.

The scripting code required to stop a service is almost identical to the code required to pause the service.

## Examples

The [Pause Services Running Under a Specific Account](https://Gallery.TechNet.Microsoft.Com/12a256dd-39da-4690-b3f0-f0adccaf25f1) VBScript sample Pauses all services running under the hypothetical service account Netsvc.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Service**](https://msdn.microsoft.com/library/aa394418)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> <dt>

[**Win32\_TerminalService**](win32-terminalservice.md)
</dt> <dt>

[WMI Tasks: Services](https://msdn.microsoft.com/library/aa394602)
</dt> <dt>

[**StopService**](https://msdn.microsoft.com/library/aa393673)
</dt> </dl>

 

 





