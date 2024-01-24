---
title: Restore method of the SystemRestore class
description: Initiates a system restore.
ms.assetid: ca4aa97b-fa59-407d-b127-951d46932c33
keywords:
- Restore method System Restore
- Restore method System Restore , SystemRestore class
- SystemRestore class System Restore , Restore method
topic_type:
- apiref
api_name:
- SystemRestore.Restore
api_location:
- Root\\Default
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Restore method of the SystemRestore class

Initiates a system restore. The caller must force a system reboot. The actual restoration occurs during the reboot.

## Syntax


```mof
uint32 Restore(
  [in] uint32 SequenceNumber
);
```



## Parameters

<dl> <dt>

*SequenceNumber* \[in\]
</dt> <dd>

The sequence number of the restore point. To determine the sequence number for a specific restore point, enumerate all restore points on the system.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the method returns one of the COM error codes defined in WinError.h.

## Examples


```VB
'Restore Method of the SystemRestore Class
'Initiates a system restore. The caller must 
'force a system reboot. The actual restoration 
'occurs during the reboot.
Set Args = wscript.Arguments
RpNum = Args.item(0)
Set obj = GetObject("winmgmts:{impersonationLevel=impersonate}!root/default:SystemRestore")
if obj.Restore(RpNum) <> 0 Then
    wscript.Echo "Restore failed"
End If
Set OpSysSet = GetObject("winmgmts:{(Shutdown)}//./root/cimv2").ExecQuery("select * from Win32_OperatingSystem where Primary=true")
for each OpSys in OpSysSet
    OpSys.Reboot()
next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | None supported<br/>                                                         |
| Namespace<br/>                | Root\\\\Default<br/>                                                        |
| MOF<br/>                      | <dl> <dt>Sr.mof</dt> </dl> |



## See also

<dl> <dt>

[**SystemRestore**](systemrestore.md)
</dt> </dl>

 

 





