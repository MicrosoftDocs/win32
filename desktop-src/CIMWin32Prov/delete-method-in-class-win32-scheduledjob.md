---
Description: The Delete&\#8194;WMI class method deletes a scheduled job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 064ff3f8-6d41-4f8d-a511-6c051bb48a5b
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Delete method of the Win32\_ScheduledJob class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Delete method of the Win32\_ScheduledJob class

The **Delete** [WMI class](https://msdn.microsoft.com/library/aa393244) method deletes a scheduled job.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Delete();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) on success, and any other number to indicate an error. For additional error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978). For general **HRESULT** values, see [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**Successful completion**
</dt> <dd>

0

The request was accepted.

</dd> <dt>

**Not supported**
</dt> <dd>

1

The request is not supported.

</dd> <dt>

**Access denied**
</dt> <dd>

2

The user did not have the necessary access.

</dd> <dt>

**Unknown failure**
</dt> <dd>

8

Interactive process.

</dd> <dt>

**Path not found**
</dt> <dd>

9

The directory path to the service executable file was not found.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

Invalid parameters have been passed to the service.

</dd> <dt>

**Service not started**
</dt> <dd>

22

The account which this service is to run under is either invalid or lacks the permissions to run the service.

</dd> <dt>

**Other**
</dt> <dd>

23 4294967295

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_ScheduledJob**](win32-scheduledjob.md)
</dt> </dl>

 

 




