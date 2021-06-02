---
title: SystemRestoreConfig class
description: Provides properties for controlling the frequency of scheduled restore point creation and the amount of disk space consumed on each drive.
ms.assetid: ed09e03f-8cc1-4923-8f39-bbe7d9a19b44
keywords:
- SystemRestoreConfig class System Restore
- SystemRestoreConfig class System Restore , described
topic_type:
- apiref
api_name:
- SystemRestoreConfig
- SystemRestoreConfig.RPSessionInterval
- SystemRestoreConfig.RPGlobalInterval
- SystemRestoreConfig.RPLifeInterval
- SystemRestoreConfig.DiskPercent
api_location:
- Root\Default
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# SystemRestoreConfig class

Provides properties for controlling the frequency of scheduled restore point creation and the amount of disk space consumed on each drive.

## Syntax

``` syntax
class SystemRestoreConfig
{
  uint32 RPSessionInterval;
  uint32 RPGlobalInterval;
  uint32 RPLifeInterval;
  uint32 DiskPercent;
};
```

## Members

The **SystemRestoreConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemRestoreConfig** class has these properties.

<dl> <dt>

**DiskPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount of disk space on each drive that can be used by System Restore. This value is specified as a percentage of the total drive space. The default value is 12 percent.

**Windows Vista:** Receives a value from the Volume Shadow Copy Service (VSS). This this is the maximum amount of disk space on each drive that can be used by System Restore. The default value is 15 percent of the total drive space or 30 percent of the available free space, whichever is smaller.

</dd> <dt>

**RPGlobalInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The absolute time interval at which scheduled system checkpoints are created, in seconds. The default value is 86,400 (24 hours).

**Windows Vista:** Receives a value from the task scheduler for System Restore. Zero if the task is disabled.

</dd> <dt>

**RPLifeInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time interval for which restore points are preserved, in seconds. When a restore point becomes older than this specified interval, it is deleted. The default age limit is 90 days.

**Windows Vista:** Receives a value of **UINTMAX**.

</dd> <dt>

**RPSessionInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time interval at which scheduled system checkpoints are created during the session, in seconds. The default value is zero, indicating that the feature is turned off.

**Windows Vista:** Receives zero if System Restore is disabled.

</dd> </dl>

## Examples

The following sample code is not supported. Use the command-line tool Vssadmin.exe to change the size of reserved drive space.

**Windows XP:** This sample is supported.


```VB
'The SystemRestoreConfig class provides properties for controlling the frequency of 
'scheduled restore point creation and the amount of disk space consumed on each drive.

Set Args = wscript.Arguments
Set regSR = GetObject("winmgmts:{impersonationLevel=impersonate}!root/default:SystemRestoreConfig='SR'")

If Args.Count() = 0 Then
    Wscript.Echo "Usage: RegSR [RP{Session|Global|Life}Interval[=value]] [DiskPercent[=value]]"
Else    
For i = 0 To Args.Count() - 1
    Myarg = Args.Item(i)
    Pos = InStr(Myarg, "=")
    If Pos <> 0 Then
        Myarray = Split(Myarg, "=", -1, 1)
        myoption = Myarray(0)
        value = Myarray(1)
    Else 
        myoption = Myarg
    End If    
    If myoption = "RPSessionInterval" Then
        If Pos = 0 Then
            Wscript.Echo "RPSessionInterval = " & regSR.RPSessionInterval
        Else    
            regSR.RPSessionInterval = value
            regSR.Put_
        End If
    ElseIf myoption = "RPGlobalInterval" Then
        If Pos = 0 Then
            Wscript.Echo "RPGlobalInterval = " & regSR.RPGlobalInterval
        Else    
            regSR.RPGlobalInterval = value
            regSR.Put_
        End If
    ElseIf myoption = "RPLifeInterval" Then
        If Pos = 0 Then
            Wscript.Echo "RPLifeInterval = " & regSR.RPLifeInterval
        Else    
            regSR.RPLifeInterval = value
            regSR.Put_
        End If
    ElseIf myoption = "DiskPercent" Then
        If Pos = 0 Then
            Wscript.Echo "DiskPercent = " & regSR.DiskPercent
        Else    
            regSR.DiskPercent = value
            regSR.Put_
        End If
    End If
Next
End If
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | None supported<br/>                                                         |
| Namespace<br/>                | Root\\Default<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Sr.mof</dt> </dl> |



## See also

<dl> <dt>

[Restore Points](restore-points.md)
</dt> <dt>

[Windows Management Instrumentation](/windows/desktop/WmiSdk/wmi-start-page)
</dt> </dl>

 

