---
description: Sets or gets the default quota threshold.
ms.assetid: d3f23e52-586f-4cb8-b91c-44a71f8f94b2
title: DiskQuotaControl.DefaultQuotaThreshold property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.DefaultQuotaThreshold
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.DefaultQuotaThreshold property

Sets or gets the default quota threshold.

This property is read/write.

## Syntax


```JScript
iDefaultQuotaThreshold = DiskQuotaControl.DefaultQuotaThreshold
DiskQuotaControl.DefaultQuotaThreshold = iDefaultQuotaThreshold
```



## Property value

An **Integer** value that is set to the default warning threshold for new users, in bytes.

## Remarks

The default quota threshold is applied automatically to new users of the volume. If a user's disk usage exceeds this value and the [**LogQuotaThreshold**](diskquotacontrol-logquotathreshold.md) property is set to **TRUE**, the system generates an event log entry. For example, if the default threshold is 10.0 MB, the value of the property is "10.0 MB". If the volume has no default threshold, the property is set to "No Limit" or the localized equivalent.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DiskQuotaControl**](diskquotacontrol-object.md)
</dt> </dl>

 

 




