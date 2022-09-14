---
title: Enable method of the SystemRestore class
description: Enables monitoring on a particular drive.
ms.assetid: f3140f6d-d190-46a4-8587-c2e928ac8ecf
keywords:
- Enable method System Restore
- Enable method System Restore , SystemRestore class
- SystemRestore class System Restore , Enable method
topic_type:
- apiref
api_name:
- SystemRestore.Enable
api_location:
- Root\Default
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Enable method of the SystemRestore class

Enables monitoring on a particular drive.

## Syntax


```mof
uint32 Enable(
  [in] String Drive
);
```



## Parameters

<dl> <dt>

*Drive* \[in\]
</dt> <dd>

The drive to be enabled. The drive string should be of the form "C:\\". If this parameter is the system drive or an empty string (""), all drives are monitored.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the method returns one of the COM error codes defined in WinError.h.

## Remarks

The **Enable** method does not wait for monitoring to be enabled completely before it returns, because this could take a while. Instead, it returns immediately after starting the System Restore service and filter driver.

To enable System Restore on a non-system drive, you must first enable System Restore on the system drive.

This method fails in safe mode.

## Examples


```VB
'Enable Method of the SystemRestore Class
'Enables monitoring on a particular drive.

Set Args = wscript.Arguments
If Args.Count() > 0 Then
    Drive = Args.item(0)
Else 
    Drive = ""
End If

Set obj = GetObject("winmgmts:{impersonationLevel=impersonate}!root/default:SystemRestore")
If (obj.Enable(Drive)) = 0 Then
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

 

 





