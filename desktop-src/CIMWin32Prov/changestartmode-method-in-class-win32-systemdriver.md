---
description: Modifies the start mode of a Win32\_SystemDriver service.
ms.assetid: 34f4e0ac-d8a0-4be7-8c84-0252e50db441
ms.tgt_platform: multiple
title: ChangeStartMode method of the Win32_SystemDriver class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemDriver.ChangeStartMode
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# ChangeStartMode method of the Win32\_SystemDriver class

The **ChangeStartMode** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method modifies the start mode of a [**Win32\_SystemDriver**](win32-systemdriver.md) service.

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

Start mode of the Windows base service.

<dt>

<span id="Boot_Start"></span><span id="boot_start"></span><span id="BOOT_START"></span>

<span id="Boot_Start"></span><span id="boot_start"></span><span id="BOOT_START"></span>**Boot Start** ("Boot")


</dt> <dd>

Device driver started by the operating system loader. This value is valid only for driver services.

</dd> <dt>

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>**System** ("System")


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

Service to be started by the service control manager when a process calls the [**StartService**](startservice-method-in-class-win32-systemdriver.md) method.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** ("Disabled")


</dt> <dd>

Service that can no longer be started.

</dd> </dl> </dd> </dl>

## Return value

Returns a value of 0 (zero) if the service was successfully modified, 1 (one) if the request is not supported, and any other number to indicate an error.

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

 

