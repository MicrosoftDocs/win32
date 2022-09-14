---
description: Sets or gets a Boolean value that indicates whether a system event log entry will be made when a user exceeds his or her assigned quota threshold.
ms.assetid: 93bf5a4b-a887-4403-8c61-9ca8ba430c47
title: DiskQuotaControl.LogQuotaThreshold property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.LogQuotaThreshold
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.LogQuotaThreshold property

Sets or gets a Boolean value that indicates whether a system event log entry will be made when a user exceeds his or her assigned quota threshold.

This property is read/write.

## Syntax


```JScript
bLogQuotaThreshold = DiskQuotaControl.LogQuotaThreshold
DiskQuotaControl.LogQuotaThreshold = bLogQuotaThreshold
```



## Property value

This property is set to **TRUE** if a system event log entry is made when the user exceeds his or her quota warning threshold, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DefaultQuotaThreshold**](diskquotacontrol-defaultquotathreshold.md)
</dt> <dt>

[**DiskQuotaControl Object**](diskquotacontrol-object.md)
</dt> <dt>

[**LogQuotaLimit**](diskquotacontrol-logquotalimit.md)
</dt> </dl>

 

 




