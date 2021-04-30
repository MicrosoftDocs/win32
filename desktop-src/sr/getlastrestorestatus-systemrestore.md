---
title: GetLastRestoreStatus method of the SystemRestore class
description: Retrieves the status of the last system restore.
ms.assetid: 03f9fd71-9f20-428e-bdca-4692e838581a
keywords:
- GetLastRestoreStatus method System Restore
- GetLastRestoreStatus method System Restore , SystemRestore class
- SystemRestore class System Restore , GetLastRestoreStatus method
topic_type:
- apiref
api_name:
- SystemRestore.GetLastRestoreStatus
api_location:
- Root\Default
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetLastRestoreStatus method of the SystemRestore class

Retrieves the status of the last system restore.

## Syntax


```mof
uint32 GetLastRestoreStatus();
```



## Parameters

This method has no parameters.

## Return value

The method returns one of the following status values.



| Return value                                                                 | Description                                  |
|------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>0</dt> </dl> | The last restore failed.<br/>          |
| <dl> <dt>1</dt> </dl> | The last restore was successful.<br/>  |
| <dl> <dt>2</dt> </dl> | The last restore was interrupted.<br/> |



 

## Examples


```VB
'GetLastRestoreStatus Method of the SystemRestore Class
'Retrieves the status of the last system restore.
Set obj = GetObject("winmgmts:{impersonationLevel=impersonate}!root/default:SystemRestore")
stat = obj.GetLastRestoreStatus()
If stat = 0 Then
    wscript.Echo "Failed"
ElseIf stat = 1 Then 
    wscript.Echo "Success"
ElseIf stat = 2 Then
    wscript.Echo "Interrrupted"
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

 

 





