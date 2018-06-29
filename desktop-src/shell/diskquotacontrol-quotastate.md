---
Description: Sets or gets the state of the volume's disk quotas.
title: DiskQuotaControl.QuotaState property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.QuotaState
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.QuotaState property

Sets or gets the state of the volume's disk quotas.

This property is read/write.

## Syntax


```JScript
iQuotaState = DiskQuotaControl.QuotaState
DiskQuotaControl.QuotaState = iQuotaState
```



## Property value

This property can be set to one of the following values.



| State          | Value | Description               |
|----------------|-------|---------------------------|
| dqStateDisable | 0     | Disk quotas are disabled. |
| dqStateTrack   | 1     | Disk quotas are disabled. |
| dqStateEnforce | 2     | Enforce quota limit.      |



 

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DiskQuotaControl Object**](diskquotacontrol-object.md)
</dt> </dl>

 

 




