---
description: The SetPriority&\#32;WMI class method attempts to change the execution priority of the process.
ms.assetid: ef012e9e-ff65-4881-835e-ddab23af9333
ms.tgt_platform: multiple
title: SetPriority method of the Win32_Process class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Process.SetPriority
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetPriority method of the Win32\_Process class

The **SetPriority** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method attempts to change the execution priority of the process.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 SetPriority(
  [in] sint32 Priority
);
```



## Parameters

<dl> <dt>

*Priority* \[in\]
</dt> <dd>

New priority class for the process. Note that these values are different than those explicitly stated in the **Priority** property of [**Win32\_Process**](win32-process.md).

<dt>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>**Idle** (64)


</dt> <dd>

Specified for a process with threads that run only when the system is idle. The threads of the process are preempted by the threads of a process that run in a higher priority class, for example, a screen saver. The idle-priority class is inherited by child processes.

</dd> <dt>

<span id="Below_Normal"></span><span id="below_normal"></span><span id="BELOW_NORMAL"></span>

<span id="Below_Normal"></span><span id="below_normal"></span><span id="BELOW_NORMAL"></span>**Below Normal** (16384)


</dt> <dd>

Indicates a process that has priority above **IDLE\_PRIORITY\_CLASS**, but below **NORMAL\_PRIORITY\_CLASS**.

</dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>**Normal** (32)


</dt> <dd>

Specified for a process with no special scheduling needs.

</dd> <dt>

<span id="Above_Normal"></span><span id="above_normal"></span><span id="ABOVE_NORMAL"></span>

<span id="Above_Normal"></span><span id="above_normal"></span><span id="ABOVE_NORMAL"></span>**Above Normal** (32768)


</dt> <dd>

Indicates a process that has priority above **NORMAL\_PRIORITY\_CLASS**, but below **HIGH\_PRIORITY\_CLASS**.

</dd> <dt>

<span id="High_Priority"></span><span id="high_priority"></span><span id="HIGH_PRIORITY"></span>

<span id="High_Priority"></span><span id="high_priority"></span><span id="HIGH_PRIORITY"></span>**High Priority** (128)


</dt> <dd>

Specified for a process that performs time-critical tasks that must be executed immediately. The threads of the process preempt the threads of normal or idle priority class processes. An example is the Task List, which must respond quickly when called by the user, regardless of the load on the operating system. Use extreme care when using the high-priority class, because a high-priority class application can use nearly all of the available CPU time.

</dd> <dt>

<span id="Realtime"></span><span id="realtime"></span><span id="REALTIME"></span>

<span id="Realtime"></span><span id="realtime"></span><span id="REALTIME"></span>**Realtime** (256)


</dt> <dd>

Specified for a process that has the highest possible priority. The threads of the process preempt the threads of all of the other processes, including operating system processes that perform important tasks. For example, a real-time process that executes for more than a very brief interval can cause disk caches not to flush or a mouse to be unresponsive.

</dd> </dl> </dd> </dl>

## Return value

Returns one of the values listed in the following list, or a different value to indicate an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion** (0)
</dt> <dt>

**Access denied** (2)
</dt> <dt>

**Insufficient privilege** (3)
</dt> <dt>

**Unknown failure** (8)
</dt> <dt>

**Path not found** (9)
</dt> <dt>

**Invalid parameter** (21)
</dt> <dt>

**Other** (22 4294967295)
</dt> </dl>

## Remarks

To set the priority to Realtime, the caller must have **SeIncreaseBasePriorityPrivilege** (**SE\_INC\_BASE\_PRIORITY\_PRIVILEGE**). Without this privilege, the highest the priority can be set to is High Priority.

## Examples

The [Modify the Priority Of a Running Process](https://Gallery.TechNet.Microsoft.Com/23615ee7-cccb-43c2-b994-6106ce2fc05e) VBScript sample changes the priority of a running instance of Notepad.exe from Normal to Above Normal.

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

[**Win32\_Process**](win32-process.md)
</dt> </dl>

 

