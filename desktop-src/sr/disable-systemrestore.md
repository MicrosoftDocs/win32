---
title: Disable method of the SystemRestore class
description: Disables monitoring on a particular drive.
ms.assetid: 2ad37dd4-7d80-4697-9dbb-abb329a34ff7
keywords:
- Disable method System Restore
- Disable method System Restore , SystemRestore class
- SystemRestore class System Restore , Disable method
topic_type:
- apiref
api_name:
- SystemRestore.Disable
api_location:
- Root\Default
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Disable method of the SystemRestore class

Disables monitoring on a particular drive.

## Syntax


```mof
uint32 Disable(
  [in] String Drive
);
```



## Parameters

<dl> <dt>

*Drive* \[in\]
</dt> <dd>

The drive to be disabled. The drive string should be of the form "C:\\". If this parameter is the system drive or an empty string (""), no drives are monitored.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the method returns one of the COM error codes defined in WinError.h.

## Examples


```VB
'Disable Method of the SystemRestore Class
'Disables monitoring on a particular drive.
Set Args = wscript.Arguments
If Args.Count() > 0 Then
    Drive = Args.item(0)
Else
    Drive = ""
End If

Set obj = GetObject("winmgmts:{impersonationLevel=impersonate}!root/default:SystemRestore")

If (obj.Disable(Drive)) = 0 Then
    wscript.Echo "Success"
Else 
    wscript.Echo "Failed"
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

[**SystemRestore**](systemrestore.md)
</dt> </dl>

 

 





