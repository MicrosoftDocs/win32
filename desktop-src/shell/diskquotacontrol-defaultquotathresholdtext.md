---
description: Gets the default quota threshold as a text string.
ms.assetid: 48b1cbd5-12dd-4c31-a14c-7904d29f6eb9
title: DiskQuotaControl.DefaultQuotaThresholdText property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.DefaultQuotaThresholdText
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.DefaultQuotaThresholdText property

Gets the default quota threshold as a text string.

This property is read-only.

## Syntax


```JScript
DefaultQuotaThresholdText = DiskQuotaControl.DefaultQuotaThresholdText
```



## Property value

A string value that contains the default quota threshold for the volume.

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

 

 




